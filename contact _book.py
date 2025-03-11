import json
con = []
with open("data.json","w") as file:
    pass
def add_contact():
    global con
    name = input("Give the name of the person: ")
    email = input("Give the email of the person: ")
    phone = input("Give the phone of the person: ")
    with open("data.json","r") as file:
        try:
            data = json.load(file)
        except(FileNotFoundError, json.JSONDecodeError):
        
            contact = {"name":name,
                    "email":email,
                    "phone":phone}
        else:
            contact = {"name":name,
                    "email":email,
                    "phone":phone}
        
    con.append(contact)
    with open("data.json","w") as file:
        json.dump(con, file, indent=4)
def view_contacts():
    with open("data.json","r") as file:
        data = json.load(file)
    print(data)
def search_contact():
    global con
    name = input("Enter Name to Search: ").lower()
    found = [ n for n in con if n["name"].lower()==name]
    if len(found)==0:
        print("Contact not found")
    else:
        print(f"person name: {found[0]["name"]}, email: {found[0]["email"]}, phone: {found[0]["phone"]}")

def delete_contact():
    global con
    name = input("Enter Name to delete: ").lower()

    for i in range(len(con) - 1, -1, -1): 
        if con[i]["name"].lower() == name:
            del con[i]
            print(" Contact deleted successfully!")
            with open("data.json","w") as file:
                json.dump(con,file)
            return  
    print(" Contact not found!")  
while True:
    print("\n📖 Contact Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    
    choice = input("Choose an option: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("🔚 Exiting... Contacts Saved!")
        break
    else:
        print("❌ Invalid choice! Please select again.")