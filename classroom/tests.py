from django.test import TestCase
from .models import SchoolYear,Classroom

# test for the creation of a new school year
class CreateNewSchoolYearTest(TestCase):
    def setUp(self):
        # creating a new school year
        SchoolYear.objects.create(year=2022)
    
    def test(self):
        # fetching the newly created school year
        school_year = SchoolYear.objects.get(year=2022)
        # testing the title of the newly created school year
        self.assertEqual(school_year.__str__(),'2022')

# test for the creation of new classrooms
class CreateNewgClassroomTest(TestCase):
    def setUp(self):
        # creating a new school year and 3 new classrooms
        school_year = SchoolYear.objects.create(year=2022)
        Classroom.objects.create(title='Class 1',school_year=school_year,join_code='abc123')
        Classroom.objects.create(title='Class 2',school_year=school_year,join_code='abc123')
        Classroom.objects.create(title='Class 3',school_year=school_year,join_code='abc123')
        
    def test(self):
        # fetching the newly created classrooms and school year
        classroom1 = Classroom.objects.get(title='Class 1')
        classroom2 = Classroom.objects.get(title='Class 2')
        classroom3 = Classroom.objects.get(title='Class 3')
        school_year = SchoolYear.objects.get(year=2022)
        # creating a list of all classes in the newly created school year
        classes = school_year.classrooms.all()
        # testing the length of the list 'classes'
        self.assertEqual(len(classes),3)
        # testing the title and school year of each newly created classroom object
        self.assertEqual(classroom1.__str__(),'Class 1 - 2022')
        self.assertEqual(classroom2.__str__(),'Class 2 - 2022')
        self.assertEqual(classroom3.__str__(),'Class 3 - 2022')