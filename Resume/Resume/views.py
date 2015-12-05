from django.http import HttpResponse
import datetime
import os,sys
import yaml
import settings
from django.contrib.auth.models import User
from models import *
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from dictionary import yaml_dictionary
try:
    import json
except ImportError:
   from django.utils import simplejson as json
from django.core.serializers.json import DjangoJSONEncoder


def UG_courses(request):
	UG_courses=[]	
	UG_courses_obj=UG_Courses.objects.all();
	for x in UG_courses_obj:
		UG_courses.append(x.Course) 
	result=json.dumps({'success':True,'UG_courses':UG_courses},cls=DjangoJSONEncoder)
	return HttpResponse(result, mimetype='application/json')
		
def PG_courses(request):
	PG_courses=[]	
	PG_courses_obj=PG_Courses.objects.all();
	for x in PG_courses_obj:
		PG_courses.append(x.Course) 
	result=json.dumps({'success':True,'PG_courses':PG_courses},cls=DjangoJSONEncoder)
	return HttpResponse(result, mimetype='application/json')	

def Universities_list(request):
	Universities_list=[]	
	Universities_obj=Universities.objects.all();
	for x in Universities_obj:
		Universities_list.append(x.University) 
	result=json.dumps({'success':True,'Universities':Universities_list},cls=DjangoJSONEncoder)
	return HttpResponse(result, mimetype='application/json')	

def UG_specialisations(request):
	spec_ids=[]
	UG_specialisations=[]
	UGcourse=request.POST.get("UGcourse")
	course_id=UG_Courses.objects.get(Course=UGcourse)
	Specialisation_ids=UG_course_Specialisation.objects.filter(Course_id_id=course_id)
	for x in Specialisation_ids:
		spec_ids.append(x.Specialisation_id_id)
	for y in spec_ids:
		Specialisations_obj=Specialisations.objects.get(id=y)
		UG_specialisations.append(Specialisations_obj.Specialisation)
	result=json.dumps({'success':True,'UG_specialisations':UG_specialisations},cls=DjangoJSONEncoder)
	return HttpResponse(result, mimetype='application/json')	
		
def PG_specialisations(request):
	spec_ids=[]
	PG_specialisations=[]
	PGcourse=request.POST.get("PGcourse")
	course_id=PG_Courses.objects.get(Course=PGcourse)
	Specialisation_ids=PG_course_Specialisation.objects.filter(Course_id_id=course_id)
	for x in Specialisation_ids:
		spec_ids.append(x.Specialisation_id_id)
	for y in spec_ids:
		Specialisations_obj=Specialisations.objects.get(id=y)
		PG_specialisations.append(Specialisations_obj.Specialisation)
	result=json.dumps({'success':True,'PG_specialisations':PG_specialisations},cls=DjangoJSONEncoder)
	return HttpResponse(result, mimetype='application/json')	

########### page loading links
def Email_info(request):
	Student_obj=Student.objects.filter(Email=request.POST.get("Email"))
	if Student_obj:	
		Student_Details_obj=Student_Details.objects.filter(Student_id=Student_obj[0].id)
		
		Phone=Student_Details_obj[0].Phone
		Name=Student_Details_obj[0].Name
		Headline=Student_Details_obj[0].Headline
		result=json.dumps({'success':True,'Phone':Phone,'Name':Name,'Headline':Headline},cls=DjangoJSONEncoder)
		return HttpResponse(result, mimetype='application/json')	
	else:
		result=json.dumps({'success':False},cls=DjangoJSONEncoder)
		return HttpResponse(result, mimetype='application/json')		
		
