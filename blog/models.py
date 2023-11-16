from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
#pylint: disable=no-member


class Hero(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    image = models.ImageField(upload_to='hero_images/')
    content_header = models.CharField(max_length=200, blank=True)
    content = models.CharField(max_length=200, blank=True)

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    fetaured_image = CloudinaryField('image', default='place_holder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        ordering = ['-created_on']



    def number_of_likes(self):
        return self.likes.count()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class Recipes(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    preparation_time = models.PositiveIntegerField()
    recipeimage = CloudinaryField('image', default='place_holder')
    servings = models.PositiveIntegerField()



class RecipeDetail(models.Model):
    recipe = models.OneToOneField(Recipes, on_delete=models.CASCADE, related_name='details')
    ingredients = models.TextField()
    instructions = models.TextField()
    notes = models.TextField()
    def __str__(self):
        return f"{self.recipe.title} - Details"
