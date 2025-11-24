from django.db import models

# Create your models here.
class Products(models.Model):
    img=models.ImageField(upload_to='product')
    song=models.FileField(upload_to='music')
    def __str__(self):
        return f"{self.img}  -   {self.song}"