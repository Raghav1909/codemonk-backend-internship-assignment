from celery import shared_task
from django.core.mail import send_mail
import os
from dotenv import load_dotenv


@shared_task
def send_verification_email(email, token):
    load_dotenv()
    subject = 'Verify your email address'
    message = f'Click the following link to verify your email: {os.getenv("BACKEND_URL")}/verify-email/{token}/'
    from_email = str(os.getenv('EMAIL_HOST_USER'))
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
    return "Done!"