def Education(request):
	Educations=[]
	Certifications=[]
	Student_Education_obj=Student_Education.objects.filter(Student_id=request.POST.get("Student_id"))
	Student_Certifications_obj=Student_Certifications.objects.filter(Student_id=request.POST.get("Student_id"))
	if Student_Certifications_obj:
		for x in Student_Certifications_obj:
			Certifications.append(str(x.Certifcation))
	if Student_Education_obj:
		Educations.append({'X_board':str(Student_Education_obj[0].X_board),
			   'X_school':str(Student_Education_obj[0].X_school),
			   'X_year':str(Student_Education_obj[0].X_year),
			   'X_percentage':str(Student_Education_obj[0].X_percentage),
			   'XII_board':str(Student_Education_obj[0].XII_board),
			   'XII_school':str(Student_Education_obj[0].XII_school),
			   'XII_year':str(Student_Education_obj[0].XII_year),
			   'XII_percentage':str(Student_Education_obj[0].XII_percentage),
			   'UG_university':str(Student_Education_obj[0].UG_university),
			   'UG_course':str(Student_Education_obj[0].UG_course),
			   'UG_specialisation':str(Student_Education_obj[0].UG_specialisation),
			   'UG_year':str(Student_Education_obj[0].UG_year),
			   'UG_percentage':str(Student_Education_obj[0].UG_percentage),
			   'PG_university':str(Student_Education_obj[0].PG_university),
			   'PG_course':str(Student_Education_obj[0].PG_course),
			   'PG_specialisation':str(Student_Education_obj[0].PG_specialisation),
			   'PG_year':str(Student_Education_obj[0].PG_year),
			   'PG_percentage':str(Student_Education_obj[0].PG_percentage),               		  	
			  })
				

		result = json.dumps({'success':True,'Educations':Educations,'Certifications':Certifications}, cls=DjangoJSONEncoder)
		return HttpResponse(result, mimetype='application/json')	
	else:
		result=json.dumps({'success':False},cls=DjangoJSONEncoder)
		return HttpResponse(result, mimetype='application/json')	


def Projects(request):
	Projects=[]
	Skills=[]
	Languages=[]
	Achievements=[]
	Student_Projects_obj=Student_Projects.objects.filter(Student_id=request.POST.get("Student_id"))
	Student_Skills_obj=Student_Skills.objects.filter(Student_id=request.POST.get("Student_id"))
	Student_Languages_obj = Student_Languages.objects.filter(Student_id=request.POST.get("Student_id"))
 	Student_Achievements_obj=Student_Achievements.objects.filter(Student_id=request.POST.get("Student_id"))
	if Student_Skills_obj:
		for x in Student_Skills_obj:
			Skills.append(str(x.Skill))
	if Student_Languages_obj:
		for x in Student_Languages_obj:
			Languages.append(str(x.Language))
	if Student_Achievements_obj:
		for x in Student_Achievements_obj:
			Achievements.append(str(x.Achievement))
	if Student_Projects_obj:
		Projects.append({'M_Title':str(Student_Projects_obj[0].M_Title),
			   'M_Duration':str(Student_Projects_obj[0].M_Duration),
			   'M_Teamsize':str(Student_Projects_obj[0].M_Teamsize),
			   'M_Description':str(Student_Projects_obj[0].M_Description),
			   'M_Environment':str(Student_Projects_obj[0].M_Environment),
			   'Mn_Title':str(Student_Projects_obj[0].Mn_Title),
			   'Mn_Duration':str(Student_Projects_obj[0].Mn_Duration),
			   'Mn_Teamsize':str(Student_Projects_obj[0].Mn_Teamsize),
			   'Mn_Description':str(Student_Projects_obj[0].Mn_Description),
			   'Mn_Environment':str(Student_Projects_obj[0].Mn_Environment),  
			   'A_Title':str(Student_Projects_obj[0].A_Title),
			   'A_Duration':str(Student_Projects_obj[0].A_Duration),
			   'A_Teamsize':str(Student_Projects_obj[0].A_Teamsize),
			   'A_Description':str(Student_Projects_obj[0].A_Description),
			   'A_Environment':str(Student_Projects_obj[0].A_Environment),  		  	
			  })

		result = json.dumps({'success':True,'Skills':Skills,'Languages':Languages,'Achievements':Achievements,'Projects':Projects}, cls=DjangoJSONEncoder)
		return HttpResponse(result, mimetype='application/json')	
	else:
		result=json.dumps({'success':False},cls=DjangoJSONEncoder)
		return HttpResponse(result, mimetype='application/json')	

