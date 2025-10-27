# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    role = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Medicine(models.Model):

    #__Medicine_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    brand = models.CharField(max_length=255, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)

    #__Medicine_FIELDS__END

    class Meta:
        verbose_name        = _("Medicine")
        verbose_name_plural = _("Medicine")


class Rx360(models.Model):

    #__Rx360_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)

    #__Rx360_FIELDS__END

    class Meta:
        verbose_name        = _("Rx360")
        verbose_name_plural = _("Rx360")



#__MODELS__END
