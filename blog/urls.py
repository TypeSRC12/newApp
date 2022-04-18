from django.urls import path
from .views import Home, about_us, blog_detail, contact_us


urlpatterns = [
    path('', Home, name='home'),
    path('blog-detail/<int:pk>/', blog_detail, name="blog-detail"),
    path('contact/', contact_us),
    path('about/', about_us),
]
