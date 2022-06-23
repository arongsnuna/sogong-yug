from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django import forms

class Post(models.Model):
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=200, default='')
    mainphoto = models.ImageField(blank=True, null=True)
    Size = (
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
    )
    size = models.CharField(max_length=20,choices=Size, default='')
    Season = (
        ('SS', 'SS'),
        ('FW', 'FW'),
    )
    season = models.CharField(max_length=20,choices=Season, default='')
    date = models.DateTimeField(auto_now_add=True)
    Cloth_Type=(
        ('Dresses', 'Dresses'),
        ('Blouses & Shirts', 'Blouses & Shirts'),
        ('Coats', 'Coats'),
        ('Bombers', 'Bombers'),
        ('T-shirts & Tops', 'T-shirts & Tops'),
        ('Sweatshirts', 'Sweatshirts'),
        ('Cardigans & Sweaters', 'Cardigans & Sweaters'),
        ('Jackets','Jackets'),
        ('Trousers', 'Trousers'),
        ('Jeans','Jeans'),
        ('Shorts', 'Shorts'),
        ('Skirts', 'Skirts'),
        ('Nightwear', 'Nightwear'),
        ('Underwear', 'Underwear'),
    )
    cloth_type = models.CharField(max_length=20,choices=Cloth_Type, default='')
    Wash_Type=(
        ('DO NOT WASH', 'DO NOT WASH'),
        ('PERMANENT PRESS', 'PERMANENT PRESS'),
        ('GENTLE CYCLE', 'GENTLE CYCLE'),
        ('HAND WASH', 'HAND WASH'),
    )
    Temperature=(
        ('30', '30'),
        ('40', '40'),
        ('50', '50'),
        ('60', '60'),
    )
    Dry_Cleaning=(
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    Repair=(
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    washType= models.CharField(max_length=20,choices=Wash_Type, default='')
    temperature = models.CharField(max_length=20,choices=Temperature, default='')
    drycleaning= models.CharField(max_length=20,choices=Dry_Cleaning, default='')
    repair = models.CharField(max_length=20,choices=Repair, default='')

    def __str__(self):
        return self.title
