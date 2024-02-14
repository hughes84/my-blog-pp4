"""
Nutrition Blog - Views
----------------
Views for Nutrition Blog

"""

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic, View
from django.http import HttpResponseRedirect, JsonResponse
from django.core.mail import EmailMessage
from django.conf import settings
from django.views.generic import DeleteView
from django.apps import apps
from django.contrib import messages
from .models import Post, Hero, Recipe, Profile, Comment
from .forms import CommentForm, ContactForm, UserUpdateForm, ProfileUpdateForm, RecipeForm

# pylint: disable=no-member

class HomeView(View):
    """View for rendering the home page."""
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        """Handle GET request and render the home page."""
        hero_instance = Hero.objects.first()
        return render(request, self.template_name, {'hero': hero_instance})


class PostList(generic.ListView):
    """View for displaying a list of published posts."""
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blogs.html"
    paginate_by = 6


class PostDetail(View):
    """View for displaying details of a specific post and handling comments."""
    def get(self, request, slug, *args, **kwargs):
        """Handle GET request and render post details."""
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(request, "post_detail.html", {
            "post": post,
            "comments": comments,
            "commented": False,
            "liked": liked,
            "comment_form": CommentForm()
        })

    def post(self, request, slug, comment_id=None, *args, **kwargs):
        """Handle POST request for adding comments to a post."""
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            if comment_id:
                existing_comment = get_object_or_404(Comment, pk=comment_id)
                existing_comment.email = request.user.email
                existing_comment.name = request.user.username
                existing_comment.body = comment_form.cleaned_data['body']
                existing_comment.post = post
                existing_comment.save()
                messages.success(request, 'Comment updated')
            else:
                comment_form.instance.email = request.user.email
                comment_form.instance.name = request.user.username
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.save()
                messages.success(request, 'New comment added')
        else:
            messages.error(request, comment_form.errors)
        return redirect('post_detail', post.slug)


def delete_comment(request, comment_id):
    """
    Handle deleting comments.
    """
    Comment.objects.filter(id=comment_id).delete()
    return JsonResponse({'status':'success','message':'Comment deleted'},status=200)

class PostLike(View):
    """View for handling post likes."""
    def post(self, request, slug, *args, **kwargs):
        """Handle POST request to toggle post likes."""
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

class AboutUs(View):
    """View for rendering the About Us page."""
    template_name = 'aboutus.html'

    def get(self, request, *args, **kwargs):
        """Handle GET request and render the About Us page."""
        return render(request, self.template_name)

class Contact(View):
    """View for rendering the Contact page and handling contact form submissions."""
    template_name = 'contact.html'

    def get(self, request, *args, **kwargs):
        """Handle GET request and render the Contact page."""
        form = ContactForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        """Handle POST request for processing contact form submissions."""
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Send email
            subject = 'Contact Form Submission'
            body = f'Name: {name}\nEmail: {email}\nMessage: {message}'
            to_email = settings.EMAIL_HOST_USER
            email_message = EmailMessage(subject, body, to=[to_email])
            email_message.send()
            return render(request, 'thankyou.html')
        form = ContactForm()
        return render(request, self.template_name, {'form': form})


class RecipesView(View):
    """View for rendering the Recipes page."""
    template_name = 'recipes.html'

    def get(self, request, *args, **kwargs):
        """Handle GET request and render the Recipes page."""
        recipes = Recipe.objects.all()
        form = RecipeForm()
        context = {'recipes': recipes, 'form': form}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        """
        Handle POST requests for updating user profiles.
        """

        if request.method == 'POST':
            form = RecipeForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Recipe added!')

                return redirect('recipes')
            messages.error(request, form.errors)
        return redirect('recipes')

class RecipeDetailView(View):
    """View for rendering details of a specific recipe."""
    template_name = 'recipedetail.html'

    def get(self, request, recipe_id, *args, **kwargs):
        recipe = get_object_or_404(Recipe, id=recipe_id)
        context = {'recipedetail': recipe}
        return render(
            request,
            self.template_name,
            context
        )

class GenericObjectDeleteView(DeleteView):
    """
    View class for deleting a generic object based on the URL parameters.
    """
    def get_object(self, queryset=None):
        """
        Retrieve the object to be deleted based on the URL parameters.
        Args:
            queryset: The queryset to use for retrieving the object.
        Returns:
            Model: The object to be deleted.
        """
        try:
            # Get the model class based on the URL parameter
            model_name = self.kwargs['model']
            model = apps.get_model(app_label='blog', model_name=model_name)
            # Get the object to be deleted
            obj_pk = self.kwargs['pk']
            obj = get_object_or_404(model, pk=obj_pk)
            return obj
        except (LookupError, ValueError, KeyError) as e:
            # Handle lookup errors, value errors, or key errors
            return JsonResponse({'status': 'error',
                                 'message': f'Error retrieving object: {str(e)}'})
    def delete(self, request, *args, **kwargs):
        # NOTE: request, *args, **kwargs are not used in this function
        # but django needs them
        """
        Handle DELETE requests to delete an object.
        Args:
            request (HttpRequest): The HTTP request object.
            args: Additional positional arguments.
            kwargs: Additional keyword arguments.
        Returns:
            JsonResponse: JSON response indicating the status of the operation.
        """
        try:
            # Get the object to be deleted
            obj = self.get_object()
            model_name = obj.__class__.__name__
            # Delete the object
            obj.delete()
            # Override the delete method to return a JSON response
            return JsonResponse({'status': 'success', 'message': f'{model_name[:-6]} deleted'})
        except Exception as e:
            # Handle other exceptions
            return JsonResponse({'status': 'error', 'message': f'Error deleting object: {str(e)}'})
    def get_context_data(self, **kwargs):
        """
        Get the context data for rendering the template.
        Returns:
            dict: A dictionary containing context data.
        """
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.kwargs['model']
        return context

class ProfileView(View):
    """
    View for displaying and updating user profiles.
    """

    template_name = 'user_profile.html'


    def get(self, request, *args, **kwargs):
        """
        Handle GET requests to display the user profile page.
        """

        profile = get_object_or_404(Profile, user=request.user)
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=profile)

        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):

        """
        Handle POST requests for updating user profiles.
        """

        if request.method == 'POST':
            profile = get_object_or_404(Profile, user=request.user)
            user_form = UserUpdateForm(request.POST, instance=request.user)
            profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=profile)
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                messages.success(request, 'Your account has been updated!')
                return redirect('profile')
        return redirect('profile')