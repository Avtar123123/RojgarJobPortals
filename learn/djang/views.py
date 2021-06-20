from django.shortcuts import render,HttpResponse,redirect
from .form import EmpForm 
  
def index(request):  
    return HttpResponse("this is created")
    # if request.method == "POST":  
    #     form = EmpForm(request.POST,request.files)  
    #     if form.is_valid():  
    #         # try:  
    #         #     return redirect('/')  
    #         # except:  
    #         #     pass  
    #         return HttpResponse("this is upload successfully")
    # else:  
    #     form = EmpForm()  
    # return render(request,'index.html',{'form':form})   
# Create your views here.
# def setsession(request):
#     request.session['name']="avtar singh soorut"
#     request.session['email']="avtar123@gmail.com"
#     return HttpResponse("session is set")
# def getsession(request):
#     stu=request.session['name']
#     stu2=request.session['email'] 
#     return HttpResponse(stu+"   "+stu2)  