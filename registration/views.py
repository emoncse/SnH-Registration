from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from tablib import Dataset
from .models import Recruitment, Apply


def simple_upload(request):
    if request.method == 'POST':
        dataset = Dataset()
        new_res = request.FILES['myfile']

        imported_data = dataset.load(new_res.read(), format='xlsx')
        print(imported_data)
        for data in imported_data:
            # print(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
            value = Recruitment(name=data[1],
                                reg=data[2],
                                email=data[3],
                                blood=data[4],
                                phone=data[5],
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
            mid = request.POST.get('id')
            try:
                data = Recruitment.objects.filter(reg__contains=mid)
            except Recruitment.DoesNotExist:
                data = None
            if data is None:
                return HttpResponse("Student not found. Please try again with a valid registration number. Go home -> "
                                    "https://snhclub.org/apply")
            name = data.get().name
            rid = data.get().reg
            if rid.startswith('0'):
                rid = rid[1:]
            else:
                rid = rid[:-2]
            email = data.get().email
            if email.startswith('0'):
                email = email[1:]
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
            if Apply.objects.filter(reg=reg).exists():
                return redirect(application)
            else:
                registration_complete = Apply(reg=reg, extra=extra, interest=interest, why=why)
                print(registration_complete)
                registration_complete.save()
                try:
                    send_mail(
                        "Welcome to Software and Hardware Club",
                        "You application for Software & Hardware Club Member recruitment is successfully submitted. "
                        "Please, wait for the another email for the schedule of oral viva. "
                        "We will send you an email very shortly.\n\nThanks for being with SnH Club.",
                        settings.EMAIL_HOST_USER,
                        [email]
                    )
                except request:
                    print("No Mail")
                return render(request, 'history.html')
    return render(request, 'apply.html', {'open': 'closed'})


def history(request):
    return render(request, 'history.html')


def applicant_view(request):
    return render(request, 'applied.html')


def applicant(request):
    list = []
    obj = Apply.objects.all()
    # Apply.objects.all().delete()
    count = 1
    for x in obj:
        dict = {
            'rid': x.reg,
        }
        print(x.reg)
        count += 1
        list.append(dict)
    context = {
        'data': list
    }
    global data_view, data_extend
    if request.method == 'POST':
        mid = request.POST.get('submit')
        cip = mid
        mid = '0' + mid
        try:
            data_view = Recruitment.objects.filter(reg=mid)
            data_extend = Apply.objects.filter(reg=cip)
        except Recruitment.DoesNotExist:
            data = None
        name = data_view.get().name
        rid = data_view.get().reg[1:]
        email = data_view.get().email[1:]
        phone = data_view.get().phone
        blood = 'Blood Group : ' + data_view.get().blood
        address = 'Address : ' + data_view.get().address
        extra = data_extend.get().extra
        interest = data_extend.get().interest
        why = data_extend.get().why
        context = {
            'open': 'open',
            'name': name,
            'rid': rid,
            'email': email,
            'phone': phone,
            'blood': blood,
            'address': address,
            'extra': extra,
            'interest': interest,
            'why': why
        }
        return render(request, "applied.html", context)
    return render(request, "list.html", context)
