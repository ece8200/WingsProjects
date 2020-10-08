from django.db import models

# Create your models here.
class Book(models.Model):
        title = models.CharField(max_length=50)
        author = models.CharField(max_length=50)
        descr = models.CharField(max_length=150)
        price = models.FloatField()
        
   



class Category(models.Model) :
        name = models.CharField(max_length=50)
        book = models.ManyToManyField(Book)
        
       


 
    
    
class Inventory (models.Model) :
        stock = models.IntegerField()
        status = models.CharField(max_length=50)
        book = models.ManyToManyField(Book)
        store = models.ForeignKey('Store',on_delete=models.CASCADE,)

class Store (models.Model) :
        name=models.CharField(max_length=50)
        tel=models.CharField(max_length=13)
        country=models.CharField(max_length=50)
        email=models.EmailField()

class Order(models.Model) :
        status = models.CharField(max_length=50)
        date = models.DateTimeField(auto_now_add=True)
        book = models.ManyToManyField(Book)
        user = models.ForeignKey('User',on_delete=models.CASCADE,)
            
class User(models.Model) :
        name = models.CharField(max_length=50)
        username = models.CharField(max_length=50)
        paswword = models.CharField(max_length=50)
        tel = models.CharField(max_length=13)
        address = models.CharField(max_length=50)
        
class Payment (models.Model) :
        order = models.OneToOneField(Order,on_delete=models.CASCADE,primary_key=True,)
        user = models.ForeignKey('User',on_delete=models.CASCADE,)
        method = models.CharField(max_length=50)
        date = models.DateTimeField(auto_now_add=True)
        
class Reviews (models.Model) :
        book = models.OneToOneField(Book,on_delete=models.CASCADE, primary_key=True,)
        user = models.ForeignKey('User',on_delete=models.CASCADE,)
        text = models.CharField(max_length=200)
        date = models.DateTimeField(auto_now_add=True)
            