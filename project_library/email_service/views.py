from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    return HttpResponse("Hello, world. You're at the email service index.")

def send_email(request):
    subject = 'Hello from futureproof'
    message = 'Hey there!'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['rookwilkes@gmail.com']

    send_mail( subject, message, email_from, recipient_list )

    return redirect('/email-service')


