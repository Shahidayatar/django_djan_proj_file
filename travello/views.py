from django.shortcuts import render
from .models import destination


# Create your views here.
def index(request):



    dests = destination.objects.all()    #  to execute this  we are going to make change in index.html file(for imaage)




    #dest1 = destination()   # we are commenting this because we are getting the destination from database..
    #dest1.name = 'mumbai'
    #dest1.desc = "city that never sleeps"
    #dest1.img = 'destination_1.jpg'
    #dest1.price = 1000
    #dest1.offer = True

    #dest2 = destination()
    #dest2.name = 'Warsaw'
    #dest2.desc = "capital"
    #dest2.img = 'destination_2.jpg'
    #dest2.price = 1250
    #dest2.offer = False

    #dest3 = destination()
    #dest3.name = 'zakopane'
    #dest3.desc = "Cold place"
    #dest3.img = 'destination_3.jpg'
    #dest3.price = 1500
    #dest3.offer = False  # python manage.py help , this will help in all django stuff

    # dests = [dest1, dest2, dest3]

    return render(request, 'index.html', {'dests': dests}, {'price': 700})

    # return render(request,'index.html',{'dest1':dest1}) you can pass it in index .html as dest1. price etc....
# return render(request,'index.html',{'price':453})

#  return render(request,'index.html',{'name' : "WEBSITE"}) # comment the first retun to execute this code

# try to understqnd mvt architecutre it will help you to understand how django works...
