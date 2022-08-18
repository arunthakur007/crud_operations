from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import GeeksModel

def home(request):
    return render(request,'base.html')

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        g = GeeksModel(name=name,email=email,message=message)
        g.save()

    title="contact me"
    paragraph="hello"
    return render(request,'create.html',{"title":title,"paragraph":paragraph})


def reterive(request):
    obj = GeeksModel.objects.all()
    return render(request,'users.html',{"obj":obj})

def update(request,id):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        print(name,email,message)
        obj = GeeksModel.objects.get(id=id)
        obj.name = name
        obj.email = email
        obj.message = message
        obj.save()
    obj = get_object_or_404(GeeksModel,id=id) #GeeksModel.objects.all().filter(id=id)
    title = "Update"
    paragraph = "Update the record"
    return render(request,'create.html',{"title":title,"paragraph":paragraph,"obj":obj})
