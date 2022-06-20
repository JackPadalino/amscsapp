from django.test import TestCase
from classroom.models import SchoolYear,Classroom
from .models import Forum,Topic,Question,Answer

class ForumTest(TestCase):
    def setUp(self):
        school_year = SchoolYear.objects.create(year=2022)
        Classroom.objects.create(title='Class 1',school_year=school_year,join_code='abc123')
        Classroom.objects.create(title='Class 2',school_year=school_year,join_code='abc123')
    
    def test_forum(self):
        classroom1 = Classroom.objects.get(title='Class 1')
        classroom2 = Classroom.objects.get(title='Class 2')
        forum1 = Forum.objects.get(classroom=classroom1)
        forum2 = Forum.objects.get(classroom=classroom2)
        self.assertEqual(forum1.classroom.title,'Class 1')
        self.assertEqual(forum2.classroom.title,'Class 2')
        