# Inheritance

class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount} into account {self.account_number}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount} from account {self.account_number}. New balance: ${self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"Added ${interest} interest to account {self.account_number}. New balance: ${self.balance}")

class CheckingAccount(BankAccount):
    def __init__(self, account_number, account_holder, overdraft_limit):
        super().__init__(account_number, account_holder)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print("Transaction declined. Insufficient funds")
        else:
            super().withdraw(amount)

# MRO (Method Resolution Order)

class Animal:
    def sound(self):
        print("The animal makes a sound.")

class Mammal(Animal):
    def sound(self):
        print("The mammal makes a sound.")

class Dog(Mammal):
    def sound(self):
        print("The dog barks.")

class Cat(Mammal):
    def sound(self):
        print("The cat meows.")

animals = [Animal(), Mammal(), Dog(), Cat()]
for animal in animals:
    animal.sound()

# Types of Inheritance

# Single Inheritance

class Employee:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name

    def display_details(self):
        print(f"Employee ID: {self.employee_id}, Name: {self.name}")

class Manager(Employee):
    def __init__(self, employee_id, name, department):
        super().__init__(employee_id, name)
        self.department = department

    def display_details(self):
        super().display_details()
        print(f"Department: {self.department}")

# Multiple Inheritance

class Publication:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Book(Publication):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages

class Journal(Publication):
    def __init__(self, title, author, volume):
        super().__init__(title, author)
        self.volume = volume

publications = [Book("Book1", "Author1", 200), Journal("Journal1", "Author2", 10)]
for publication in publications:
    print(f"Title: {publication.title}, Author: {publication.author}")

# Multilevel Inheritance

class University:
    def __init__(self, university_name):
        self.university_name = university_name

class Department(University):
    def __init__(self, department_name, university_name):
        super().__init__(university_name)
        self.department_name = department_name

class Student(Department):
    def __init__(self, student_name, department_name, university_name):
        super().__init__(department_name, university_name)
        self.student_name = student_name

    def display_details(self):
        print(f"University: {self.university_name}, Department: {self.department_name}, Student: {self.student_name}")

# Hierarchical Inheritance

class Vehicle:
    def __init__(self, vehicle_id):
        self.vehicle_id = vehicle_id

class Car(Vehicle):
    def __init__(self, vehicle_id, car_model):
        super().__init__(vehicle_id)
        self.car_model = car_model

class Truck(Vehicle):
    def __init__(self, vehicle_id, truck_model):
        super().__init__(vehicle_id)
        self.truck_model = truck_model

class Motorcycle(Vehicle):
    def __init__(self, vehicle_id, motorcycle_model):
        super().__init__(vehicle_id)
        self.motorcycle_model = motorcycle_model

vehicles = [Car(1, "CarModel1"), Truck(2, "TruckModel1"), Motorcycle(3, "MotorcycleModel1")]
for vehicle in vehicles:
    print(f"Vehicle ID: {vehicle.vehicle_id}")

# Hybrid Inheritance

class Animal:
   def sound(self):