from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Hero, Recipes, RecipeDetail
from .forms import CommentForm, ContactForm
from django.core.mail import EmailMessage
from django.conf import settings

class HomeView(View):
    template_name = "index.html"
    def get(self, request, *args, **kwargs):
        hero_instance = Hero.objects.first()
        return render(
            request,
            self.template_name,
            {'hero': hero_instance}
        )


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blogs.html"
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        context = {
            "post": post,
            "comments": comments,
            "commented": True,
            "comment_form": comment_form,
            "liked": liked
        }

        return render(
            request,
            "post_detail.html",
            context,
        )


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

class AboutUs(View):

    template_name = 'aboutus.html'

    def get(self, request, *args, **kwargs):

        return render(
            request,
            self.template_name,
        )

class Contact(View):

    template_name = 'contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        return render(
            request,
            self.template_name,
            {'form': form},
        )

    def post(self, request):
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

    template_name = 'recipes.html'

    def get(self, request, *args, **kwargs):
        recipes = Recipes.objects.all()
        context = {'recipes': recipes}
        return render(
            request,
            self.template_name,
            context,
        )

class RecipeDetailView(View):

    template_name = 'recipedetail.html'

    def get(self, request, recipe_id, *args, **kwargs):
        recipe = get_object_or_404(Recipes, id=recipe_id)
        recipedetail = RecipeDetail.objects.filter(recipe=recipe)
        context = {'recipedetail': recipedetail[0]}
        return render(
            request,
            self.template_name,
            context
        )