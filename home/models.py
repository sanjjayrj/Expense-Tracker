from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

#Create your models here.
class Addexpense_info(models.Model):
    CATEGORY = [
        ("Food","Food"),
        ("Travel","Travel"),
        ("Shopping","Shopping"),
        ("Necessities","Necessities"),
        ("Entertainment","Entertainment"),
        ("Other","Other")
    ]
    EXPENSE = [
        ("Expense","Expense"),
        ("Income","Income")
    ]
    user = models.ForeignKey(User,default = 1, on_delete=models.CASCADE)
    add_expense = models.CharField(max_length = 10 , choices = EXPENSE )
    quantity = models.BigIntegerField()
    Date = models.DateField(default = now)
    Category = models.CharField( max_length = 20, choices = CATEGORY , default ='Food')
    class Meta:
        db_table:'addexpense'
        
class UserProfile(models.Model):
    PROFESSION =[
        ("Employee","Employee"),
        ("Business","Business"),
        ("Student","Student"),
        ("Other","Other")
    ]
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profession = models.CharField(
        max_length = 10,
        choices=PROFESSION
    )
    Savings = models.IntegerField( null=True, blank=True)
    income = models.BigIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='profile_image',blank=True)
    def __str__(self):
       return self.user.username
   

