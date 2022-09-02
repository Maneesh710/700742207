#Create an empty  dictionary
dog={}

#Add name, color, breed, legs, age to the dog dictionary
dog={'name':'alex','color':'broen','breed':'german shepherd','legs':'4','age':'one year '}
print(dog)

#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student={'first_name':'alex','last_name':'hales','gender':'male','age':'27','martial status':'single','skills':'python','country':'USA','city':'kansas','address':'leawood'}
print(student)

#Get the length of the student dictionary
print(len(student))

#Get the value of skills and check the data type, it should be a list
s2 = list(student)
print(student.get('skills'),type(s2))
#Modify the skills values by adding one or two skills
student['skills']='java'
print(student)

#Get the dictionary keys as a list
print(list(student.keys()))

#Get the dictionary values as a list
print(list(student.values()))

