from django.shortcuts import render,HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .models import GeeksModel

def home(request):
    title = "Welcome"
    paragraph = "Hello, Please use and test this CRUD!!"
    return render(request,'home.html',{"title":title,"paragraph":paragraph})

def create(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        phone = request.POST.get('phone')
        zipcode = request.POST.get('zipcode')
        address = request.POST.get('address')
        g = GeeksModel(fullname=fullname,phone=phone,zipcode=zipcode,address=address)
        g.save()
        # this code will redirect my page to users
        return HttpResponseRedirect("/users")
    title="contact me"
    paragraph="hello"
    return render(request,'create.html',{"title":title,"paragraph":paragraph})


def reterive(request):
    obj = GeeksModel.objects.all()
    print(obj)

    return render(request,'users.html',{"obj":obj})

def update(request,id):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        phone = request.POST.get('phone')
        zipcode = request.POST.get('zipcode')
        address = request.POST.get('address')
        obj = GeeksModel.objects.get(id=id)
        obj.fullname = fullname
        obj.phone = phone
        obj.zipcode = zipcode
        obj.address = address
        obj.save()
        return HttpResponseRedirect("/users")
    obj = get_object_or_404(GeeksModel,id=id) #GeeksModel.objects.all().filter(id=id)
    title = "Update"
    paragraph = "Update the record"
    return render(request,'create.html',{"title":title,"paragraph":paragraph,"obj":obj})


def delete(request, id):
    obj = get_object_or_404(GeeksModel, id=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/users")
    title = "Delete"
    paragraph = "Are you sure?"
    return render(request, 'delete.html', {"title": title, "paragraph": paragraph,"obj":obj})
