# products/models.py
from django.db import models
from ckeditor.fields import RichTextField


class MushroomProduct(models.Model):
    name = models.CharField(default='Product Name', help_text='Enter the name of the product', max_length=255)
    description = models.TextField(default='Product Description', help_text='Enter a description for the product')
    price = models.DecimalField(decimal_places=2, default=0.0, max_digits=10)
    image = models.ImageField(blank=True, help_text='Upload an image for the product', upload_to='mushroom_images/')
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name


from django.db import models

class Slider(models.Model):
    title = models.CharField(max_length=200, help_text="Title for the slide")
    description = models.TextField(help_text="Description for the slide", blank=True)
    image = models.ImageField(upload_to="sliders/", help_text="Upload an image for the slide")
    is_active = models.BooleanField(default=True, help_text="Check to display this slide")

    def __str__(self):
        return self.title



class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='services_images/')
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.title
    


class About(models.Model):
    title = models.CharField(max_length=200, help_text="Enter the title for the About section")
    description = RichTextField(help_text="Enter the main description text for the About section")
    short_description = models.TextField(default="Default short description here")  # Add a default value 
    image = models.ImageField(upload_to='about_images/', null=True, blank=True, help_text="Upload an image for the About section")
    banner_image = models.ImageField(upload_to='about_banners/', null=True, blank=True, help_text="Upload a banner image for the About page")

    def __str__(self):
        return self.title


# class links(models.Model):
#     name = models.CharField(max_length=200, help_text="Enter the title for the About section")
#     link = models.URLField(max_length=200)
#     def __str__(self):
#         return self.title

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

# Signal to create a Profile when a new user is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Signal to save the Profile whenever the User is saved (e.g. when updated)
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()





class Mushroom(models.Model):
    title = models.CharField(max_length=200,default="Default short description here")
    description = RichTextField(help_text="Enter the main description text for the About section")
    # short_description = models.TextField(default="Default short description here")  # Add a default value 
    image = models.ImageField(upload_to='about_images/', null=True, blank=True, help_text="Upload an image for the About section")
    # banner_image = models.ImageField(upload_to='about_banners/', null=True, blank=True, help_text="Upload a banner image for the About page")

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField(help_text="Enter the main description text for the About section")

    image = models.ImageField(upload_to='blogs/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
from django.db import models

class EmailSignup(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


# models.py
from django.db import models

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"
