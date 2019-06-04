from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  portfolio_site = models.URLField(blank=True)
  profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
  def __str__(self):
    return self.user.username

class Gender(models.Model):
  gender = models.CharField(max_length=6,help_text='Male or Female')
  
  class Meta:
    ordering = ['gender']

  def __str__(self):
    return self.gender
	
class Company(models.Model):
  company_name = models.CharField(max_length=100,help_text='Provide your company name')
  
  class Meta:
    ordering = ['company_name']

  def __str__(self):
    return self.company_name
