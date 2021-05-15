from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django_countries.fields import Country, CountryField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(blank=True, null=True)
    # personal information
    date_of_birth = models.DateField(null=True, blank=True)
    name = models.CharField(max_length=100, unique=True)
    # contact informationpr
    email = models.EmailField()
    phone_number = PhoneNumberField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    # home address
    address1 = models.CharField("Address line 1", max_length=50)
    address2 = models.CharField(
        "Address line 2", max_length=50, null=True, blank=True
    )
    zip_code = models.CharField("ZIP / Postal code", max_length=12)
    city = models.CharField("City", max_length=50)
    country = CountryField(blank_label="(select country)")

    def __str__(self):
        return self.name


class Language(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    add_skills = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    educational_institute = models.CharField(
        max_length=300, blank=True, null=True
    )
    city = models.CharField(max_length=50, blank=True, null=True)
    country = CountryField(blank_label="(select country)")

    def __str__(self):
        return self.title


class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class CustomSection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
