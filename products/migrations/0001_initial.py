# Generated by Django 5.1.5 on 2025-01-27 19:01

import ckeditor.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter the title for the About section', max_length=200)),
                ('description', ckeditor.fields.RichTextField(help_text='Enter the main description text for the About section')),
                ('short_description', models.TextField(default='Default short description here')),
                ('image', models.ImageField(blank=True, help_text='Upload an image for the About section', null=True, upload_to='about_images/')),
                ('banner_image', models.ImageField(blank=True, help_text='Upload a banner image for the About page', null=True, upload_to='about_banners/')),
            ],
        ),
        migrations.CreateModel(
            name='Mushroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Default short description here', max_length=200)),
                ('description', ckeditor.fields.RichTextField(help_text='Enter the main description text for the About section')),
                ('image', models.ImageField(blank=True, help_text='Upload an image for the About section', null=True, upload_to='about_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Product Name', help_text='Enter the name of the product', max_length=255)),
                ('description', models.TextField(default='Product Description', help_text='Enter a description for the product')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('image', models.ImageField(blank=True, help_text='Upload an image for the product', upload_to='mushroom_images/')),
                ('is_featured', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='services_images/')),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title for the slide', max_length=200)),
                ('description', models.TextField(blank=True, help_text='Description for the slide')),
                ('image', models.ImageField(help_text='Upload an image for the slide', upload_to='sliders/')),
                ('is_active', models.BooleanField(default=True, help_text='Check to display this slide')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
