from django.db import models

# Create your models here.
class Products(models.Model):
    img=models.ImageField(upload_to='product')
    song=models.FileField(upload_to='music')
    def __str__(self):
        return f"{self.img}  -   {self.song}"
    
class CustomersInfo(models.Model):
    name=models.CharField(max_length=40)
    phone=models.IntegerField()
    email=models.EmailField()
    location_details=[
        ('dhaka','Dhaka'),
        ('mymensingh','Mymensingh'),
        ('khulna','Khulna'),
        ('chatragram','Chatragram'),
        ('rajshahi','Rajshahi')
    ]
    location=models.CharField(max_length=11,choices=location_details)
    payment_choise=[
        ('bkash','Bkash'),
        ('nagad','Nagad'),
        ('rocket','Rocket')
    ]
    payment=models.CharField(max_length=21,choices=payment_choise)
    age=models.IntegerField(default=14)

    """ def __str__(self):
        return f"{self.name}      {self.phone}      {self.email}      {self.location}     {self.payment}" """