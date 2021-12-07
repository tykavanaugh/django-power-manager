from django.db import models
from django.core import validators
from django.conf import settings

# Choices lists

country_choices = (
    ('US','America'),
    ('Malaysia','Malaysia'),
    ('Ukraine','Ukraine'),
    ('UK','Great Britain and Northern Ireland'),
    ('Kenya','Kenya'),
    ('Netherlands','Netherlands'),
    ('Canada','Canada'),
    ('Austria','Austria'),
    ('Germany','Germany'),
    ('Colombia','Colombia'),
    ('Israel','Israel'),
    ('Brazil','Brazil'),
    ('Indonesia','Indonesia'),
    ('Denmark','Denmark'),
    ('Italy','Italy'),
    ('Australia','Australia'),
    ('Greece','Greece'),
    ('Russia','Russian Federation'),
    ('Pakistan','Pakistan'),
    ('Nigeria','Nigeria'),
    ('China','China'),
    ('Poland','Poland'),
    ('Turkey','Turkey'),
    ('Japan','Japan'),
    ('Mexico','Mexico'),
    ('Sweden','Sweden'),
    ('India','India'),
    ('Philippines','Philippines'),
    ('N Korea',"The Democratic People's Republic of Korea"),
    ('Spain','Spain'),
    ('Ireland','Ireland'),
    ('Egypt','Egypt'),
    ('Argentina','Argentina'),
    ('S Korea','The Republic of Korea'),
    ('Iran','Iran'),
    ('France','French Republic'),
    ('Saudi Arabia','Saudi Arabia'),
    ('Syria','Syria'),
    ('NZ','New Zealand'),
) 

sector_types = (
    ('Agriculture','Agriculture'),
    ('Automobiles','Automobiles'),
    ('Defense','Defense'),
    ('Financial','Financial'),
    ('Healthcare','Healthcare'),
    ('Manufacturing','Manufacturing'),
    ('Media','Media'),
    ('Mining','Mining'),
    ('Oil and gas','Oil and gas'),
    ('Retail','Retail'),
    ('Technology','Technology'),
)

paramilitary_types = (
    ('Government','Government'),
    ('Crime','Crime'),
    ('Insurgent','Insurgent'),
)

# Create your models here.

#TODO enforce party/country

class Assignment(models.Model):
    name = models.CharField(max_length=100)
    content = models.CharField(max_length=5000)
    isDone = models.BooleanField(default=False)
    manager = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='given_assignments')
    def __str__(self):
        return f"""Assignment {self.id}: {self.name}:
        {self.content}
        Completed: {self.isDone}
        Manager: {self.manager}
        """

class Country(models.Model):
    name = models.CharField(max_length=100,choices=country_choices,unique=True)
    class Meta:
        verbose_name_plural = "Countries"
    def __str__(self):
        return f"{self.name}"

class Region(models.Model):
    country = models.ForeignKey('Country', on_delete=models.CASCADE,related_name='country_regions')
    name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.country}: {self.name}"

class Party(models.Model):
    name = models.CharField(max_length=40)
    country = models.ForeignKey('Country', on_delete=models.CASCADE,related_name='country_parties')
    class Meta:
        verbose_name_plural = "Parties"
    def __str__(self):
        return f"{self.name} party in {self.country}"

class Corporation(models.Model):
    name = models.CharField(max_length=40)
    specialization = models.CharField(max_length=50,choices=sector_types)
    def __str__(self):
        return f"{self.name}- {self.specialization} company"

class Union(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return f"{self.name} Union"

class Sector(models.Model):
    type = models.CharField(max_length=50,choices=sector_types)
    region = models.ForeignKey('Region', on_delete=models.CASCADE,related_name='region_sectors')
    corporations = models.ForeignKey('Corporation', on_delete=models.CASCADE,related_name='corp_sectors',null=True,default=None,blank=True )
    unions = models.ForeignKey('Union', on_delete=models.CASCADE,related_name='union_sectors',null=True,default=None,blank=True )
    def __str__(self):
        return f"""{self.type} sector of {self.region}:
        Corporations: {self.corporations}
        Unions: {self.unions}
        """

class Paramilitary(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey('Country', on_delete=models.CASCADE,related_name='paramilitaries')
    type = models.CharField(max_length=20,choices=paramilitary_types)
    class Meta:
        verbose_name_plural = "Paramilitaries"
    def __str__(self):
        return f"""The {self.type} {self.name} force in {self.country}:"""

class Account(models.Model):
    username = models.CharField(max_length=50)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='player_accounts')
    character_name = models.CharField(max_length=50)
    region = models.ForeignKey('Region', on_delete=models.CASCADE,related_name='region_players')
    corporation = models.ForeignKey('Corporation', on_delete=models.CASCADE,related_name='ceo',null=True,default=None,blank=True )
    paramilitary = models.ForeignKey('Paramilitary', on_delete=models.CASCADE,related_name='military_leader',null=True,default=None,blank=True )
    union = models.ForeignKey('Union', on_delete=models.CASCADE,related_name='union_boss',null=True,default=None,blank=True )
    party = models.ForeignKey('Party', on_delete=models.CASCADE, related_name='members',null=True,default=None,blank=True )
    assignments = models.ForeignKey('Assignment', on_delete=models.CASCADE, related_name='accounts',null=True,default=None,blank=True )
    class Meta:
        verbose_name_plural = "Accounts"
    def __str__(self):
        return f"""In-game Username: {self.username}\n
        Region: {self.region}\n
        Corporation: {self.corporation}\n
        Paramilitary: {self.paramilitary}\n
        Union: {self.union}\n
        Party: {self.party}
        """