from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'home.html',{'name':'Zain'})
def add(request):
     
    # print(val1)
   
    val1 = request.POST['num1']
        #return HttpResponse(val1)
    val2 = request.POST['num2']
    res  = int(val1) + int(val2) 
    return render(request,'result.html',{'result':res})
     
        
    
    #return HttpResponse('success')
    #print('successful')