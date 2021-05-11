from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from registration.models import Recruitment, Apply
import pandas as pd


def home(request):
    return redirect(application)


def application(request):
    if request.method == 'POST':
        if request.POST['id'] is not None:
            id = request.POST.get('id')
            data = Recruitment.objects.get(id)
            return render(request, "apply.html", {'context': data})

        elif request.POST['extra'] is not None:
            reg = Recruitment.objects.get(request.POST['id'])
            email = request.POST['email']
            extra = request.POST['extra']
            interest = request.POST['interest']
            why = request.POST['why']
            registration = Apply(reg=reg, extra=extra, interest=interest, why=why)
            registration.save()

            send_mail(
                "Welcome to Software and Hardware Club",
                "You application for Software & Hardware Club Member recruitment is successfully submitted."
                "Please, wait for the another email with oral viva.",
                settings.EMAIL_HOST_USER,
                [email]
            )

    return render(request, 'apply.html')
