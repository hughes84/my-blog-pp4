from django.contrib import admin
from .models import Post, Comment, Hero, RecipeDetail, Recipes
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

class RecipeDetailInline(admin.TabularInline):  # You can use admin.TabularInline for a more compact display
    model = RecipeDetail
    extra = 1  # Number of empty forms to display

@admin.register(Recipes)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeDetailInline]


admin.site.register(RecipeDetail)

admin.site.register(Hero)