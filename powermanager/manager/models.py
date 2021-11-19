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



# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=100,choices=country_choices)

class Region(models.Model):
    country = models.ForeignKey('Country', max_length=50,related_name='regions')
    name = models.CharField(max_length=100,choices=country_choices)

class Sector(models.Model):
    type = models.CharField(max_length=50,choices=sector_types)
    region = models.ForeignKey('Region', max_length=50,related_name='region_sectors')

class Corporation(models.Model):
    name = models.CharField(max_length=255)

class Union(models.Model):
    name = models.CharField(max_length=255)

class Paramilitary(models.Model):
    name = models.CharField(max_length=255)

class Account(models.Model):
    username = models.CharField(max_length=255)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='player_accounts')
    character_name = models.CharField(max_length=255)
    region = models.ForeignKey('Region', on_delete=models.CASCADE,related_name='region_players')
    corporation = models.ForeignKey('Corporation', on_delete=models.CASCADE,related_name='ceo')
    paramilitary = models.ForeignKey('Paramilitary', on_delete=models.CASCADE,related_name='military_leader')
    union = models.ForeignKey('Union', on_delete=models.CASCADE,related_name='union_boss')
