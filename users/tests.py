from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile,Project,Comment,CommentNotification,AnswerNotification
from classroom.models import SchoolYear,Classroom
from forum.models import Forum,Topic,Question,Answer

# test for the creation of a profile for a newly created user
class CreateNewUserProfileTest(TestCase):
    def setUp(self):
        # creating a new user
        user1 = User.objects.create_user(username='NewUser1',email='newuser@gmail.com')
    
    def test(self):
        # fetching the profile for the newly created user
        user1 = User.objects.get(username='NewUser1')
        profile1 = Profile.objects.get(user=user1)
        # verifying that newly created profile points to the correct user
        self.assertEqual(profile1.user,user1)

# test for the creation of new projects
class CreateNewProjectTest(TestCase):
    def setUp(self):
        # creating a new user and two new projects associated with that user
        user1 = User.objects.create_user(username='NewUser1',email='newuser@gmail.com')
        Project.objects.create(user=user1,title='Project 1',blurb='Check out my project!',description='This is my first project!',video='video url')
        Project.objects.create(user=user1,title='Project 2',blurb='Check out my project!',description='This is my first project!',video='video url')
    
    def test(self):
        # fetching the newly creatd user and their projects
        user1 = User.objects.get(username='NewUser1')
        project1 = Project.objects.get(user=user1,title='Project 1')
        project2 = Project.objects.get(user=user1,title='Project 2')
        # testing the titles of each newly created project
        self.assertEqual(project1.title,'Project 1')
        self.assertEqual(project2.title,'Project 2')
        # testing that both projects were created by the same user
        self.assertEqual(project1.user,user1)
        self.assertEqual(project2.user,user1)
        # creating a list of all projects created by user1
        projects = user1.projects.all()
        # verifying the length of the list 'projects'
        self.assertEqual(len(projects),2)