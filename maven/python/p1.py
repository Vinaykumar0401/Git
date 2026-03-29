'''"""
Python Program: Lambda Functions and Filter Function
========================================================
This program demonstrates and explains lambda functions and filter functions
in Python, which are functional programming concepts.
"""

# =====================================================
# 1. LAMBDA FUNCTIONS
# =====================================================
print("=" * 60)
print("1. LAMBDA FUNCTIONS")
print("=" * 60)

# A lambda function is a small anonymous function
# Syntax: lambda arguments: expression

print("\n--- Example 1: Basic Lambda Function ---")
# Regular function
def add(x, y):
    return x + y

# Equivalent lambda function
add_lambda = lambda x, y: x + y

print(f"Regular function add(5, 3) = {add(5, 3)}")
print(f"Lambda function add_lambda(5, 3) = {add_lambda(5, 3)}")

print("\n--- Example 2: Lambda with Single Argument ---")
square = lambda x: x ** 2
numbers = [1, 2, 3, 4, 5]
print(f"Numbers: {numbers}")
print(f"Squares: {[square(n) for n in numbers]}")

print("\n--- Example 3: Lambda used with map() ---")
# map() applies a function to each item in an iterable
prices = [10, 20, 30, 40]
discount_rate = 0.1
discounted_prices = list(map(lambda price: price * (1 - discount_rate), prices))
print(f"Original prices: {prices}")
print(f"Discounted prices (10% off): {discounted_prices}")

print("\n--- Example 4: Lambda with sorted() ---")
students = [
    {"name": "John", "score": 85},
    {"name": "Alice", "score": 92},
    {"name": "Bob", "score": 78}
]
sorted_students = sorted(students, key=lambda student: student["score"], reverse=True)
print("Students sorted by score (highest to lowest):")
for student in sorted_students:
    print(f"  {student['name']}: {student['score']}")

# =====================================================
# 2. FILTER FUNCTION
# =====================================================
print("\n" + "=" * 60)
print("2. FILTER FUNCTION")
print("=" * 60)

# filter() returns items from an iterable for which a function returns True
# Syntax: filter(function, iterable)

print("\n--- Example 1: Filter Even Numbers ---")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Original numbers: {numbers}")
print(f"Even numbers: {even_numbers}")

print("\n--- Example 2: Filter Numbers Greater Than 5 ---")
numbers = [2, 8, 1, 9, 3, 7, 4, 6, 5]
filtered = list(filter(lambda x: x > 5, numbers))
print(f"Original numbers: {numbers}")
print(f"Numbers > 5: {filtered}")

print("\n--- Example 3: Filter Strings by Length ---")
words = ["apple", "pie", "banana", "cat", "elephant", "dog"]
long_words = list(filter(lambda word: len(word) > 4, words))
print(f"Original words: {words}")
print(f"Words with length > 4: {long_words}")

print("\n--- Example 4: Filter with Custom Function ---")
def is_positive(num):
    return num > 0

numbers = [-5, 3, -2, 8, -1, 4, 0, 6]
positive_numbers = list(filter(is_positive, numbers))
print(f"Original numbers: {numbers}")
print(f"Positive numbers: {positive_numbers}")

print("\n--- Example 5: Filter Objects (Real-World Scenario) ---")
employees = [
    {"name": "John", "salary": 50000, "department": "IT"},
    {"name": "Alice", "salary": 75000, "department": "HR"},
    {"name": "Bob", "salary": 45000, "department": "IT"},
    {"name": "Carol", "salary": 85000, "department": "Finance"},
    {"name": "Dave", "salary": 55000, "department": "IT"}
]

high_earners = list(filter(lambda emp: emp["salary"] > 60000, employees))
print("High earners (salary > 60000):")
for emp in high_earners:
    print(f"  {emp['name']}: ${emp['salary']} ({emp['department']})")

it_employees = list(filter(lambda emp: emp["department"] == "IT", employees))
print("\nIT Department Employees:")
for emp in it_employees:
    print(f"  {emp['name']}: ${emp['salary']}")

# =====================================================
# 3. COMBINING LAMBDA AND FILTER
# =====================================================
print("\n" + "=" * 60)
print("3. COMBINING LAMBDA AND FILTER")
print("=" * 60)

print("\n--- Example: Filter with Complex Logic ---")
scores = [45, 75, 82, 38, 91, 67, 55, 88, 49, 78]
print(f"All scores: {scores}")

# Filter scores within a grade range (70-85)
in_range = list(filter(lambda score: 70 <= score <= 85, scores))
print(f"Scores between 70-85: {in_range}")

# Filter scores that are passing (>= 50)
passing = list(filter(lambda score: score >= 50, scores))
print(f"Passing scores (>= 50): {passing}")

# =====================================================
# 4. KEY DIFFERENCES AND USE CASES
# =====================================================
print("\n" + "=" * 60)
print("4. KEY DIFFERENCES AND USE CASES")
print("=" * 60)

print("""
LAMBDA FUNCTIONS:
- Anonymous, small, one-liner functions
- Used for simple operations
- Best used with map(), sorted(), filter(), etc.
- Cannot contain multiple statements
- Useful for callbacks

FILTER FUNCTION:
- Filters items from an iterable
- Returns an iterator of items that satisfy a condition
- Requires a function (often lambda) and an iterable
- Returns True/False for each item
- Useful for cleaning and selecting data

USE CASES:
1. Lambda: Quick transformations, sorting keys, one-off functions
2. Filter: Removing invalid data, selecting specific items, data validation
3. Combined: Extract and transform data in a single operation
""")
'''
# =====================================================
# 5. OBJECT-ORIENTED PROGRAMMING (OOP) CONCEPTS
# =====================================================
print("\n" + "=" * 60)
print("5. OBJECT-ORIENTED PROGRAMMING (OOP) CONCEPTS")
print("=" * 60)

