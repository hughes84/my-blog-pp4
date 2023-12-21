from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment, Hero, RecipeDetail, Recipe

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
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    
    def approve_comments(self, request, queryset):
        """
        Action to approve selected comments.
        """
        queryset.update(approved=True)


# Inline configuration for RecipeDetail within Recipe admin
class RecipeDetailInline(admin.TabularInline):
    """
    Inline configuration for RecipeDetail within Recipe admin.
    """
    model = RecipeDetail
    extra = 1  # Number of empty forms to display

# Register the Recipe model with RecipeDetailInline
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the Recipe model.
    """
    inlines = [RecipeDetailInline]


# Register RecipeDetail and Hero models directly
admin.site.register(RecipeDetail)
admin.site.register(Hero)
