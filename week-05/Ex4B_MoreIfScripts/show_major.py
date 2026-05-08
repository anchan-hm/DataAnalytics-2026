# lookup for name of major and location of office on major code

# creating variables (can change whenever)
student_name = "Alexus"
student_major = "CSCI" #(BIOL, CSCI, ENG, HIST, MKT)

# creating lookup logic
if student_major == "BIOL":
    major = "Biology"
    department = "Science Bldg, Room 310"
elif student_major == "CSCI":
    major = "Computer Science"
    department = "Sheppard Hall, Room 314"
elif student_major == "ENG":
    major = "English"
    department = "Kerr Hall, Room 201"
elif student_major == "HIST":
    major = "History"
    department = "Kerr Hall, Room 114"
elif student_major == "MKT":
    major = "Marketing"
    department = "Westly Hall, Room 310"
else:
    major = "<unknown>"
    department = ""

# displaying output
print("Student name:", student_name)
print("Major:", major)
print("Department office:", department)
#output:Student name: Alexus
#               Major: Computer Science
#               Department office: Sheppard Hall, Room 314