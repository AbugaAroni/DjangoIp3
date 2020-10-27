from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    bio = models.TextField()
    contactinfo = models.IntegerField(default=0)

    def __str__(self):
        return self.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    class Meta:
        ordering = ['username']


class Project(models.Model):
    title = models.CharField(max_length =60)
    project_details = models.TextField()
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

class Rating(models.Model):
    userid = models.ForeignKey(User,on_delete=models.CASCADE)
    projectid = models.ForeignKey(Project,on_delete=models.CASCADE)
    design = models.IntegerField(default=0)
    usablity = models.IntegerField(default=0)
    content = models.IntegerField(default=0)
