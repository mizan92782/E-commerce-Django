from django.shortcuts import render, redirect  # For rendering templates and redirecting
from django.contrib.auth import login, authenticate  # For logging in users manually
from django.contrib.auth.tokens import default_token_generator  # For generating secure email tokens
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  # For safe encoding/decoding user ID
from django.utils.encoding import force_bytes, force_str  # For string<->byte conversion
from django.contrib.sites.shortcuts import get_current_site  # To get domain for email link
from django.template.loader import render_to_string  # To render email template
from django.core.mail import EmailMessage  # For sending email
from django.contrib import messages  # To display flash messages
from django.contrib.auth import get_backends  # Needed when using multiple authentication backends
from django.urls import reverse  # To reverse URL from view name

from .models import CustomUser  # Your custom user model





def login_profile_view(request):
    if request.user.is_authenticated:
        return render(request, 'User/profile.html')  # Show profile if already logged in

    if request.method == 'POST':
        # Get login credentials from form
        email = request.POST.get('username')
        password = request.POST.get('password')
        
       
        # Authenticate user using custom user model (USERNAME_FIELD = 'email')
        user = authenticate(request, username=email, password=password)

        if user:
            login(request, user)
            return redirect('login_profile')  # Redirect to profile after login
        else:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'User/login.html')  # Show login form







def activate_account(request, uidb64, token):
    try:
        # Decode user ID from base64
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except:
        user = None

    # Verify token and activate the user
    if user and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()

        # If multiple authentication backends, manually specify one
        backend = get_backends()[0]
        user.backend = f"{backend.__module__}.{backend.__class__.__name__}"

        # Log the user in and redirect to profile
        login(request, user)
        return redirect(request,'User/activation_success.html')  # ✅ This is your named URL for the profile page
    else:
        return render(request, 'User/activation_failed.html')  # Show error if token/user is invalid






def signup_view(request):
    if request.method == "POST":
        # Extract data from form
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        contact_number = request.POST['contact_number']
        address = request.POST['address']
        
        if password != password1:
            return render(request, 'User/signup.html', {'error': 'Passwords do not match'})

        # Prevent duplicate email signup
        if CustomUser.objects.filter(email=email).exists():
            return render(request, 'User/signup.html', {'error': 'Email already exists'})

        # Create inactive user
        user = CustomUser.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            contact_number=contact_number,
            address=address,
            is_active=False
        )

        # Prepare email activation link
        current_site = get_current_site(request)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        activate_url = f"http://{current_site.domain}{reverse('activate', kwargs={'uidb64': uid, 'token': token})}"

        # Send email
        mail_subject = 'Activate your account'
        message = render_to_string('User/verify_email.html', {
            'user': user,
            'activate_url': activate_url
        })

        email_msg = EmailMessage(mail_subject, message, to=[email])
        email_msg.content_subtype = "html"
        email_msg.send()

        return render(request, 'User/please_check_email.html')

    return render(request, 'User/signup.html')
