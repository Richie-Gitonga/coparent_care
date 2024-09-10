from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import datetime

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars/', null=True, blank=True)
    displayname = models.CharField(max_length=20, null=True, blank=True)
    info = models.TextField(null=True, blank=True) 
    
    def __str__(self):
        return str(self.user)
    
    @property
    def name(self):
        if self.displayname:
            return self.displayname
        return self.user.username 
    
    @property
    def avatar(self):
        if self.image:
            return self.image.url
        return f'{settings.STATIC_URL}images/avatar.svg'

GENDER = (
    ('M', 'MALE'),
    ('F', 'FEMALE')
)

class ChildInfo(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=256, help_text="Full name of the child",
        blank=True
    )
    gender = models.CharField(max_length=6, choices=GENDER, blank=True)
    date_of_birth = models.DateField(blank=True)
    medical_condition = models.TextField(
        help_text='comma separated values',
        blank=True
    )

    def __str__(self):
        return self.name

class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    school = models.CharField(max_length=256, blank=True)
    location = models.CharField(max_length=256, blank=True)
    from_date = models.DateField(blank=True)
    to_date = models.DateField(blank=True)
    current = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.school