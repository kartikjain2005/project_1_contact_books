contacts = []

class Contact:
    def __init__(self , name , contact_no , email):
        self.name = name
        self.contact_no = contact_no
        self.email = email



    def show_all(self):
        print(f"name = {self.name}")
        print(f"contact_no = {self.contact_no}")
        print(f"email = {self.email}")



def showall():
    if not contacts:
        print("There is no contact ")
        return
    for i , contact in enumerate(contacts):
        print(f"\nContact{i+1}")
        contact.show_all()



def add_info():
    name = input("enter the name : ")
    contact_no = int(input("enter the number : "))
    email = input("enter the email : ")
    contacts.append(Contact(name , contact_no , email))
    print("contact successfully")



def deleate_info():
    name = input("enter the name you want to delete : ")
    for contact in contacts:
        if contact.name.lower() == name.lower():
            contacts.remove(contact)
            print("contact deleate sucessfully")
            return
    print("contact not found")



def search_details():
    name = input("enter the name you want to search : ")
    for contact in contacts:
        if contact.name.lower() == name.lower():
            contact.show_all()
            return
    print("name is not available")


while True:
    print("======== CONTACT MANAGER ========")
    print("choice 1 : show all contacts :")
    print("choice 2 : add the contact details :")
    print("choice 3 : delete the contact details : ")
    print("choice 4 : search contact : ")
    print("choice 5 : exit : ")


    user = int(input("select your choice : "))
    if(user == 1):
        showall()
    elif(user ==2 ):
        add_info()
    elif(user == 3):
        deleate_info()
    elif(user == 4):
        search_details()
    elif(user == 5):
        print("you sucessfully Exited ...... thankyou ")
        break
    else:
     print("Invalid number choose 1-5")
