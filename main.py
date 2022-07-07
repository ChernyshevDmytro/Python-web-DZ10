from datetime import datetime
from pymongo import MongoClient
import connect
from models import Person


#client = MongoClient(f"{connect.connect}")
#db = client[ f"{connect.db_name}" ]
#col = db[ "testcol" ]
#result_one = col.insert_one({"name": "aaa"})

#print(result_one.inserted_id)

COMMANDS_LIST = ["hello", "exit", "close", "good bye", "show_all", "phone", "add", "add_phone",
                 "del_phone", "edit_phone", "del_contact", "add_birthday", "find"]

def handling(user_command_normalized):
    if "add" == str(user_command_normalized[0]):
        person = Person.objects(name=f"{user_command_normalized[1]}")
        if not person:
            person = Person(name=f"{user_command_normalized[1]}").save()
            print(f'Person {user_command_normalized[1]} added')
        else:
            print(f"Contact name {user_command_normalized[1]} exists. Please use another name")

    elif "add_phone" == str(user_command_normalized[0]):
        person = Person.objects(name=f"{user_command_normalized[1]}")

        if person:    
            person = Person.objects.get(name=f"{user_command_normalized[1]}")
            person.phones.append( f"{user_command_normalized[2]}")
            person.save()
        
        elif not person:
            person = Person(name=f"{user_command_normalized[1]}", phones= [f"{user_command_normalized[2]}", ]).save()
            print(f'Person {user_command_normalized[1]} added') 
        
    elif "phone" == str(user_command_normalized[0]):
        person = Person.objects(name=f"{user_command_normalized[1]}")
        if person:    
            person = Person.objects.get(name=f"{user_command_normalized[1]}")
            print(person.phones)     

    elif "add_birthday" == str(user_command_normalized[0]):
        raw_birtday = f"{user_command_normalized[2]}"
        dt_birthday = datetime(year=int(raw_birtday[0:4]), month=int(raw_birtday[4:6]), day=int(raw_birtday[6:]))
        person = Person.objects(name=f"{user_command_normalized[1]}")

        if person:    
            person = Person.objects.get(name=f"{user_command_normalized[1]}")
            person.birthday = dt_birthday
            person.save()
            print(f'Person {user_command_normalized[1]} added birthday {dt_birthday}')        
        elif not person:
            person = Person(name=f"{user_command_normalized[1]}", birthday= dt_birthday).save()
            print(f'Person {user_command_normalized[1]} added')         


    elif "edit_phone" == str(user_command_normalized[0]):        
        person = Person.objects(name=f"{user_command_normalized[1]}")

        if person:    
            person = Person.objects.get(name=f"{user_command_normalized[1]}")
            for ind, phone in enumerate(person.phones):
                if phone == f"{user_command_normalized[2]}":
                    person.phones[ind] = f"{user_command_normalized[3]}"            
                person.save()        
        else:
            print ("Person or phone does not exist")

    elif "del_phone" == str(user_command_normalized[0]):        
        person = Person.objects(name=f"{user_command_normalized[1]}")

        if person:    
            person = Person.objects.get(name=f"{user_command_normalized[1]}")
            for ind, phone in enumerate(person.phones):
                if phone == f"{user_command_normalized[2]}":
                    person.phones.pop(ind)            
                person.save()        
        else:
            print ("Person or phone does not exist")                                            

    elif "del_contact" == str(user_command_normalized[0]):        
        person = Person.objects(name=f"{user_command_normalized[1]}")

        if person:    
            person = Person.objects.get(name=f"{user_command_normalized[1]}")
            person.delete()

    elif "find" == str(user_command_normalized[0]):       
        person_name = Person.objects.get(name=f"{user_command_normalized[1]}")
        if person_name:    
            if person_name.birthday != None:
                print(f"{person_name.name}, {person_name.phones}, {person_name.birthday}")
            else:
                print(f"{person_name.name}, {person_name.phones}")


    elif "show_all" == str(user_command_normalized[0]):      
        for person in Person.objects.all():         
            if person.birthday == None:
                print(f"{person.name}:{person.phones}") 
            else:
                print(f"{person.name}:{person.phones} DB{person.birthday}")                                      

def input_():
    while True:
        raw_user_command = input("Please, give me a command:")
        raw_user_command = raw_user_command.split(" ")        
        if raw_user_command[0] in COMMANDS_LIST:  
            return raw_user_command
        continue

while True:
    raw_user_command = input_()
    if raw_user_command[0] in ["close", "good bye", "exit"]:
        print("By")    
        break
    elif raw_user_command[0] == "hello":
        print(f"I know follow coomands{COMMANDS_LIST}")

    a= handling(raw_user_command) 
    try:
        a() 
    except   TypeError:
        pass                        