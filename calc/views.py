from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

#def home(request):
 # return HttpResponse("<h1>hello world<h1>"); # you can use htmls tags here
def home(request):
   return render(request,'home.html',{'name':'shahid'} ) # out of the these two comment any function to see the othe executing
                                                        # name is making the page dynamic we are calling it in home.html

def add(request):
    val1=  int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res= val1+val2

    return render(request,"result.html",{'result': res})