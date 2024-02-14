"""
Nutrition Blog - URLS
----------------
URLS configuration for Nutrition Blog

"""
from django.urls import path
from . import views



urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('posts', views.PostList.as_view(), name='posts'),
    path('<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/<int:comment_id>', views.PostDetail.as_view(), name='edit_comment'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('aboutus/', views.AboutUs.as_view(), name='aboutus'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('recipes/', views.RecipesView.as_view(), name='recipes'),
    path('recipedetail/<int:recipe_id>/', views.RecipeDetailView.as_view(), name='recipedetail'),
    path('delete/<int:comment_id>/',
        views.delete_comment, name='delete'),
    path('profile/', views.ProfileView.as_view(), name='profile'),

]
