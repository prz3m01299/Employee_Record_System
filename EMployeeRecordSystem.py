run='N'
#This is a variable that will look the program

def add_record():
        UID=input("Please type employee's id: ")
        FirstName=input("Employee's name: ")
        SurName=input("Employee's surname: ")
        StartDate=input("Employee's start date: ")
        Position=input("Employee's position: ")
        Department=input("Employee's department: ")
        Salary=input("Employee's basic salary: ")
        ContactNumber=input("Employee's contact number: ")
        EmailAddress=input("Employee's email address: ")

        record[UID]=UID, FirstName, SurName, StartDate, Position, Department, Salary, ContactNumber, EmailAddress
        print ('\nEmployee added successfully.')
        return record[UID]
#defining a function that will add a new record into the system, by adding every element of employee's information into the dictionary

UID=[]
FirstName=[]
SurName=[]
StartDate=[]
Position=[]
Department=[]
Salary=[]
ContactNumber=[]
EmailAddress=[]
#creating lists that will hold employees' data

record=dict(zip(UID,FirstName,SurName,StartDate,Position,Department,Salary,ContactNumber,EmailAddress))
#here we created a dictionary by integrating the lists created above

print('Welcome!')
import datetime

current_time = datetime.datetime.now()

print('\nCurrent time and date: ',current_time.strftime('%H:%M')+', '+current_time.strftime('%d-%m-%Y'))
#welcome message like in Windows operating system

while run!="t" or run!="T":
    
    menu_select=input("\nPlease select a menu option and press enter:\n\n1.Add Record\n2.Modify\n3.List\n4.Search\n5.Delete\n6.Exit\n")

    if menu_select=="1" or menu_select=="add record":
        
        add_record()

    elif menu_select=='2' or menu_select=='modify':
        modify=input("\nWhich employee's record do you wish to modify? Please type the ID: ")
        if modify in record.keys():
            del record[modify]
            add_record()
        else:
            print("\nEmployee doesn't exist in the system.")

#to modify a record, the program deletes the record from user's input and allows to provide the changes once again


    elif menu_select == '3' or menu_select == 'list':
        print("\nCurrent list of employees:")
        print("{:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<20} {:<25}".format("UID", "First Name", "Surname", "Start Date", "Position", "Department", "Salary", "Contact Number", "Email Address"))
        for key, value in record.items():
            print("{:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<20} {:<25}".format(key, value[1], value[2], value[3], value[4], value[5], value[6], value[7], value[8]))
#prints the message 'current list of employees' and the stored employee records withing the dictionary 'record'
   

    elif menu_select=='4' or menu_select=='search':
        search=input("\nPlease enter Id of the employee you are searching for: ")
        if search in record.keys():
                print('\nThe employee with ID:',search,'exists in the system.')
                print(record[search])
        else:
                print("\nCouldn't find employee with this ID.")

# this function searches for the employee that user has provide ID of, in case it wasn't found, an error message is displayed

    elif menu_select=='5' or menu_select=='delete':
            delete=input("Which employee's record do you want to delete?: ")
            if delete in record.keys():
                del record[delete]
                print('\nEmployee deleted successfully.')
            else:
                print("\nThis employee doesn't exist in the system.")
#this function first check if the ID exists in the system and then deletes it, otherwise displays a message that the employee doesn't exist                                 

    elif menu_select=='6' or menu_select=='exit':
        run=input('Are you sure you want to exit the program? Y/N: ')
        if run=='Y' or run=='y':
            print('\nSee you soon!')
            break
        else:
            run='N'
# this elif statement asks if user wants to quit the program

    else:
        print('Please choose menu options from 1 to 6 only!')
        run='N'
        
#this else statement is for when the user types something else than numbers from 1 to 6
        
