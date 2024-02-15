"""
Nutrition Blog - Models
----------------
Models for Nutrition Blog

"""

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# pylint: disable=no-member

class Hero(models.Model):
    """
    Model representing a hero section on the website's home page.
    """
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    image = models.ImageField(upload_to='hero_images/')
    content_header = models.CharField(max_length=200, blank=True)
    content = models.CharField(max_length=200, blank=True)

class Post(models.Model):
    """
    Model representing a blog post.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='place_holder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=((0, "Draft"), (1, "Published")), default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        """
        Model to provide metadata to the ModelForm.
        """
        ordering = ['-created_on']


    def number_of_likes(self):
        """
        Returns the number of likes for the blog post.
        """
        return self.likes.count()

class Comment(models.Model):
    """
    Model representing a comment on a blog post.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        """
        Model to provide metadata to the ModelForm.
        """
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

class Recipe(models.Model):
    """
    Model representing a recipe.
    """
    title = models.CharField(max_length=255)
    preparation_time = models.PositiveIntegerField()
    recipeimage = CloudinaryField('image', default='place_holder')
    servings = models.PositiveIntegerField()
    ingredients = models.TextField()
    instructions = models.TextField(default='place_holder')

    def __str__(self):
        return f"{self.title} - Details"


class Profile(models.Model):
    """
    Model representing a profile for the blog.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    image = CloudinaryField('image')

    def __str__(self):
        return f'{self.user.username} Profile'
