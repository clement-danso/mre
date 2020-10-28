from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
	
class Salespoint(models.Model):
	name = models.CharField(max_length=15, null=True)
	location = models.CharField(max_length=15, null=True)
	gps_address = models.CharField(max_length=15, null=True)
	
	def __str__(self):
		return self.name
		
class Product(models.Model):
	PACKAGING = (
			 ('Boxes', 'Boxes'),
			 ('Cartons', 'Cartons'),
			
			 )
	
	name = models.CharField(max_length=15, null=True)
	packaging = models.CharField(max_length=15, null=True, choices=PACKAGING)
	price = models.FloatField(null=True)
	description = models.CharField(max_length=15, null=True)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

class Flavours(models.Model):
	name = models.CharField(max_length=15, null=True)
	product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
	
	def __str__(self):
		return self.name

class Customer(models.Model):
	name = models.CharField(max_length=15, null=True)
	phone = models.CharField(max_length=15, null=True)
	location = models.CharField(max_length=15, null=True)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name
		

class Sales(models.Model):
	shop =  models.ForeignKey(Salespoint, null=True, on_delete=models.SET_NULL)
	customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
	product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
	flavour = models.CharField(max_length=15, null=True)
	quantity = models.CharField(max_length=15, null=True)
	total_amount = models.CharField(max_length=15, null=True)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.product.name
	
class Audit_Trail(models.Model):
	customer = models.CharField(max_length=15, null=True)
	product = models.CharField(max_length=15, null=True)
	flavour = models.CharField(max_length=15, null=True)
	Quantity = models.CharField(max_length=15, null=True)
	date_updated = models.DateTimeField()
