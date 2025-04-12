# OOP Project implementing required concepts

from abc import ABC, abstractmethod

# 1. Vehicle and SchoolBus Classes (Inheritance, Polymorphism, Abstraction)
class Vehicle(ABC):
    def __init__(self, make, model):
        self._make = make
        self._model = model

    @abstractmethod
    def vehicle_type(self):
        pass

    def info(self):
        return f"Vehicle Make: {self._make}, Model: {self._model}"

class SchoolBus(Vehicle):
    def __init__(self, make, model, capacity):
        super().__init__(make, model)
        self.capacity = capacity

    def vehicle_type(self):
        return "School Bus"

    def info(self):
        return f"{super().info()}, Capacity: {self.capacity}"


# 2. Employee Class with Multiple Constructors (Encapsulation, Class Methods)
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    @classmethod
    def from_string(cls, emp_str):
        name, position, salary = emp_str.split(',')
        return cls(name.strip(), position.strip(), float(salary.strip()))

    @classmethod
    def intern(cls, name):
        return cls(name, 'Intern', 0.0)

    def details(self):
        return f"Employee: {self.name}, Position: {self.position}, Salary: ${self.salary}"


# 3. SchoolOne and SchoolTwo Classes (Encapsulation, Abstraction, Polymorphism)
class School:
    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_student(self, name, grades):
        self.students[name] = grades

    def average_grades(self):
        return {name: sum(grades) / len(grades) for name, grades in self.students.items() if grades}

    def gpa(self):
        return {name: round(sum(grades) / len(grades) / 20, 2) for name, grades in self.students.items() if grades}

class SchoolOne(School):
    pass

class SchoolTwo(School):
    pass


# 4. Vector Class with Operator Overloading (Dunder Methods)
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


# 5. Book and Author Classes (Composition)
class Author:
    def __init__(self, name, bio):
        self.name = name
        self.bio = bio

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author  # Composition

    def details(self):
        return f"Book: {self.title}, Author: {self.author.name}"


# Test Code
if __name__ == "__main__":
    # 1. Vehicle instance check
    bus = SchoolBus("Ford", "E450", 40)
    print(bus.info())
    print("Is SchoolBus an instance of Vehicle?", isinstance(bus, Vehicle))

    # 2. Employee multiple constructors
    emp1 = Employee("Alice", "Manager", 5000)
    emp2 = Employee.from_string("Bob, Developer, 4000")
    emp3 = Employee.intern("Ruel")
    print(emp1.details())
    print(emp2.details())
    print(emp3.details())

    # 3. Schools and GPA
    school1 = SchoolOne("CIIT")
    school1.add_student("Aj", [80, 90, 85])
    school1.add_student("Gerry", [70, 75, 80])
    print("SchoolOne Averages:", school1.average_grades())
    print("SchoolOne GPA:", school1.gpa())

    school2 = SchoolTwo("Quezon City High")
    school2.add_student("Jane", [88, 92, 95])
    print("SchoolTwo Averages:", school2.average_grades())
    print("SchoolTwo GPA:", school2.gpa())

    # Edge test: student with no grades
    school2.add_student("NoGrades", [])
    print("SchoolTwo Averages with empty grades:", school2.average_grades())
    print("SchoolTwo GPA with empty grades:", school2.gpa())

    # 4. Vector addition
    v1 = Vector(2, 3)
    v2 = Vector(4, 5)
    v3 = v1 + v2
    print("Vector addition:", v3)

    # Additional test: Adding vector to non-vector
    try:
        print("Invalid Vector addition:", v1 + 10)
    except TypeError as e:
        print("Caught TypeError as expected:", e)

    # 5. Composition example
    author = Author("Bob Ong", "Contemporary Filipino Author")
    book = Book("ABNKKBSNPLAKO?!", author)
    print(book.details())
