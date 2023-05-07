from django.contrib import messages

from django.shortcuts import render, redirect

from homeApp.models import District, Branches
from .models import Account
from .forms import AccountForm


# Create your views here.
def userpg(request):
    district = District.objects.all()
    if request.user.is_authenticated:
        return render(request, 'user.html', {'dist': district})
    else:
        return redirect('/')


def apply(request):
    district = District.objects.all()
    form = AccountForm()
    return render(request, 'card.html', {'dist': district, 'form': form})


def add(request):
    dist = District.objects.all()
    form = AccountForm()
    if request.method == 'POST':
        name = request.POST['name']
        DOB = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        district = request.POST['district']
        dist1 = District.objects.get(id=district)
        print(dist1)
        branch = request.POST['branch']
        branch1 = Branches.objects.get(id=branch)
        account = request.POST['account']
        cc = request.POST.get('cc')
        if cc == 'on':
            cc = True
        else:
            cc = False
        db = request.POST.get('db')
        if db == 'on':
            db = True
        else:
            db = False
        cb = request.POST.get('cb')
        if cb == 'on':
            cb = True
        else:
            cb = False
        Uaccount = Account.objects.create(name=name, DOB=DOB, age=age, gender=gender, phone=phone, email=email, address=address, district=dist1, branch=branch1, account=account, cc=cc, cb=cb, db=db)
        Uaccount.save()

        return render(request, 'success.html')

# AJAX
def load_branches(request):
    print('started')
    district_id = request.GET.get('district_id')
    branches = Branches.objects.filter(Tdistrict=district_id).all()
    return render(request, 'branches.html', {'branches': branches})