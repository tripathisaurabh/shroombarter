from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.static import serve
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('shop/', views.shop, name='shop'),
    path('learn/', views.learn, name='learn'),
    path('community/', views.community, name='community'),
    # path('join/', views.join, name='join'),
    path('blogs/', views.blog_list, name='blog_list'),
    path('blogs/<int:id>/', views.blog_detail, name='blog_detail'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),   
    path('register/', views.register, name='register'),
    path('profile/', views.profile_view, name='profile'),
]

# Serve media files in production
urlpatterns += [
    path(f'{settings.MEDIA_URL.lstrip("/")}<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
]