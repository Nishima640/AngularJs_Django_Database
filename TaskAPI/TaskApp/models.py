from django.db import models


# Create your models here.

class Table(models.Model):
    Id = models.AutoField(primary_key= True)
    SubjectA = models.IntegerField()
    SubjectB = models.IntegerField()
    Total = models.IntegerField(null= True, default= None)
    Average = models.IntegerField(null= True, default= None)

    


    



