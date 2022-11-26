from email.policy import default
import sys
from django.db import models
from django.contrib.auth.models import User 
from django.conf import settings


User = settings.AUTH_USER_MODEL


# Create your models here.
class Champion(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=False)
    img = models.ImageField(upload_to=r'champions/')

    def __str__(self):
        return self.name


class Classification(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.name


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE,)
    classification = models.ForeignKey('Classification', on_delete=models.CASCADE)
    img = models.ImageField(upload_to='items/', blank=True)

    def __str__(self):
        return self.name
    

class Build(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=False)
    champion = models.ForeignKey('Champion', on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,)
    top_lane = 'Top'
    jg_lane = 'Jungle'
    mid_lane = 'Mid'
    adc_lane = 'ADC'
    sup_lane = 'Sup'
    lanes_choices = [
        (top_lane, 'Top'),
        (jg_lane, 'Jungle'),
        (mid_lane, 'Mid'),
        (adc_lane, 'ADC'),
        (sup_lane, 'Sup'),
    ]
    lanes = models.CharField(max_length=8, choices=lanes_choices, default=lanes_choices[0][0])
    initial_item = models.ForeignKey('Item', on_delete=models.CASCADE, related_name='initial')
    initial_heal = models.ForeignKey('Item', on_delete=models.CASCADE, related_name='heal')
    initial_ward = models.ForeignKey('Item', on_delete=models.CASCADE, related_name='ward')
    first_item = models.ForeignKey('Item', on_delete=models.CASCADE, related_name='first')
    second_item = models.ForeignKey('Item', on_delete=models.CASCADE, related_name="second")
    third_item = models.ForeignKey('Item', on_delete=models.CASCADE, related_name="third")
    fourth_item = models.ForeignKey('Item', on_delete=models.CASCADE, related_name='fourth')
    fifth_item = models.ForeignKey('Item', on_delete=models.CASCADE, related_name='fifth')
    sixth_item = models.ForeignKey('Item', on_delete=models.CASCADE, related_name='sixth')
    
    def __str__(self):
        return self.name
    