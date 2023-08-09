import sys
import os
from python.databases.SQLalchemy.todo.todo_database import Item, Session, User, UserItem

def main():
    print(f"{os.linesep}Register new account or login!")
    print("1: Register a new account")
    print("2: Login to an already existing account")
    selection1 = input()
    if selection1 == "1": 
        registeration() 
        return None


    if selection1 == "2": 
        current_access = login()
        if current_access == "access denied":
            return None
            
        else:
            print("You have logged in as:")
            print(current_access)


    while True:
        print(f"{os.linesep}What do you want to do today?")
        print("1: View todo items")
        print("2: Create new todo item")
        print("3: Remove todo item")
        print("4: Exit" + os.linesep)

        selection2 = input()
        if selection2 == "1": showItems(current_access) 
        if selection2 == "2": createItem(current_access)
        if selection2 == "3": removeItem(current_access)
        if selection2 == "4": sys.exit("Goodbye!")


def registeration():
    print("Choose a username:")
    userName = input()

    with Session() as session:
        user = session.query(User).filter(User.username == userName).first()
        if user is None:
            print("The username was available :)")

        else:
            print("This username has been taken, try again")
            return
        
    print("Choose a password:")
    password = input()

    with Session() as session:
        newUser = User(username = userName, password = password)
        session.add(newUser)
        session.commit()
    
    print("Your user has been added to the system!")


def login():
    print("Enter your username:")
    userName = input()

    print("Enter your password:")
    password = input()

    with Session() as session:
        user = session.query(User).filter(User.username == userName, User.password == password).first()
        if user is None:
            print("Username or password is wrong!")
            return("access denied")
                
        else:
            print("Succesfully logged in!")
            return(user.username)

def showItems(current_access):
    print("your todo lists:")
    print("---")
    with Session() as session:
        the_user = session.query(User).filter( User.username == current_access).first()
        items = session.query(Item)
        for item in the_user.items:
            itemId = item.itemId
            itemName = item.name
            itemDesc = item.description
            itemTime = item.time
            print(f"{itemId}: {itemName} - {itemDesc} - created: {itemTime}")
        print("---" + os.linesep)


def createItem(current_access):
    print("Name of the item:")
    itemName = input()

    print("Description of item:")
    itemDesc = input()
    with Session() as session:
        the_user = session.query(User).filter( User.username == current_access).first()
        newItem = Item(name = itemName, description = itemDesc)
        session.add(newItem)
        the_user.items.append(newItem)
        session.commit()

def removeItem(current_access):
    with Session() as session: 
        the_user = session.query(User).filter( User.username == current_access).first()
        itemAmount = len(the_user.items)
        
        if itemAmount < 1:
            print("You should add some items first.")
            return
        
        print("Give ID to remove:")
        itemId = int(input())

        removableItem = session.query(Item).filter(Item.itemId == itemId)
        if (removableItem.count() > 0):
            session.delete(removableItem.one())
            session.commit()
        else:
            print("Invalid ID!")

print("Welcome to TOD-O LIST O-MAKER Version 5123.524")
main()