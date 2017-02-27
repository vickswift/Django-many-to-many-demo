from __future__ import unicode_literals
from django.db import models
import re

# Create your models here.
Name_Regex= re.compile(r'^[a-zA-Z]+$')

class Manager(models.Manager):
    def validateUser(self, postData):
        status = True
        errors = []

        if not Name_Regex.match(postData['name']): #check for valid name
            errors.append("Name field should contain letters only")
            status = False
        if not Name_Regex.match(postData['interest']): #check for valid interest
            status = False
        if len(postData['name']) < 1:
            errors.append("Name field can't be blank!")
            status = False

        if User.objects.filter(user_name = postData['name']):
              #if there is a user.....
            # if len(User.objects.filter(name = name).filter(interests = interest)) > 0:
            #     #user already has that interest!!!!!
            #     return False
            user = User.objects.filter(user_name=postData['name'])
            interests = user[0].interests.all()          ##???
            for interest in interests:
                print (interest.interest_name)
                if interest == interest.interest_name:
                    errors.append("")
                    return False
                else:
                    this_user = User.objects.get(user_name = postData['name'])
                    this_interest = Interest.objects.create(interest_name = postData['interest'])
                    this_interest.users.add(this_user)
                    return True
                # get user, create interest, add interest to user
        if status is True:
            user = User.objects.create(user_name = postData['name'])

            interest = Interest.objects.create(interest_name = postData['interest'])
            interest.users.add(user)
            print ("we created")
            return True
            #create user, get user, create interest, join interest to user

class User(models.Model):
    user_name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add = True)
    objects = Manager()

class Interest(models.Model):
    interest_name = models.CharField(max_length=45)
    users = models.ManyToManyField(User, related_name="interests")
    created_at = models.DateTimeField(auto_now_add = True)
