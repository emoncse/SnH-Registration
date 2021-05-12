from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Recruitment, Apply
from .resources import RecruitmentResources
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse


def simple_upload(request):
    if request.method == 'POST':
        resource = Recruitment()
        dataset = Dataset()
        new_res = request.FILES['myfile']

        imported_data = dataset.load(new_res.read(), format='xlsx')
        print(imported_data)
        for data in imported_data:
            # print(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
            value = Recruitment(name=data[1],
                                email=data[2],
                                reg=data[3],
                                phone=data[4],
                                blood=data[5],
                                address=data[6],
                                )
            value.save()

            # result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        # if not result.has_errors():
        #    person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'upload.html')


def application(request):
    if request.method == 'POST':
        if request.POST['submit'] == 'Submit':
            id = request.POST.get('id')
            id = '0' + id
            try:
                data = Recruitment.objects.filter(reg=id)
            except Recruitment.DoesNotExist:
                data = None
            if data is None:
                return HttpResponse("Student not found. Please try again with a valid registration number. Go home -> "
                                    "https://snhclub.org/apply")
            name = data.get().name
            rid = data.get().reg[1:]
            email = data.get().email[1:]
            phone = data.get().phone[:9] + '**'
            blood = 'Blood Group : ' + data.get().blood
            address = 'Address : ' + data.get().address
            context = {
                'open': 'open',
                'name': name,
                'rid': rid,
                'email': email,
                'phone': phone,
                'blood': blood,
                'address': address
            }
            return render(request, "apply.html", context)
        if request.POST['submit'] == 'Apply':
            reg = request.POST['id']
            email = request.POST['email']
            extra = request.POST['extra']
            interest = request.POST['interest']
            why = request.POST['why']
            registration_complete = Apply(reg=reg, extra=extra, interest=interest, why=why)
            print(registration_complete)
            registration_complete.save()

            send_mail(
                "Welcome to Software and Hardware Club",
                "You application for Software & Hardware Club Member recruitment is successfully submitted. "
                "Please, wait for the another email for the schedule of oral viva. "
                "We will send you an email very shortly.\n\nThanks for being with SnH Club.",
                settings.EMAIL_HOST_USER,
                [email]
            )
            return render(request, 'history.html')
    return render(request, 'apply.html', {'open': 'closed'})


def history(request):
    return render(request, 'history.html')
