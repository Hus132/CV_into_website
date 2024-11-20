
alldata_list=[]
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
        self.student_data = {} #create a new dictionary for every object created
        self.classnames=[]    #create an empty list to store class names

        #A method to take input from the user.
    def entry(self):
        self.first_name=input("please enter the first name of the student")
        self.last_name = input("please enter the last name of the student")
        while True:
            student_classes=input("please enter the class/es the student attends")
            if student_classes == "":
                break
            self.classnames.append(student_classes)  #save the classes into the list

        # save the entries in a dictionary
        self.student_data["student's first name"] = self.first_name
        self.student_data["student's last name"] = self.last_name
        self.student_data["student's class/es"] = self.classnames #add the list as  a key value into the dictionary

        # add the dictionary to the list of all values
        alldata_list.append(self.student_data)

        # A method to search for the student's first and last name i the list.
    def find_student_by_name(self,firstname,lastname):
        #looking for the dictionary of the student inside the list.
        for student_data in alldata_list:
            if student_data["student's first name"] == firstname and student_data["student's last name"] == lastname:
                return student_data["student's class/es"]



class teacher:
    def __init__(self,firstname,lastname,subject):
        self.firstname = firstname
        self.lastname = lastname
        self.subject = subject
        # create an empty list to store different class names
        self.classnames = []

        #create a method to take input from user
    def entry_teacher(self):
        self.firstname=input("please enter the first name of the teacher")
        self.lastname=input('please enter the last name of the teacher')
        self.subject=input("please enter the subject the teacher teaches")

        #create a dictionary for every object of the class
        teacher_data = {}
        while True:
            classnames=input("please enter the name of classes the teacher teaches")
            if classnames == "":
                break
            self.classnames.append(classnames) #add the class name to the list
        teacher_data["teacher's first name"] = self.firstname
        teacher_data["teacher's last name"] = self.lastname
        teacher_data["teacher's subject"] = self.subject
        teacher_data["classes names"] = self.classnames #add the classnames list as a value to this key
        alldata_list.append(teacher_data) #add the whole dictionary to the list

class homeroomteacher:
    def __init__(self):
        self.firstname=input("please enter the first name of the teacher")
        self.lastname=input("please enter the last name of the teacher")
        self.class_lead=input("please enter the name of the clas the teacher leads")
        homeroom = {}
        homeroom["HR teacher's first name"]=self.firstname
        homeroom["HR teacher's last name"]=self.lastname
        homeroom["HR class name"]=self.class_lead
        alldata_list.append(homeroom)

# class manage:
#     def __init__(self):
#
#     def find_student_by_name (self, firstname, lastname):
#             # looking for the dictionary of the student inside the list.
#         for student_data in alldata_list:
#             if student_data["student's first name"] == firstname and student_data[
#                     "student's last name"] == lastname:
#                  v= student_data["student's class/es"]
#                  return v
#         for teacher_data in alldata_list:
#             if teacher_data["classes names"] == student_data["student's class/es"]:
#                 return teacher_data["classes names"]

# Loop to take user input and handle commands
while True:
    command = input("\nEnter a command: ")

    # Handle the 'create' command
    if command == 'create':
        print("You selected 'create'. Creating a new resource...")
        user_type=input("please enter the type of user to create\n")
        if user_type == "student":
            s=student(x,y) #create an object of the class student in case the type is student
            s.entry() #calling the entry function
        elif user_type == "teacher":
            t=teacher(x,y,z) #create an object of teacher class
            t.entry_teacher() #call method to take input from user


    # Handle the 'manage' command
    elif command == 'manage':
        print("You selected 'manage'. Managing existing resources...")
        option=input("please choose what option you need to manage : student/ teacher/ homeroom teacher/ class")
        if option == "student":
            first_name_search=input("please enter the first name of the student")
            last_name_search=input("please enter the last name of the student")
            s=student(x,y)
            found_student=s.find_student_by_name(first_name_search,last_name_search)
            print(f"The student attends the following classes: {found_student}")

    # Handle the 'end' command
    elif command == 'end':
        print("Exiting the program. Goodbye!")
        break  # Exit the loop and end the program

    # Handle invalid commands
    else:
        print("Invalid command. Please try again.")

print(alldata_list)


#use a list instead of a dictionary since dictionaries do not accept dupliacates.