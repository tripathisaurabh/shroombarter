from django.contrib import admin
from .models import Blog, ContactUs, EmailSignup, Mushroom, Slider, Service, About
from ckeditor.widgets import CKEditorWidget
from . import models

# Register Mushroom model
admin.site.register(Mushroom)
admin.site.register(Blog)

# Register Slider model with custom admin
@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')

# Register Service model
admin.site.register(Service)
admin.site.register(EmailSignup)
admin.site.register(ContactUs)
# Register About model with CKEditor widget for RichTextField
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title',)
    formfield_overrides = {
        models.RichTextField: {'widget': CKEditorWidget},
    }
from django.contrib import admin
from .models import MushroomProduct

@admin.register(MushroomProduct)
class MushroomProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_featured']