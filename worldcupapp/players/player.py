'''
from django.db import models
from models import *



class Club(models.Model): 
    clubName= models.CharField(max_length=15) 
    clubCountry = models.CharField(max_length=30) 

    def __str__(self):
        return self.clubName+" "+self.clubCountry

class Players(models.Model):
    competition = models.CharField(max_length=12, default = true)
    year = models.IntegerField()
    team = models.CharField(max_length=15)
    number = models.IntegerField()
    position = models.CharField(max_length=2)
    fullName = models.CharField(max_length=40)
    club = models.ForeignKey(Club) #ondelete
    dateOfBirth = models.DateFeild()
    isCaptain = models.BooleanFeild(default = False)
    

    def __str__(self):
        return self.fullName+" "+self.number+" "+self.position+" "+self.team+" "+self.year
'''
from django.conf import settings
from django.db import models
from django.db.models import CharField
from django.db.models import IntegerField
from django.db.models import BooleanField
from django.db.models import DateTimeField




class Player(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    Competition =CharField(max_length=12, default ="World Cup")
    Year = IntegerField(default=2018,null=True)
    Team = CharField(max_length=15,null=True)
    Number = IntegerField(null=True)
    TYPES=(
        ("ST","ST"),
        ("RW","RW"),
        ("LW","LW"),
        ("CM","CM"),
        ("DM","DM"),
        ("CB","CB"),    
        ("RB","RB"),
        ("GK","GK"),
        ("FW","FW"),
        ("DF","DF")

    )
    Position = CharField(max_length=2,choices=TYPES,null=True)
    FullName = CharField(max_length=40,null=True)
    Club =CharField(max_length=40,null=True) 
    ClubCountry=CharField(max_length=40,null=True) 
    created=DateTimeField(auto_now_add=True)
    IsCaptain = BooleanField(default = False)

    def __str__(self):
        return self.pk

   

