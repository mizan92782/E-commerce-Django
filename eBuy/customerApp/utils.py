from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.conf import settings

def send_verification_email(request, user):
    from django.urls import reverse
    token = default_token_generator.make_token(user)
    uid = user.pk
    verify_link = request.build_absolute_uri(reverse("verify_email", args=[uid, token]))
    subject = "Verify Your Email"
    message = f"Click to verify: {verify_link}"
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])



