# Generated by Django 5.1.5 on 2025-01-28 12:10

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=ckeditor.fields.RichTextField(help_text='Enter the main description text for the About section'),
        ),
    ]