def Personal(request):
	Details=[]
	Student_Details_obj=Student_Details.objects.filter(Student_id=request.POST.get("Student_id"))	
	if Student_Details_obj:
		dob=Student_Details_obj[0].DOB.strftime('%d-%m-%Y')
		address=Student_Details_obj[0].Address
		hobbies=Student_Details_obj[0].Hobbies
		result=json.dumps({'success':True,'dob':dob,'address':address,'hobbies':hobbies},cls=DjangoJSONEncoder)
		return HttpResponse(result, mimetype='application/json')	
	else:
		result=json.dumps({'success':False},cls=DjangoJSONEncoder)
		return HttpResponse(result, mimetype='application/json')	

	
############## Form Submission links
def Contact_info(request):
	Student_obj=Student()
	Student_Details_obj=Student_Details()

	Student_obj1=Student.objects.filter(Email=request.POST['Email'])
	if Student_obj1:
		Student_Details.objects.filter(Student_id=Student_obj1[0].id).delete();
		Student_Details_obj.Student_id=Student_obj1[0]
		
	else:
		Student_obj.Email=request.POST['Email']
		Student_obj.save()
		Student_Details_obj.Student_id=Student_obj

	
	Student_Details_obj.Name=request.POST['Name']
	Student_Details_obj.Phone=request.POST['Mobile']
	Student_Details_obj.Headline=request.POST['Headline']
	Student_Details_obj.save()
	return HttpResponseRedirect('/Contact_response/?Student_id='+str(Student_Details_obj.Student_id.id))
	
	