print("""
OOP is a programming paradigm based on objects and classes.
Four main pillars of OOP:
1. Encapsulation - bundling data and methods together
2. Inheritance - deriving new classes from existing ones
3. Polymorphism - objects can take multiple forms
4. Abstraction - hiding internal implementation details
""")

# =====================================================
# 5.1 CLASSES AND OBJECTS
# =====================================================
print("\n" + "=" * 60)
print("5.1 CLASSES AND OBJECTS")
print("=" * 60)

print("\n--- Example 1: Basic Class Definition ---")

class Car:
    """A simple Car class to demonstrate OOP concepts"""
    
    # Class attribute (shared by all instances)
    total_cars = 0
    
    # Constructor method
    def __init__(self, brand, model, year):
        # Instance attributes (unique to each object)
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0
        Car.total_cars += 1
    
    # Instance methods
    def accelerate(self, amount):
        self.speed += amount
        print(f"{self.brand} {self.model} accelerated. Speed: {self.speed} km/h")
    
    def brake(self):
        self.speed = 0
        print(f"{self.brand} {self.model} stopped.")
    
    def display_info(self):
        print(f"Car: {self.year} {self.brand} {self.model}")
    
    # Special method
    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"

# Creating objects (instances of the class)
car1 = Car("Toyota", "Camry", 2023)
car2 = Car("Honda", "Civic", 2024)

print(f"Car 1: {car1}")
print(f"Car 2: {car2}")
car1.accelerate(50)
car1.brake()
print(f"Total cars created: {Car.total_cars}")

# =====================================================
# 5.2 ENCAPSULATION
# =====================================================
print("\n" + "=" * 60)
print("5.2 ENCAPSULATION (Data Hiding)")
print("=" * 60)

print("\n--- Example: Private and Public Attributes ---")

class BankAccount:
    """Bank Account with encapsulation"""
    
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder  # Public
        self.__balance = initial_balance  # Private (double underscore)
        self._account_number = "ACC12345"  # Protected (single underscore)
    
    def deposit(self, amount):
        """Public method to deposit money"""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive")
    
    def withdraw(self, amount):
        """Public method to withdraw money"""
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: ${amount}. Remaining balance: ${self.__balance}")
        else:
            print("Invalid withdrawal amount")
    
    def get_balance(self):
        """Public method to check balance (read-only)"""
        return self.__balance
    
    def __calculate_interest(self):
        """Private method (cannot be accessed directly from outside)"""
        return self.__balance * 0.05

account = BankAccount("John Doe", 1000)
account.deposit(500)
account.withdraw(200)
print(f"Current balance: ${account.get_balance()}")
print(f"Account holder: {account.account_holder}")

