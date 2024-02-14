"""
Nutrition Blog - Admin
----------------
Admin Configuration for Nutrition Blog.
"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment, Hero, Recipe

# Register the Post model with SummernoteModelAdmin
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Custom admin configuration for the Post model.
    """
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register the Comment model with custom admin configuration
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the Comment model.
    """
    list_display = ('name', 'body', 'post', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('name', 'email', 'body')



# Register the Recipe model with RecipeDetailInline
admin.site.register(Recipe)


# Register RecipeDetail and Hero models directly

admin.site.register(Hero)
