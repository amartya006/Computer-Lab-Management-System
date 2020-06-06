from django.db import models

# Create your models here.
class Monitor(models.Model): #name of table
    
    choices1=(('TFT','TFT'),('LCD','LCD'),('LED','LED'))
    
    brand = models.CharField(max_length=20,blank=False)
    type = models.CharField(max_length=20,blank=False,choices=choices1)
    size =models.DecimalField(max_digits=4,decimal_places=1,blank=False)
    price =models.IntegerField(blank=False)
    display =models.CharField(max_length=10,blank=False)
    
    def __str__(self):
        return 'Type: {0} Price: {1}'.format(self.type, self.price)
    
    
class CPU(models.Model): #name of table
    
    brand = models.CharField(max_length=20,blank=False)
    type = models.CharField(max_length=20, blank=False)
    Processorspeed =models.DecimalField(max_digits=3,decimal_places=1,blank=False)
    price =models.IntegerField(blank=False)
    RAMgb =models.IntegerField(blank=False)
    HDDgb =models.IntegerField(blank=False)
    
    def __str__(self):
        return 'Type: {0} Price: {1}'.format(self.type, self.price)

    
class Keyboard(models.Model): #name of table
    choices2=(('Wired','Wired'),('Wireless','Wireless'))
    
    brand = models.CharField(max_length=20, blank=False)
    type = models.CharField(max_length=20, blank=False,choices=choices2)
    price =models.IntegerField(blank=False)
    
    def __str__(self):
        return 'Type: {0} Price: {1}'.format(self.type, self.price)
    
    
class Mouse(models.Model): #name of table
    choices3=(('Wired','Wired'),('Wireless','Wireless'))
    
    brand = models.CharField(max_length=20, blank=False)
    type = models.CharField(max_length=20, blank=False,choices=choices3)
    price =models.IntegerField(blank=False)
    
    def __str__(self):
        return 'Type: {0} Price: {1}'.format(self.type, self.price)