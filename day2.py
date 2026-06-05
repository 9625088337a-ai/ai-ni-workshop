course_A = {'Alice', 'Bob', 'Rina', 'Charlie'}
course_B = {'Ocean', 'Sila', 'Reena', 'Frank'}

print("course A students:", course_A)
print("course B students:", course_B)

print("\nstudents in both courses:", course_A & course_B)        # intersection
print("students in either course:", course_A | course_B)        # union
print("only in Course A:", course_A - course_B)                 # A minus B
print("only in one course:", course_A ^ course_B)               # symmetric difference

scores_with_duplicates = [85, 92, 78, 92, 95, 85]
unique_scores = list(set(scores_with_duplicates))               # remove duplicates (order not guaranteed)

print("\noriginal scores:", scores_with_duplicates)
print("unique scores:", unique_scores)



student = {
    "name":"Alice",
    "age":20,
    "scores":[85,92,78],
    "Hobbies":"football",
    "department":"Computer science",
    "is active":True
}
print("Student Dictionary:")
print(student)

print("\nStudent name:",student['name'])
print("Student scores:",student["age"])
print("Student scores:",student["scores"])


