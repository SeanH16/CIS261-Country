#Sean Holbrook
#CIS261
#Country


#create a command list menu function and call it

def menu():
    print("COMMAND MENU")
    print("view - View country name")
    print("add -  Add a country")
    print("del -  Delete a country")
    print("exit - Exit program")

menu()


#create a function that will prepopulate dictionary with country key and name

def my_country_dict():
    country_dict = {'FR':'France',
                    'US':'United States',
                    'MX':'Mexico'}
    return country_dict

country_dict = my_country_dict()

#create a function to display the dictionary codes

def display_dict(country_dict):
    codes = ""
    for key in country_dict:
        codes = codes + " " + key
    print(f"Country Codes:{codes}")
    country_input = str(input("Enter Country Code: "))
    if country_input in country_dict:
        print(f"Country name: {country_dict[country_input]}")
    else:
        print("Invalid Country Code")



#create function to add a code and country to the dictionary

def add_to_dict(country_dict):
    country_code = input("Enter country code: ")
    if country_code in country_dict:
        print(f"{country_dict[country_code]} is already using this code.")
    else:
        country_name = input("Enter country name: ")
        country_dict[country_code] = country_name
        print(f"{country_dict[country_code]} was added.")


#create function to delete a code and country from dictionary

def del_from_dict(country_dict):
    del_code = input("Enter country code to delete: ")
    if del_code not in country_dict:
        print("Invalid country code")
    else:
        print(f"{country_dict[del_code]} was deleted.")
        del country_dict[del_code]
        

#choice menu

command = str(input("Command: "))

while command.lower() != "exit":
    if command.lower() == "view":
        display_dict(country_dict)
        command = str(input("Command: "))
    elif command.lower() == "add":
        add_to_dict(country_dict)
        command = str(input("Command: "))
    elif command.lower() == "del":
        del_from_dict(country_dict)
        command = str(input("Command: "))
    elif command.lower() == "exit":
        break
    else:
        print("Invalid command, try again please.")
        command = str(input("Command: "))

print("Bye!")
