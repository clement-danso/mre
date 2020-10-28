from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from mirensah.models import *
from mirensah.forms import *
from django.db.models import Sum
from mirensah.decorators import *


# Create your views here.
def empty(request):
	
	
	
	
	return render(request, 'mre_app/empty.html')
	
@login_required(login_url='login')
@allowed_users(allowed_roles=['Managers'])
def home(request):
	sales=Sales.objects.all()
	prod1=Product.objects.get(id=1)
	prod2=Product.objects.get(id=2)
	prod3=Product.objects.get(id=3)
	customers=Customer.objects.all()
	
	context={'sales':sales, 'prod1':prod1, 'prod2':prod2, 'prod3':prod3, 'customers':customers}
	return render(request, 'mirensah/dashboard.html', context)


@login_required(login_url='login')
def customer(request, pk):
	customer = Customer.objects.get(id=pk)
	sales=customer.sales_set.all()
	
	total=sales.aggregate(Sum('quantity'))['quantity__sum'] or 0.00
	
	context={'customer':customer, 'sales':sales, 'total':total}
	return render(request, 'mirensah/customer.html', context)


@login_required(login_url='login')
def createcustomer(request):
	"""form page for creating orders"""
	fm = CreateCustomerForm()
	if request.method == 'POST':
		fm = CreateCustomerForm(request.POST or None)
		if fm.is_valid():
			fm.save()
			return redirect('/home')
	
	context = {'fm':fm}
	return render (request, 'mirensah/customerfrm.html', context)
	
@login_required(login_url='login')
def updatecustomer(request, pk):
	"""form page for creating orders"""
	record = Customer.objects.get(id=pk)
	fm = CreateCustomerForm(instance=record)
	
	if request.method == 'POST':
		fm = CreateCustomerForm(request.POST or None, instance=record)
		if fm.is_valid():
			fm.save()
			return redirect('/')
	
	context = {'fm':fm}
	return render (request, 'mirensah/customerfrm.html', context)


@login_required(login_url='login')
def addsale(request, pk):
	"""form page for creating orders"""
	customer = Customer.objects.get(id=pk)
	fm = SalesForm(initial={'customer':customer})
	if request.method == 'POST':
		fm = SalesForm(request.POST or None)
		if fm.is_valid():
			fm.save()
			return redirect('/home')
	
	context = {'fm':fm, 'customer':customer}
	return render (request, 'mirensah/salesfrm.html', context)


@login_required(login_url='login')
def updatesale(request, pk):
	"""form page for creating orders"""
	record = Sales.objects.get(id=pk)
	fm = SalesForm(instance=record)
	
	if request.method == 'POST':
		fm = SalesForm(request.POST or None, instance=record)
		if fm.is_valid():
			fm.save()
			return redirect('/')
	
	context = {'fm':fm}
	return render (request, 'mirensah/salesfrm.html', context)
	
@unauthenticated_user
def register(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
			
	context = {'form':form}
	return render(request, 'mirensah/register.html', context)
	
@unauthenticated_user
def loginpage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		user = authenticate(request, username=username , password=password)
		
		if user is not None:
			login(request, user)
			return redirect('/')
			
	
	return render(request, 'mirensah/login.html')
	
def logoutuser(request):
	logout(request)
	
	return redirect('/login')
	
	
#def trying(request):
	
#	
#	form = UserCreationForm()
#	if request.method == 'POST':
#		form = UserCreationForm(request.POST)
#		if form.is_valid():
#			form.save()
	
#	context={'form':form}
#	return render(request, 'mirensah/try.html', context)
