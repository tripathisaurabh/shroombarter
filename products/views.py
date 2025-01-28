from django.shortcuts import get_object_or_404, render

# Home page view
from .models import About, Blog, EmailSignup, Mushroom
from .models import Slider
from .models import Service
from .models import MushroomProduct
def home(request):
    about = About.objects.first()  # Fetch the first entry for the About page
    services = Service.objects.all()  # Fetch all services
    products = MushroomProduct.objects.all()  # Fetch all products, make sure to use .objects.all()
    sliders = Slider.objects.filter(is_active=True)  # Fetch all active sliders
    mushrooms = Mushroom.objects.all()  # Fetch all mushroom entries

    return render(request, 'products/home.html', {
        'sliders': sliders,
        'services': services,
        'about': about,
        'products': products,
        'mushrooms': mushrooms,
            # Pass the correct products data (queryset) to the template

    })

# About Us page view
def about(request):
    about = About.objects.first()  # Fetch the first entry for the About page

    return render(request, 'products/about.html',{  'about': about})

# Shop page view
def shop(request):
    thank_you = False  # This will track if the email was successfully saved
    duplicate_message = False  # Flag for duplicate email
    
    if request.method == 'POST':
        email = request.POST.get('email')
        
        if email:
            email_entry, created = EmailSignup.objects.get_or_create(email=email)
            
            if created:
                thank_you = True
            else:
                duplicate_message = True  # Show duplicate message if the email exists
    
        return render(request, 'products/shop.html',  {'thank_you': thank_you, 'duplicate_message': duplicate_message})
    
    return render(request, 'products/shop.html')

# Learn page view
def learn(request):
    return render(request, 'products/learn.html')

# Community page view
def community(request):
    return render(request, 'products/community.html')

# Join Us page view
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
# from .forms import JoinUsForm

# def join(request):
#     if request.method == 'POST':
#         form = JoinUsForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']

#             # Send a confirmation email
#             subject = 'Thank You for Joining Us!'
#             body = f"Hi {name},\n\nThank you for joining ShroomBarter. We'll get in touch with you shortly."
#             send_mail(subject, body, settings.EMAIL_HOST_USER, [email])

#             # Save or process the data (if needed)
#             return HttpResponse('Thank you for joining us!')

#     else:
#         form = JoinUsForm()

#     return render(request, 'products/join.html', {'form': form})


# Contact Us page view
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
from .models import ContactUs  # Import the model for saving the contact details

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Save the contact details in the database
            contact = ContactUs(name=name, email=email, message=message)
            contact.save()  # Save the instance to the database

            

            # Render the success page and pass the user's name
            return render(request, 'products/contact_success.html', {'name': name})

    else:
        form = ContactForm()  # Empty form for GET requests

    return render(request, 'products/contact.html', {'form': form})



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'auth/login.html', {'error': 'Invalid credentials'})
    return render(request, 'auth/login.html')

def logout_view(request):
    logout(request)
    return redirect('/')


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user to the database
            messages.success(request, "Your account has been created! You can now log in.")
            return redirect('login')  # Redirect to login page
    else:
        form = UserCreationForm()
    return render(request, 'products/register.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after saving the changes
    else:
        form = ProfileForm(instance=request.user.profile)

    return render(request, 'products/profile.html', {'form': form})


def blog_list(request):
    mushrooms = Blog.objects.all()  # Replace with your query
    return render(request, 'products/blog_list.html', {'mushrooms': mushrooms})

def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'products/blog_detail.html', {'blog': blog})