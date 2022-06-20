from django.test import TestCase
from .models import SchoolYear,Classroom

# school year test
class SchoolYearTest(TestCase):
    def setUp(self):
        SchoolYear.objects.create(year=2022)
    
    def test_school_year(self):
        school_year = SchoolYear.objects.get(year=2022)
        self.assertEqual(school_year.__str__(),'2022')

# classroom test
class ClassroomTest(TestCase):
    def setUp(self):
        school_year = SchoolYear.objects.create(year=2022)
        Classroom.objects.create(title='Class 1',school_year=school_year,join_code='abc123')
        Classroom.objects.create(title='Class 2',school_year=school_year,join_code='abc123')
        Classroom.objects.create(title='Class 3',school_year=school_year,join_code='abc123')
        
    def test_classroom(self):
        classroom1 = Classroom.objects.get(title='Class 1')
        classroom2 = Classroom.objects.get(title='Class 2')
        classroom3 = Classroom.objects.get(title='Class 3')
        school_year = SchoolYear.objects.get(year=2022)
        classes = school_year.classrooms.all()
        self.assertEqual(classroom1.__str__(),'Class 1 - 2022')
        self.assertEqual(classroom2.__str__(),'Class 2 - 2022')
        self.assertEqual(classroom3.__str__(),'Class 3 - 2022')
        self.assertEqual(len(classes),3)

