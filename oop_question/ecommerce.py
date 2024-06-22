from abc import ABC, abstractmethod

#Using lists in place of a database to keep track of objects
vendor_list = list()
user_list = list()

#Abstract User class with the base methods
#The normal user, store manager, and admin class will implement these abstract methods
class User():
    @abstractmethod
    def view_items(vendor):
        pass
    @abstractmethod
    def buy_items(vendor):
        pass
    @abstractmethod
    def view_vendor_items(self, vendor):
        pass
    @abstractmethod
    def view_individual_item(self):
        pass


#Normal User class which can view and buy items
#Store manager and admin will inherit from this base class
class normal_user(User):
    def __init__(self, name, address, password):
        self.name = name
        self.address = address
        self.items_ordered = list()
        self.password = password
        user_list.append(self)

    #View all items
    def view_items(self):
        print("Following items are offered by the all vendors: ")
        for vendor in vendor_list:
            print(str(vendor.name) + ": " +  str(vendor.items))
    
    #View item according to vendor
    def view_vendor_items(self, vendor):
        print("Following items are offered by vendor: " + str(vendor.name))
        print(vendor.items)

    #View item by item name/id
    def view_individual_item(self, item_id):
        for vendor in vendor_list:
            for item in vendor.items:
                if item[0] == item_id:
                    print(f"{vendor.name} offers {item[0]}")

    #Buy item for the user and reduce the quantity of the items that have been bought
    def buy_item(self, vendor):
        print("Following items are offered by vendor: " + str(vendor.name))
        print(vendor.items)
        i = input("Enter number of the item you want to buy:")
        print("Item bought!")
        self.items_ordered.append(vendor)
        vendor.items[i][1] -= 1


#Store manager class inherits from the User class
#Admin class will inherit fromt this store manager class
class Store_manager(normal_user):
    def add_vendor_items(self, v):
        item = input("Enter name of item to add to this vendor, and the quantity in the form of a list: ")
        v.items.append(item)
        return v.items

#Admin class, which inherits from Store_manager class and has highest privileges
class Admin(Store_manager):

    #Creates new vendors based on the received details
    def create_vendor(self):
        name = input("Input vendor name: ")
        location = input("Input vendor location: ")
        items = input("Input vendor items: ")
        return Vendor(name, location, items)

    #Creates new users based on the received details
    def create_user(self):
        name = input("Input user name: ")
        location = input("Input user location: ")
        password = input("Input user password: ")
        return normal_user(name, location, password)

#Vendor class which holds all vendor attributes and items
class Vendor:

    #allows having many items from many different vendors
    def __init__(self, name, location, items):
        self.name = name
        self.location = location
        self.items = items
        vendor_list.append(self)

#Log in the user from the username and password
class Login:
    def login_user(self, username, password):
        for user in user_list:
            if user.name == username and user.password == password:
                print(f"You have been logged in as {user.name}")
                return user


#Driver code to run the OOD program
            
#Creating vendors, admin, and store managers
v0 = Vendor("Danish", "NUST", [["Item1", 50], ["Item2", 40], ["Item3", 30], ["Item4", 20]])
#v0.add_items(["Item5", 10])
v2 = Vendor("Humza", "216", [["Item1", 50], ["Item2", 40]])
admin = Admin("Affan", "120", 123)
v1 = admin.create_vendor()
admin.view_vendor_items(v1)
manager = Store_manager("Zaid", "DS", "654")
u1 = admin.add_vendor_items(v2)
print(u1)
print(user_list)
print(vendor_list)
login = Login()
name = input("Enter username: ")
password = input("Enter password: ")
this_user = login.login_user(name, password)
this_user.view_vendor_items(v2)

