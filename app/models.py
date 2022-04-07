from django.db import models

# Create your models here.

class USER(models.Model) : 
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    mobile = models.TextField()
    email = models.EmailField()
    password = models.TextField()
    pic = models.FileField(upload_to='Profile', default='images/Default.png')

    def __str__(self) :
        return self.fname + '' + self.lname