def Education_info(request):
	Certifications=[]
	Skills_set=[]
	Student_id=request.GET['Student_id']
	Student_Education_obj=Student_Education()
	Student_Certifications_obj=Student_Certifications()
	Student_obj=Student.objects.get(id=request.GET['Student_id'])
	now=datetime.datetime.now().strftime('%H:%M:%S') 
	
	if Student_Education.objects.filter(Student_id=request.GET['Student_id']):
		Student_Education.objects.filter(Student_id=request.GET['Student_id']).delete()	
	

	########  add Certifications courses to Student_Certifications table
	for x in request.POST.keys():
		if x.startswith('Certification'):
			Certifications.append(x)
	
	for y  in Certifications:
		Student_Certifications_obj=Student_Certifications()
		Student_Certifications_obj.Student_id=Student_obj
		Student_Certifications_obj.Certifcation=request.POST[y]
		Student_Certifications_obj.save()	

	
	########### saving all certificates in Certificates folder
	x_certificate =request.FILES['Xcertificate']
	x_name =request.GET['Student_id']+'-X'
	os.chdir("/home/tsuser/Resume/Resume/media/Certificates")
	if os.path.isfile(x_name):
		os.remove(x_name)
	else:
		print ""	
	x_link =settings.MEDIA_ROOT + '/Certificates/' +x_name	
	default_storage.save(x_link , ContentFile(x_certificate.read()))

	x2_certificate =request.FILES['X2certificate']
	x2_name =request.GET['Student_id']+'-XII'
	os.chdir("/home/tsuser/Resume/Resume/media/Certificates")
	if os.path.isfile(x2_name):
		os.remove(x2_name)
	else:
		print ""
	x2_link =settings.MEDIA_ROOT + '/Certificates/' +x2_name
	default_storage.save(x2_link , ContentFile(x2_certificate.read()))


	UG_certificate =request.FILES['UGcertf']
	UG_name =request.GET['Student_id']+'-UG'
	os.chdir("/home/tsuser/Resume/Resume/media/Certificates")
	if os.path.isfile(UG_name):
		os.remove(UG_name)
	else:
		print ""
	UG_link =settings.MEDIA_ROOT + '/Certificates/' +UG_name	
	default_storage.save(UG_link , ContentFile(UG_certificate.read()))

	if  len(request.FILES)>3:
		PG_certificate =request.FILES['PGcertf']
		PG_name =request.GET['Student_id']+'-PG'
		os.chdir("/home/tsuser/Resume/Resume/media/Certificates")
		if os.path.isfile(PG_name):
			os.remove(PG_name)
		else:
			print ""
		PG_link =settings.MEDIA_ROOT + '/Certificates/' +PG_name	
		default_storage.save(PG_link , ContentFile(PG_certificate.read()))
	else:
		PG_link =''

	########

	if request.POST['PGyear'] == '':
		PGyear=0
	else:	
		PGyear=request.POST['PGyear']
	if request.POST['PGmarks'] == '':
		PGmarks=0
	else:	
		PGmarks=request.POST['PGmarks']
	Student_Education_obj.X_board        =request.POST['Xboard']
	Student_Education_obj.X_school       =request.POST['Xschool']
	Student_Education_obj.X_year         =request.POST['Xyear']
	Student_Education_obj.X_percentage   =request.POST['Xmarks']
	Student_Education_obj.X_Certificate=x_link
	Student_Education_obj.XII_board      =request.POST['X2board']
	Student_Education_obj.XII_school     =request.POST['X2school']
	Student_Education_obj.XII_year       =request.POST['X2year']
	Student_Education_obj.XII_percentage =request.POST['X2marks']
	Student_Education_obj.XII_Certificate=x2_link
	Student_Education_obj.UG_university  =request.POST['UGuniv']
	Student_Education_obj.UG_course      =request.POST['UGcourse']
	Student_Education_obj.UG_specialisation=request.POST['UGspec']
	Student_Education_obj.UG_year         =request.POST['UGyear']
	Student_Education_obj.UG_percentage   =request.POST['UGmarks']
	Student_Education_obj.UG_Certificate=UG_link
	Student_Education_obj.PG_university   =request.POST['PGuniv']
	Student_Education_obj.PG_course       =request.POST['PGcourse']
	Student_Education_obj.PG_specialisation=request.POST['PGspec']
	Student_Education_obj.PG_year          =PGyear
	Student_Education_obj.PG_percentage    =PGmarks
	Student_Education_obj.PG_Certificate=PG_link
	Student_Education_obj.Student_id=Student_obj
	Student_Education_obj.save()

	#### all skills sending to PRojects page
	Skills_obj=Skills.objects.all()
	for x in Skills_obj:
		Skills_set.append(str(x.Skill))	
	return HttpResponseRedirect('/Education_response/?Student_id='+str(Student_id)+'&Skills_set='+str(Skills_set))	

