
student_list=[]
teacher_list=[]
homeroom_teacher_list=[]
x=0
y=0
z=0
# Display the available commands
print("Available commands:")
print("1. create - Create a new resource")
print("2. manage - Manage existing resources")
print("3. end    - End the program")

class student:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.student_data = {} #create a dictionary for every object of the class
        self.classnames=[] #creates a list for every object

    def entry(self):
        self.first_name=input("please enter the first name of the student")
        self.last_name = input("please enter the last name of the student")
        while True:
            studentclasses=input("please enter the class/es the student attends")
            if studentclasses == "":
                break
            self.classnames.append(studentclasses)

        # save the entries in a dictionary
        self.student_data["student's first name"] = self.first_name
        self.student_data["student's last name"] = self.last_name
        self.student_data["student's class/es"] = self.classnames

        # add the dictionary to a list
        student_list.append(self.student_data)


class teacher:
    def __init__(self,firstname,lastname,subject):
        self.firstname = firstname
        self.lastname = lastname
        self.subject = subject
        # create an empty list to store different class names
        self.classnames = []
        self.teacher_data = {}

        #create a method to take input from user
    def entry_teacher(self):
        self.firstname=input("please enter the first name of the teacher")
        self.lastname=input('please enter the last name of the teacher')
        self.subject=input("please enter the subject the teacher teaches")
        while True:
            classnames=input("please enter the name of classes the teacher teaches")
            if classnames == "":
                break
            self.classnames.append(classnames) #add the class name to the list
        self.teacher_data["teacher's first name"] = self.firstname
        self.teacher_data["teacher's last name"] = self.lastname
        self.teacher_data["teacher's subject"] = self.subject
        self.teacher_data["classes names"] = self.classnames #add the classnames list as a value to this key
        teacher_list.append(self.teacher_data) #add the whole dictionary to the list

class homeroomteacher:
    def __init__(self,firstname,lastname,class_lead):
        self.firstname = firstname
        self.lastname = lastname
        self.class_lead = class_lead
        self.homeroom_data = {}

#create a method to take input from user for the homeroom teacher
    def entry_homeroom(self):
        self.firstname=input("please enter the first name of the teacher")
        self.lastname=input("please enter the last name of the teacher")
        self.class_lead=input("please enter the name of the class the teacher leads")
        self.homeroom_data["homeroom firstname"] = self.firstname
        self.homeroom_data["homeroom last name"] = self.lastname
        self.homeroom_data["class lead"] = self.class_lead
        #add the dictionary to the list

        homeroom_teacher_list.append(self.homeroom_data)

# create a function that searches for the students name entered by the user and prints returns the teacher that teaches the class of the student
def find_contact_by_name(firstname,lastname):
    for student_data in student_list:
        for teacher_data in teacher_list:
            if student_data["student's first name"] == firstname and student_data["student's last name"] == lastname:
              for student_class_name in student_data["student's class/es"]:
                  for teacher_class_name in teacher_data["classes names"]:
                      if student_class_name == teacher_class_name:
                          return f"the name of the teacher of the class {student_class_name} is {teacher_data["teacher's first name"] } { teacher_data["teacher's last name"]}"

#create a function that that takes class name as input from the user and searches for students enrolled in the class
def display_class(class_name):
    Search = False
    for student_data in student_list:
            if class_name in student_data["student's class/es"]:
                print (f"{student_data["student's first name"] } {student_data["student's last name"]} is enrolled in {class_name}")
                Search = True
    if not Search:
        print(f"no students are enrolled in {class_name}")

#a function that takes the first and last name of a teacher from the user and displays the classes the teacher teaches.
def display_teacher_class(first_name,last_name):
        for teacher_data in teacher_list:
            if first_name == teacher_data["teacher's first name"] and last_name == teacher_data["teacher's last name"]:
                print(f"{teacher_data["teacher's first name"] } teaches {teacher_data.get("classes names")}")
            else:
                print("teacher not found in the data base")

# a function that searches for a homeroom teacher and displays the students lead by that teacher.
def display_lead_students(first_name,last_name):
    for homeroom_data in homeroom_teacher_list:
        if homeroom_data["homeroom firstname"] == first_name and homeroom_data["homeroom last name"]:
            for student_data in student_list:
                if homeroom_data["class lead"] in student_data["student's class/es"]:
                    print(f"this home room teacher leads {student_data["student's first name"] } {student_data["student's last name"]} in {homeroom_data["class lead"] } class")
        else:
            print("homeroom teacher not found in the database")


# Loop to take user input and handle commands
while True:
    command = input("\nEnter a command: ")

    # Handle the 'create' command
    if command == 'create':
        print("You selected 'create'. Creating a new resource...")
        user_type=input("please enter the type of user to create\n")
        if user_type == "student":
            s=student(x,y)
            s.entry()
        elif user_type == "teacher":
            t=teacher(x,y,z)
            t.entry_teacher()
        elif user_type == "homeroom teacher":
            h=homeroomteacher(x,y,z)
            h.entry_homeroom()


    # Handle the 'manage' command
    elif command == 'manage':
        print("You selected 'manage'. Managing existing resources...")
        option=input("please choose what option you need to manage : student/ teacher/ homeroom teacher/ class")
        if option == "student":
            first_name_search=input("please enter the first name of the student")
            last_name_search=input("please enter the last name of the student")
            found=find_contact_by_name(first_name_search,last_name_search)
            print(found)
        elif option == "class":
            search_class=input("please enter the name of the class you would like to search for")
            display_class(search_class)
        elif option == "teacher":
            first_name=input("please enter the first name of the teacher")
            last_name=input("please enter the last name of the teacher")
            display_teacher_class(first_name,last_name)
        elif option == "homeroom teacher":
            first_name=input("enter the first name of the homeroom teacher")
            last_name=input("enter the last name of the homeroom teacher")
            display_lead_students(first_name,last_name)

    # Handle the 'end' command
    elif command == 'end':
        print("Exiting the program. Goodbye!")
        break  # Exit the loop and end the program

    # Handle invalid commands
    else:
        print("Invalid command. Please try again.")

