from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator

# Create your models here.
class Profile(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    bio = models.TextField()
    contactinfo = models.CharField(max_length=20)
    user_image = models.ImageField(upload_to = 'articles/')    

    def __str__(self):
        return self.username.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    class Meta:
        ordering = ['username']

class Project(models.Model):
    title = models.CharField(max_length =60)
    project_details = models.TextField()
    live_site = models.CharField(max_length =100)
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    ratedcount = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def update_project(cls,projid,newscore):
        ratedcount = cls.objects.get(id=projid)
        newcount = ratedcount.ratedcount + 1
        cls.objects.filter(id = projid).update(ratedcount = newcount)
        cls.objects.filter(id = projid).update(score = newscore)

    class Meta:
        ordering = ['title']

class Rating(models.Model):
    userid = models.ForeignKey(User,on_delete=models.CASCADE)
    projectid = models.ForeignKey(Project,on_delete=models.CASCADE)
    design = models.PositiveIntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(10)])
    usablity = models.PositiveIntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(10)])
    content = models.PositiveIntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(10)])

    def __str__(self):
        return self.projectid.title

    def save_rating(self):
        self.save()

    def delete_rating(self):
        self.delete()

    class Meta:
        ordering = ['id']
