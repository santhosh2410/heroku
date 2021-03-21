from django.shortcuts import render,HttpResponse
from .models import Contact

# Create your views here.
def index(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        message=request.POST.get('message','')
        if name and email and message:
            contact=Contact(name=name,email=email,phone=phone,message=message)
            contact.save()
        else:
            return HttpResponse("ERROR")
    return render(request,'index.html')