print("Hello World")

name = "DEV"
faculty = "Computer Science"
dob = "01/01/2000"
age = "22"
is_student = "bbb"
gpa = "4.9"

print("Hello, " + name + "! You are a student of " + faculty + " and your date of birth is " + dob)

print(f"Hello, {name}! you are a student of {faculty} and your date of birth is {dob}.")

#check data type 
print(f"Type of name: {type(name)}")
print(f"Type of faculty: {type(faculty)}")
print(f"Type of dob: {type(dob)}")
print(f"Type of age: {type(age)}")
print(f"Type of is_student: {type(is_student)}")
print(f"Type of gpa: {type(gpa)}")

#multiple assignment 
name,faculty ,dob, age, is_student, gpa  = "Hari","BCA","2004/12/18",23,True,3.56



#Swap Variable Easily
x, y = 10,20
print("Before swap: x=",x, "y=", y )
x, y = y, x  #swap without temporary variable
print("After swap: x=",x, "y=", y )


#unpack lists
student_info = ["Charlie",21, 88.0]
name, age, score = student_info
print("Unpacked:",name, age, score )


name1,*others = student_info
print("Name:", name1)
print("Other:", others)  #this will be a list containing age and score 


#creating lists
student_names = ["Dev","Govinda","Saroj","sawan"]
student_scores = [89, 32, 35, 65]

print ("Student Names:", student_names)
print ("Student Scores:", student_scores)


#accessing elements (indexing starts at 0)
print("\nFirst  student:", student_names[0])
print ("Last student:", student_names[-1])
print("First three:", student_names[0:3])
#all students  from index 1 to end
print("Students from index 1 to end:", student_names[:])
print("Every second student:", student_names[::2])


#List operation
student_names.append("Govinda")
print("\nAfter adding Eve:", student_names)

student_names.insert(1,"Dev")
print("After adding Eve:", student_names)

student_names.remove("Saroj")
print("After adding Saroj:", student_names)

#list comprehension (power feature!)
passing_score = [score for scorw in student_scores if score >= 80]
print("\nPassing scores  (>=80):", passing_score)

#common methods 
print("Number of students:", len(student_names))
print("Highest score:", max(student_scores))
print("Lowest score:", min(student_scores))