# =====================================================
# 5.3 INHERITANCE
# =====================================================
print("\n" + "=" * 60)
print("5.3 INHERITANCE (Code Reusability)")
print("=" * 60)

print("\n--- Example: Parent and Child Classes ---")

class Animal:
    """Parent class"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def make_sound(self):
        return "Some generic animal sound"
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Dog(Animal):
    """Child class inheriting from Animal"""
    
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # Call parent constructor
        self.breed = breed
    
    def make_sound(self):  # Override parent method
        return "Woof! Woof!"
    
    def display_info(self):
        super().display_info()
        print(f"Breed: {self.breed}")

class Cat(Animal):
    """Another child class"""
    
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    
    def make_sound(self):
        return "Meow! Meow!"

dog = Dog("Buddy", 5, "Golden Retriever")
cat = Cat("Whiskers", 3, "Orange")

print("\nDog Info:")
dog.display_info()
print(f"Sound: {dog.make_sound()}")

print("\nCat Info:")
cat.display_info()
print(f"Sound: {cat.make_sound()}")

# =====================================================
# 5.4 POLYMORPHISM
# =====================================================
print("\n" + "=" * 60)
print("5.4 POLYMORPHISM (Many Forms)")
print("=" * 60)

print("\n--- Example: Same method, different behavior ---")

class Shape:
    """Base class for shapes"""
    
    def area(self):
        pass
    
    def display(self):
        print(f"Area: {self.area()}")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

# Polymorphism in action
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 7)
]

print("Using polymorphism - same method call, different results:")
for shape in shapes:
    shape.display()

# =====================================================
# 5.5 ABSTRACTION
# =====================================================
print("\n" + "=" * 60)
print("5.5 ABSTRACTION (Hiding Complexity)")
print("=" * 60)

print("\n--- Example: Abstract Base Class ---")

from abc import ABC, abstractmethod

class Vehicle(ABC):
    """Abstract base class"""
    
    def __init__(self, brand):
        self.brand = brand
    
    @abstractmethod
    def start(self):
        """This method must be implemented by child classes"""
        pass
    
    @abstractmethod
    def stop(self):
        """This method must be implemented by child classes"""
        pass
    
    def display_brand(self):
        print(f"Brand: {self.brand}")

class Car(Vehicle):
    """Concrete implementation of Vehicle"""
    
    def start(self):
        print(f"{self.brand} Car is starting...")
        print("Engine started with key")
    
    def stop(self):
        print(f"{self.brand} Car is stopping...")
        print("Engine turned off")

class Bike(Vehicle):
    """Another concrete implementation"""
    
    def start(self):
        print(f"{self.brand} Bike is starting...")
        print("Kick-started")
    
    def stop(self):
        print(f"{self.brand} Bike is stopping...")
        print("Engine cut off")

# You cannot instantiate abstract class directly
# vehicle = Vehicle("Generic")  # This would raise an error

car = Car("Toyota")
bike = Bike("Harley-Davidson")

print("\nCar Operations:")
car.display_brand()
car.start()
car.stop()

print("\nBike Operations:")
bike.display_brand()
bike.start()
bike.stop()

# =====================================================
# 5.6 OOP PRINCIPLES SUMMARY
# =====================================================
print("\n" + "=" * 60)
print("5.6 OOP PRINCIPLES SUMMARY")
print("=" * 60)

print("""
ENCAPSULATION:
- Bundles data and methods together in a class
- Protect data using private attributes (__attribute)
- Use getters/setters for controlled access
- Example: BankAccount with private balance

INHERITANCE:
- Child classes inherit properties and methods from parent class
- Use super() to access parent class methods
- Promotes code reusability and creates hierarchies
- Example: Dog, Cat inherit from Animal

POLYMORPHISM:
- Same method name, different implementations
- Achieved through method overriding
- Allows treating different objects uniformly
- Example: Different shapes with same area() method

ABSTRACTION:
- Hides internal implementation complexity
- Shows only essential features
- Use abstract base classes (ABC)
- Forces child classes to implement specific methods
- Example: Vehicle abstract class with Car and Bike
""")

print("\n" + "=" * 60)
print("Program Complete!")
print("=" * 60)
