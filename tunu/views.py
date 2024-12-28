
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def contact_view(request):
    success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            # Send email to the user
            user_email_subject = "Your message has been sent!"
            user_email_message = f"""
            Hi {contact.name},

            Thank you for visiting Jaggu's Portfolio. We have received your message:
            "{contact.message}"

            We will get back to you shortly.

            Regards,
            Jagadisha Palai
            """
            send_mail(
                user_email_subject,
                user_email_message,
                settings.DEFAULT_FROM_EMAIL,  # Sender email
                [contact.email],  # Recipient email
            )

            success = True
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form, 'success': success})
