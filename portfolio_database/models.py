from django.db import models

# Create your models here.


class Hobbies(models.Model):

    def __str__(self):
        return "<h1 style='text-align:center;'>"+self.hobby_name + ": " + self.hobby_description + "</h1>\n"

    hobby_name = models.CharField(max_length=200)
    hobby_description = models.CharField(max_length=800)
    hobby_image = models.CharField(max_length=800, default="https://www.shutterstock.com/image-vector/default-ui-image-placeholder-wireframes-260nw-1037719192.jpg")


class Portfolio(models.Model):

    def __str__(self):
        return "<h1 style='text-align:center;'>"+self.project_name + ": " + self.project_description + "</h1>\n"

    project_name = models.CharField(max_length=200)
    project_description = models.CharField(max_length=800)
    project_image = models.CharField(max_length=800, default="https://www.shutterstock.com/image-vector/default-ui-image-placeholder-wireframes-260nw-1037719192.jpg")


class Contacts(models.Model):

    def __str__(self):
        return "<h1 style='text-align:center;'>"+self.contact_name + ": " + self.contact_email + self.contact_message + "</h1>\n"


    contact_name = models.CharField(max_length=200)
    contact_email = models.CharField(max_length=200)
    contact_message = models.CharField(max_length=1000)

