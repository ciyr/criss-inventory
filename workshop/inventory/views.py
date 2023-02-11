from datetime import datetime
from django.shortcuts import render,redirect,HttpResponse
from django.db import IntegrityError
from .models import Inventory,Transaction
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import user_passes_test

# Create your views here.

def login(request):
    return render(request,'login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('homePage')

@login_required(login_url='/login')
def homePage(request):
    return render(request,'homePage.html')

@login_required(login_url='/login')
def searchById(request):
    search = request.GET.get('ID',None)
    inventory = Inventory.objects.filter(itemId__startswith=search)
    return render(request,'searchResults.html',{'inventory':inventory})

@login_required(login_url='/login')
def searchByName(request):
    search = request.GET.get('Name',None)
    inventory = Inventory.objects.filter(itemName__contains=search)
    return render(request,'searchResults.html',{'inventory':inventory})

@login_required(login_url='/login')
def add(request):
    staff = ["chaitanyaiyer01@gmail.com"]
    #only allow admin to add items
    if request.user.email in staff:
        if request.method == 'POST':
            try:
                itemId = request.POST.get('itemId')
                itemName = request.POST.get('itemName')
                quantity = request.POST.get('quantity')
                inventory = Inventory(itemId=itemId,itemName=itemName,quantity=quantity)
                inventory.save()
                return render(request,'homePage.html',{'message':'Item added successfully'})
        # code that produces error
            except IntegrityError as e:
                return render(request,'addNewItem.html',{'message':'Item ID already exists'})
    else:
        return render(request,'homePage.html',{'message':'You are not authorized to add items'})
    return render(request,'addNewItem.html')

@login_required(login_url='/login')
def addQuantity(request):
    if request.method == 'POST':
        itemId = request.POST.get('itemId')
        quantity = request.POST.get('quantityAdd')
        inventory = Inventory.objects.get(itemId=itemId)
        inventory.quantity += int(quantity)
        inventory.save()
        return render(request,'searchResults.html',{'message' : 'Quantity added successfully'})
    return render(request,'searchResults.html')

@login_required(login_url='/login')
def issueQuantity(request):
    if request.method == 'POST':
        itemId = request.POST.get('itemId')
        quantity = request.POST.get('quantityIssue')
        #request get user
        issuee = request.user.email
        inventory = Inventory.objects.get(itemId=itemId)
        # if inventory.quantity < int(quantity):
        #     if int(requestedQuantity) > 0:
        #         send_mail(
        #                 'Quantity Request',
        #                 'Item ID: '+itemId+'\n Item Name: '+inventory.itemName+'\n Quantity Requested: '+str(requestedQuantity) + '\n Quantity Available: '+str(inventory.quantity) + '\n Issuee: '+issuee + '\n Cost: ' + str((inventory.cost/inventory.quantity)*int(requestedQuantity)),
        #                 settings.EMAIL_HOST_USER,
        #                 ['pratinavmongia2002@gmail.com']
        #                 )
        #         return render(request,'searchResults.html',{'message' : 'Requested Successfully'})   
        #     return render(request,'searchResults.html',{'message' : 'Insufficient quantity'})
        inventory.quantity -= int(quantity)
        iName = inventory.itemName
        transaction = Transaction(itemName = iName,itemId=inventory,quantity=quantity,date=datetime.now().date(),time=datetime.now().time(),issuee=issuee)
        inventory.save()
        transaction.save()
        return render(request,'searchResults.html',{'message' : 'Issued successfully'})
    return render(request,'searchResults.html')



@login_required(login_url='/login')
def viewTransactions(request):
    staff = ["chaitanyaiyer01@gmail.com"]
    if request.user.email in staff:
        transactions = Transaction.objects.filter(approved=False)
        
        return render(request,'viewTransactions.html',{'transactions':transactions})
    else:
        return render(request,'homePage.html',{'message':'You are not authorized to view transactions'})