def Projects_info(request):
	Skills1=[]
	Languages=[]
	Achivements=[]
	Student_id=request.GET['Student_id']
	Student_Projects_obj=Student_Projects()
	Student_obj=Student.objects.get(id=request.GET['Student_id'])

	if Student_Projects.objects.filter(Student_id=request.GET['Student_id']):
		Student_Projects.objects.filter(Student_id=request.GET['Student_id']).delete()	
	if Student_Skills.objects.filter(Student_id=request.GET['Student_id']):
		Student_Skills.objects.filter(Student_id=request.GET['Student_id']).delete()
	if Student_Languages.objects.filter(Student_id=request.GET['Student_id']):
		Student_Languages.objects.filter(Student_id=request.GET['Student_id']).delete()	
	if Student_Achievements.objects.filter(Student_id=request.GET['Student_id']):
		Student_Achievements.objects.filter(Student_id=request.GET['Student_id']).delete()
	
	for x in request.POST.keys():
		if x.startswith('Skill'):
			Skills1.append(x)
		elif x.startswith('lang'):	
			Languages.append(x)
		elif x.startswith('achievement'):
			Achivements.append(x)
		else:
			print ""

	for skill in Skills1:
		Skills_obj=Skills.objects.filter(Skill=request.POST[skill])
		Student_Skills_obj=Student_Skills()
		Student_Skills_obj.Student_id=Student_obj
		Student_Skills_obj.Skill=request.POST[skill]
		Student_Skills_obj.Type=Skills_obj[0].Skill_type
		Student_Skills_obj.save()
	for lang in Languages:
		Student_Languages_obj=Student_Languages()
		Student_Languages_obj.Student_id=Student_obj
		Student_Languages_obj.Language=request.POST[lang]
		Student_Languages_obj.save()
	for achievement  in Achivements:
		Student_Achievements_obj= Student_Achievements()
		Student_Achievements_obj.Student_id=Student_obj
		Student_Achievements_obj.Achievement=request.POST[achievement]
		Student_Achievements_obj.save()
		
	
	Student_Projects_obj.M_Title=request.POST['M_title']
	Student_Projects_obj.M_Duration=request.POST['M_duration']
	Student_Projects_obj.M_Teamsize=request.POST['M_size']
	Student_Projects_obj.M_Description=request.POST['M_desc']
	Student_Projects_obj.M_Environment=request.POST['M_env']
	Student_Projects_obj.Mn_Title=request.POST['Mn_title']
	Student_Projects_obj.Mn_Duration=request.POST['Mn_duration']
	Student_Projects_obj.Mn_Teamsize=request.POST['Mn_size']
	Student_Projects_obj.Mn_Description=request.POST['Mn_desc']
	Student_Projects_obj.Mn_Environment=request.POST['Mn_env']
	Student_Projects_obj.A_Title=request.POST['A_title']
	Student_Projects_obj.A_Duration=request.POST['A_duration']
	Student_Projects_obj.A_Teamsize=request.POST['A_size']
	Student_Projects_obj.A_Description=request.POST['A_desc']
	Student_Projects_obj.A_Environment=request.POST['A_env']
	Student_Projects_obj.Student_id=Student_obj
	Student_Projects_obj.save()
	
	return HttpResponseRedirect('/Projects_response/?Student_id='+Student_id)	

def Personal_info(request):
	Student_Details_obj=Student_Details()
	Student_obj=Student.objects.get(id=request.GET['Student_id'])
	now=datetime.datetime.now().strftime('%H:%M:%S') 
	
	if Student_Details.objects.filter(Student_id=request.GET['Student_id']):
		Student_Details.objects.filter(Student_id=request.GET['Student_id']).delete()	

	profile_pic =request.FILES['profile_pic']
	profile_name =request.GET['Student_id']
	os.chdir("/home/tsuser/Resume/Resume/media/Proficepics")
	if os.path.isfile(profile_name):
		os.remove(profile_name)
	else:
		print ""
	profile_link =settings.MEDIA_ROOT + '/Profiles/' +profile_name	
	default_storage.save(profile_link , ContentFile(profile_pic.read()))
	
	

	Student_Details_obj.DOB=datetime.datetime.strptime(request.POST['dob'], '%d-%m-%Y').strftime('%Y-%m-%d')
	Student_Details_obj.Address=request.POST['address']
	Student_Details_obj.Hobbies=request.POST['hobbies']	
	Student_Details_obj.Profile=profile_link 
	Student_Details_obj.Student_id=Student_obj
	Student_Details_obj.save()

	###### creating dictionary 
	os.chdir("/home/tsuser/Resume")	
	yaml_dictionary(request.GET['Student_id'])



        
  	html = "<html><a href='#'>You can download your resume here[ %s ]</a></html>" % now
  	return HttpResponse(html)
	

