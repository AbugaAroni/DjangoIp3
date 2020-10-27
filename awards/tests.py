from django.test import TestCase
from .models import Profile, Project, Rating
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestClass(TestCase):
        # Set up method
    def setUp(self):
        self.abuga = User(username="rick", password="password")
        self.abuga.save()
        self.abugaprofile= Profile(username = self.abuga,  bio='testbio of this user')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.abugaprofile,Profile))

    # Testing Save Method
    def test_save_method(self):
        self.abugaprofile.save_profile()
        testsaved = Profile.objects.all()
        self.assertTrue(len(testsaved) > 0)

    # Testing Delete Method
    def test_delete_method(self):
        self.abugaprofile.save_profile()
        testsaved = Profile.objects.all()
        self.assertTrue(len(testsaved) > 0)

        self.abugaprofile.delete_profile()
        testdelete = Profile.objects.filter(username=self.abuga)
        self.assertEqual(len(testdelete), 0)

class ProjectTestClass(TestCase):

    def setUp(self):
        self.abuga = User(username="rick", password="password")
        self.abuga.save()
        self.abugaproject= Project(title = "testproject", project_details = "these are the details of the rpoject", creator = self.abuga,  score = 4)

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.abugaproject,Project))

    # Testing Save Method
    def test_save_method(self):
        self.abugaproject.save_project()
        testsaved = Project.objects.all()
        self.assertTrue(len(testsaved) > 0)

    # Testing Delete Method
    def test_delete_method(self):
        self.abugaproject.save_project()
        testsaved = Project.objects.all()
        self.assertTrue(len(testsaved) > 0)

        self.abugaproject.delete_project()
        testdelete = Project.objects.filter(title="testproject")
        self.assertEqual(len(testdelete), 0)

class RatingTestClass(TestCase):

    def setUp(self):
        self.abuga = User(username="rick", password="password")
        self.abuga.save()
        self.abugaproject= Project(title = "testproject", project_details = "these are the details of the rpoject", creator = self.abuga,  score = 4)
        self.abugaproject.save_project()

        self.abugarating = Rating(userid = self.abuga, projectid = self.abugaproject, design =10, usablity=10, content=10)

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.abugarating,Rating))

    # Testing Save Method
    def test_save_method(self):
        self.abugarating.save_rating()
        testsaved = Rating.objects.all()
        self.assertTrue(len(testsaved) > 0)

    # Testing Delete Method
    def test_delete_method(self):
        self.abugarating.save_rating()
        testsaved = Project.objects.all()
        self.assertTrue(len(testsaved) > 0)

        self.abugarating.delete_project()
        testdelete = Project.objects.filter(projectid=self.abugaproject)
        self.assertEqual(len(testdelete), 0)
