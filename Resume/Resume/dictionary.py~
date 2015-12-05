from models import *
def yaml_dictionary(sid):
	print "Came to dictionary"
	
	Certifications=[]
	Achievements=[]
	Languages=[]
	PSS=[]
 	fields = {}
	EQ=[]
	X={}
	X2={}
	UG={}
	Projects=[]
	Student_obj=Student.objects.get(id=sid)
	Student_Details1=Student_Details.objects.filter(Student_id=sid)
	Student_Education1=Student_Education.objects.filter(Student_id=sid)
	Student_Certifications1=Student_Certifications.objects.filter(Student_id=sid)
	Student_Skills1=Student_Skills.objects.filter(Student_id=sid)
	for x in Student_Certifications1:
		Certifications.append(x.Certifcation)
	Student_Skills1=Student_Skills.objects.filter(Student_id=sid)
	Student_Projects1=Student_Projects.objects.filter(Student_id=sid)
	Student_Achievements1=Student_Achievements.objects.filter(Student_id=sid)
	for x in Student_Achievements1:
		Achievements.append(x.Achievement)
	Student_Languages1=Student_Languages.objects.filter(Student_id=sid)
	for x in Student_Languages1:
		Languages.append(x.Language)
	for x in Student_Skills1:
		d={}
		d[x.Skill]=x.Type
		PSS.append(d)


	X['Board']="SSC"
	X['University']=Student_Education1[0].X_school
	X['Year']=Student_Education1[0].X_year
	X['Aggregate']=Student_Education1[0].X_percentage
	EQ.append(X)
	X2['Board']='Intermediate'
	X2['University']=Student_Education1[0].XII_school
	X2['Year']=Student_Education1[0].XII_year
	X2['Aggregate']=Student_Education1[0].XII_percentage
	EQ.append(X2)
	UG['Board']=Student_Education1[0].UG_course+','+Student_Education1[0].UG_specialisation
	UG['University']=Student_Education1[0].UG_university
	UG['Year']=Student_Education1[0].UG_year
	UG['Aggregate']=Student_Education1[0].UG_percentage
	EQ.append(UG)
	if  Student_Education1[0].PG_course and Student_Education1[0].pG_specialisation:
		PG['Board']=Student_Education1[0].PG_course+','+Student_Education1[0].pG_specialisation
		PG['University']=Student_Education1[0].PG_university
		PG['Year']=Student_Education1[0].PG_year
		PG['Aggregate']=Student_Education1[0].PG_percentage
		EQ.append(PG)	

	
	if Student_Projects1[0].M_Title :
		Main={}
		Main['Name']=Student_Projects1[0].M_Title 
		Main['Duration']=Student_Projects1[0].M_Duration
		Main['Size']=Student_Projects1[0].M_Teamsize
		Main['Environment']=Student_Projects1[0].M_Environment
		Main['Description']=Student_Projects1[0].M_Description
		Projects.append(Main)
	if Student_Projects1[0].Mn_Title :
		Mini={}
		Mini['Name']=Student_Projects1[0].Mn_Title 
		Mini['Duration']=Student_Projects1[0].Mn_Duration
		Mini['Size']=Student_Projects1[0].Mn_Teamsize
		Mini['Environment']=Student_Projects1[0].Mn_Environment
		Mini['Description']=Student_Projects1[0].Mn_Description
		Projects.append(Mini)
	if Student_Projects1[0].A_Title :
		A={}
		A['Name']=Student_Projects1[0].A_Title 
		A['Duration']=Student_Projects1[0].A_Duration
		A['Size']=Student_Projects1[0].A_Teamsize
		A['Environment']=Student_Projects1[0].A_Environment
		A['Description']=Student_Projects1[0].A_Description
		Projects.append(A)
	
       	with open('resumeBuilder.conf', 'r') as fh:
		lines = [line.strip() for line in fh if line[0] != "#"]
   
	for line in lines:
        	lst = line.split(';')
        	if lst[1] != ' ':
                	keys = lst[1].split(',')
                	fields[lst[0]] = []
                	fields[lst[0]].append(dict.fromkeys(keys))
          	else :
                	fields[lst[0]] = None
        print fields


			
	
		
 	fields['Email']=Student_obj.Email
	fields['PhoneNum']=Student_Details1[0].Phone
	fields['Name']=Student_Details1[0].Name  
	fields['Objective']=Student_Details1[0].Headline
	fields['Address']=Student_Details1[0].Address
	fields['DOB']=Student_Details1[0].DOB
	fields['Hobbies']=Student_Details1[0].Hobbies
	fields['Languages']=Languages
	fields['Achievements']=Achievements
	fields['Certificates']=Certifications	
	fields['PSS']=PSS
	fields['EQ']=EQ
	fields['Projects']=Projects
	fields['studentId']=sid
	print "fields==",fields
	
	
