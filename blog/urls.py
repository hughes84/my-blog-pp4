from django.urls import path
from . import views



urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('posts/', views.PostList.as_view(), name='posts'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('aboutus', views.AboutUs.as_view(), name='aboutus'),
    path('contact', views.Contact.as_view(), name='contact'),
    path('recipes', views.RecipesView.as_view(), name='recipes'),
    path('recipedetail/<int:recipe_id>/', views.RecipeDetailView.as_view(), name='recipedetail'),
    path('delete/<str:model>/<int:pk>/',
        views.GenericObjectDeleteView.as_view(), name='delete_object'),

]