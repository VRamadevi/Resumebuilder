from django.db import models
import settings

class Countries(models.Model):
    Country=models.CharField(max_length=50)

    class Meta:
        db_table = "Countries"

class States(models.Model):
    State=models.CharField(max_length=50)
    class Meta:
        db_table = "States"

class Cities(models.Model):
    City=models.CharField(max_length=50)
    class Meta:
        db_table = "Cities"

class State_City(models.Model):
    city_id=models.ForeignKey(Cities)
    state_id=models.ForeignKey(States)
    class Meta:
        db_table = "State_City"

class UG_Courses(models.Model):
    Course=models.CharField(max_length=50)
    class Meta:
        db_table = "UG_Courses"

class PG_Courses(models.Model):
    Course=models.CharField(max_length=50)
    class Meta:
        db_table = "PG_Courses"


class Specialisations(models.Model):
    Specialisation=models.CharField(max_length=50)
    class Meta:
        db_table = "Specialisations"

class UG_course_Specialisation(models.Model):
	Course_id=models.ForeignKey(UG_Courses)
	Specialisation_id=models.ForeignKey(Specialisations)
	class Meta:
        	db_table = "UG_course_Specialisation"

class PG_course_Specialisation(models.Model):
	Course_id=models.ForeignKey(PG_Courses)
	Specialisation_id=models.ForeignKey(Specialisations)
	class Meta:
        	db_table = "PG_course_Specialisation"


class Universities(models.Model):
	University=models.TextField()
	class Meta:
        	db_table = "Universities"
	

class University_state(models.Model):
	University_id=models.ForeignKey(Universities)
	State_id=models.ForeignKey(States)
	class Meta:
        	db_table = "University_state"

class Skills(models.Model):
	Skill=models.CharField(max_length=50)	
	Skill_type=models.CharField(max_length=50)
	class Meta:
        	db_table = "Skills"


class Student(models.Model):
	Email=models.CharField(max_length=50)	
	class Meta:
        	db_table = "Student"

class Student_Details(models.Model):
	Student_id=models.ForeignKey(Student)
	Name=models.CharField(max_length=50)	
	Address=models.TextField()
	Pincode=models.IntegerField(default=0)
	Phone=models.IntegerField(default=0)
	Hobbies=models.TextField()
	Headline=models.TextField()
	DOB=models.DateField(auto_now_add=True)
	Profile=models.CharField(max_length=50)	
	class Meta:
        	db_table = "Student_Details"

class Student_Languages(models.Model):
	Student_id=models.ForeignKey(Student)	
	Language=models.CharField(max_length=50)	
	Proficiency=models.CharField(max_length=50)	
	Read=models.BooleanField(default=True)
	Write=models.BooleanField(default=True)
	Speak=models.BooleanField(default=True)	
	class Meta:
        	db_table = "Student_Languages"	

class Student_Projects(models.Model):
	Student_id=models.ForeignKey(Student)
	M_Title=models.CharField(max_length=50)	
	M_Duration=models.CharField(max_length=50)	
	M_Teamsize=models.CharField(max_length=50)	
	M_Description=models.TextField()
	M_Environment=models.CharField(max_length=50)
	Mn_Title=models.CharField(max_length=50)	
	Mn_Duration=models.CharField(max_length=50)	
	Mn_Teamsize=models.CharField(max_length=50)	
	Mn_Description=models.TextField()
	Mn_Environment=models.CharField(max_length=50)	
	A_Title=models.CharField(max_length=50)	
	A_Duration=models.CharField(max_length=50)	
	A_Teamsize=models.CharField(max_length=50)	
	A_Description=models.TextField()
	A_Environment=models.CharField(max_length=50)
	class Meta:
        	db_table = "Student_Projects"	
	

class Student_Education(models.Model):
	Student_id=models.ForeignKey(Student)
	X_board=models.CharField(max_length=50)	
	X_school=models.CharField(max_length=50)		
	X_year=models.IntegerField()
	X_percentage=models.IntegerField()
	X_Certificate=models.CharField(max_length=100)	

	XII_board=models.CharField(max_length=50)	
	XII_school=models.CharField(max_length=50)		
	XII_year=models.IntegerField()
	XII_percentage=models.IntegerField()
	XII_Certificate=models.CharField(max_length=100)	

        UG_university=models.CharField(max_length=50)
	UG_course=models.CharField(max_length=50)
	UG_specialisation=models.CharField(max_length=50)		
	UG_year=models.IntegerField()
	UG_percentage=models.IntegerField()
	UG_Certificate=models.CharField(max_length=100)	

	PG_university=models.CharField(max_length=50)	
	PG_course=models.CharField(max_length=50)	
	PG_specialisation=models.CharField(max_length=50)		
	PG_year=models.IntegerField()
	PG_percentage=models.IntegerField()
	PG_Certificate=models.CharField(max_length=100)		
	class Meta:
        	db_table = "Student_Education"	
	


class Student_Skills(models.Model):
	Student_id=models.ForeignKey(Student)
	Skill=models.CharField(max_length=50)	
	Type=models.CharField(max_length=50)	
	class Meta:
        	db_table = "Student_Skills"	


class Student_Achievements(models.Model):
	Student_id=models.ForeignKey(Student)
	Achievement=models.TextField()	
	class Meta:
        	db_table = "Student_Achievements"


class Student_Certifications(models.Model):
	Student_id=models.ForeignKey(Student)
	Certifcation=models.TextField()	
    	class Meta:
        	db_table = "Student_Certifications"		







