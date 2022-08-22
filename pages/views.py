from itertools import product
from django.shortcuts import render , redirect
from .models import Company
from .forms import CompanyForm

# Create your views here.

def index(request):
    context = {'name':'owaes', 'age':''}
    return render(request, 'pages/index.html',context)

def active_substance(request):
    pass

def companies(request):
    return render(request, 'pages/companies.html',{'context': Company.objects.all})

def company(request,companyid):
    return render(request, 'pages/company.html',{'context': Company.objects.get(id=companyid)})

def addcompany(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/allcompany')
    else:
        form = CompanyForm()
    return render(request, 'pages/addcompany.html',{'context': form })

def editcompany(request, companyid): 
    company = Company.objects.get(id=companyid)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('/allcompany')
    else:
        form = CompanyForm(instance=company)
    return render(request, 'pages/editcompany.html',{'context': form })