from django.db import models
from django.utils import timezone
from datetime import datetime, time

class userregtbl(models.Model):
    name=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    address=models.CharField(max_length=150)
    phone=models.CharField(max_length=150)
    gender=models.CharField(max_length=150)
    password=models.CharField(max_length=150)

class trucktbl(models.Model):
    tname=models.CharField(max_length=150)
    no_plate=models.CharField(max_length=150)
    license_no=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    password=models.CharField(max_length=150)
    status=models.CharField(max_length=150)


class categorytbl(models.Model):
    name=models.CharField(max_length=150)

class foodtbl(models.Model):
    uname=models.CharField(max_length=150)
    uid=models.CharField(max_length=150)
    food_name=models.CharField(max_length=150)
    category=models.CharField(max_length=150)
    district=models.CharField(max_length=150)
    city=models.CharField(max_length=150)
    quantity=models.CharField(max_length=150)
    type=models.CharField(max_length=150)
    p_date=models.DateField(max_length=150)
    status=models.CharField(max_length=150)

class charitytbl(models.Model):
    cname=models.CharField(max_length=150)
    c_license_no=models.CharField(max_length=150)
    member=models.CharField(max_length=150)
   
    address=models.CharField(max_length=150)
    phone=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    password=models.CharField(max_length=150)
    status=models.CharField(max_length=150)

class foodreqtbl(models.Model):
    uname=models.CharField(max_length=150)
    uid=models.CharField(max_length=150)
    food_name=models.CharField(max_length=150)
    food_id=models.CharField(max_length=150)
    date=models.DateField(max_length=150)
    status=models.CharField(max_length=150)
    cname=models.CharField(max_length=150)
    cid=models.CharField(max_length=150)

class assigntbl(models.Model):
    food_name=models.CharField(max_length=150)
    food_id=models.CharField(max_length=150)
    tname=models.CharField(max_length=150)
    status=models.CharField(max_length=150)
    cname=models.CharField(max_length=150)
    cid=models.CharField(max_length=150)
    fdreq_id=models.CharField(max_length=150)

class delivertbl(models.Model):
    food_name=models.CharField(max_length=150)
    food_id=models.CharField(max_length=150)
    tname=models.CharField(max_length=150)
    status=models.CharField(max_length=150)
    cname=models.CharField(max_length=150)
    cid=models.CharField(max_length=150)

class rewardtbl(models.Model):
    uid=models.CharField(max_length=150)
    uname=models.CharField(max_length=150)
    point=models.CharField(max_length=150)

class products(models.Model):
    name=models.CharField(max_length=150)
    quantity=models.CharField(max_length=150)
    price=models.FloatField(max_length=150)
    description=models.CharField(max_length=500)
    image=models.FileField(max_length=150)


class cartitems(models.Model):
    user=models.CharField(max_length=150)
    product_id=models.CharField(max_length=150)
    quantity=models.IntegerField()

class purchases(models.Model):
    userr=models.CharField(max_length=150)
    product=models.CharField(max_length=150)
    total_item=models.CharField(max_length=150)
    total_price=models.CharField(max_length=150)
    card_name=models.CharField(max_length=150)
    card_number=models.FloatField(max_length=150)
    cvv=models.CharField(max_length=150)
    status=models.CharField(max_length=150)

class feedbacktbl(models.Model):
    cname=models.CharField(max_length=150)
    feedback=models.CharField(max_length=150)

class complainttbl(models.Model):
    cname=models.CharField(max_length=150)
    msg=models.CharField(max_length=150)
    reply=models.CharField(max_length=150)