"""
Nutrition Blog - Apps
----------------
App Configuration for Nutrition Blog.
"""
from django.apps import AppConfig

class BlogConfig(AppConfig):
    """
    Configuration class for the 'blog' Django app.

    Attributes:
        default_auto_field (str): The default auto field for model primary keys.
        name (str): The name of the Django app.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
