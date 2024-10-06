from django.http import HttpResponse
from django.shortcuts import render, redirect
from .import forms
from .models import StudentModel

# Create your views here.

def index(request):
    return render(request, 'curdApp/index.html')

def insert(request):
     form = forms.InsertForm()
     if request.method == 'POST':
         forms.InsertForm(request.POST)
         if form.is_valid():
             print('Form validation process Successful...')
             print('name',form.cleaned_data['name'])
             print('rollno', form.cleaned_data['rollno'])
             print('school', form.cleaned_data['school'])
             print('address', form.cleaned_data['address'])
     return render(request, 'curdApp/insert.html', context = {'form':form})

def addNew(request):
    if request.method == 'POST':
        name = request.POST['name']
        rollno = request.POST['rollno']
        school = request.POST['school']
        address = request.POST['address']
        formData = StudentModel(name= name, rollno=rollno, school=school, address =address)
        formData.save()
        return HttpResponse('<h1>form submitted successfully...')
    return render(request, 'curdApp/insert.html')

def display(request):
     formData = StudentModel.objects.all()
     return render(request, 'curdApp/display.html', context={'formData':formData})

def update(request):
    formData = StudentModel.objects.all()
    return render(request, 'curdApp/update.html', context={'formData':formData})

def delete(request):
    formData = StudentModel.objects.all()
    return render(request, 'curdApp/delete.html', context={'formData':formData})

def updateRecord(request,id):
    queryset = StudentModel.objects.get(id=id)
    if request.method== 'POST':
        formData = request.POST
        name = formData.get('name')
        rollno = formData.get('rollno')
        school = formData.get('school')
        address = formData.get('address')
        queryset.name = name
        queryset.rollno = rollno
        queryset.school = school
        queryset.address= address
        queryset.save()
        return HttpResponse('<h1>Record Successfully updated....')
        # return redirect('/display/')
    return render(request, 'curdApp/updateRecord.html', context={'formData':queryset})



def deleteRecord(request,id):
    queryset = StudentModel.objects.get(id =id)
    queryset.delete()
    # return render(request, 'curdApp/delete.html', context={'queryset':queryset})
    return redirect('/delete/')
