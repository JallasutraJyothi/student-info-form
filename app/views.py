from django.shortcuts import render,redirect
from .models import Details
from rest_framework.decorators import api_view
from .serializers import StudentSerializers
from rest_framework.response import Response
# Fetch all data initially
data = Details.objects.all()

# Create your views here.
def index(request):
    if request.method == "POST":
        search = request.POST.get('search')
        data1 = Details.objects.filter(name__icontains=search)  # Adjust the field name accordingly
    else:
        data1 = data  # If no search, use all data

    context = {
        'data1': data1
    }
    return render(request, 'index.html', context)


def py(request):
    context={
        'data':data
    }
    return render(request,'py.html',context)

def jsp(request):
    context={
        'data':data
    }
    return render(request,'jsp.html',context)

def pytst(request):
    context={
        'data':data
    }
    return render(request,'pytst.html',context)

def jtst(request):
    context={
        'data':data
    }
    return render(request,'jtst.html',context)

def bank(request):
    context={
        'data':data
    }
    return render(request,'bank.html',context)

def single_details(request,pk):
    data1=Details.objects.get(id=pk)
    if request.method=="POST":
        data1.delete()
        return redirect("home")
    context={
        'data1':data1
    }
    return render(request,'singlr_details.html',context)

def update(request,fk):
    b=True
    data2=Details.objects.get(id=fk)
    if request.method=="POST":
        name=request.POST.get('name')
        qualification=request.POST.get('qualification')
        gender=request.POST.get('gender')
        age=request.POST.get('age')
        yop=request.POST.get('yop')
        course=request.POST.get('course')
        skills=request.POST.get('skills')
        mock_rating=request.POST.get('mock_rating')
        dob=request.POST.get('dob')
        address=request.POST.get('address')

        data2.name=name
        data2.qualification=qualification
        data2.gender=gender
        data2.age=age
        data2.yop=yop
        data2.course=course
        data2.skills=skills
        data2.mock_rating=mock_rating
        data2.dob=dob
        data2.address=address

        data2.save()
        return redirect("home")
        print(name,age)

    context={
        'data2':data2
    }
    return render(request,'edit.html',context)

def create(request):
    b=False
    if request.method=="POST":
        name=request.POST.get('name')
        qualification=request.POST.get('qualification')
        gender=request.POST.get('gender')
        age=request.POST.get('age')
        yop=request.POST.get('yop')
        course=request.POST.get('course')
        skills=request.POST.get('skills')
        mock_rating=request.POST.get('mock_rating')
        dob=request.POST.get('dob')
        address=request.POST.get('address')
        a=Details.objects.create(name=name,qualification=qualification,gender=gender,age=age,yop=yop,course=course,skills=skills,mock_rating=mock_rating,dob=dob,address=address)
        return redirect("home")
    return render(request,'create.html',{'b':b})

@api_view(['get'])
def api(request):
    if request.method=="GET":
        stu=Details.objects.all()
        a=StudentSerializers(stu,many=True)
        
        return Response(a.data)
