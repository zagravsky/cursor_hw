

class Developer(object):
    years_experience = 0
    name = ""
    language = ""

    def __init__(self, years_experience, name):
        self.years_experience = years_experience
        self.name = name
        self.language = ""

    def __str__(self):
        return f"{self.name} - {self.years_experience} years, {self.language}"

    def __call__(self, *args, **kwargs):
        self.write_code()

    def about(self):
        if self.years_experience <= 3:
            print(f"My name is {self.name} and I am a Junior Developer.")
        elif self.years_experience <= 5:
            print(f"My name is {self.name} and I am a Middle Developer.")
        else:
            print(f"My name is {self.name} and I am a Senior Developer.")

    def write_code(self):
        print("I am a developer and I write code")


class PythonDeveloper(Developer):
    def __init__(self, years_experience, name):
        Developer.__init__(self, years_experience, name)
        self.language = "Python"

    def write_code(self):
        print(f"I use {self.language} to write code")


class JavaDeveloper(Developer):
    def __init__(self, years_experience, name):
        Developer.__init__(self, years_experience, name)
        self.language = "Java"

    def write_code(self):
        print(f"I use {self.language} to write code")


class RubyDeveloper(Developer):
    def __init__(self, years_experience, name):
        Developer.__init__(self, years_experience, name)
        self.language = "Ruby"

    def write_code(self):
        print(f"I use {self.language} to write code")


class A:
    pass

class B:
    pass

class C(B, A):
    pass

class D(C, A):
    pass

class E(D, B):
    pass


class ItCompany:
    employees = []

    def add_employee(self, dev):
        self.employees.append(dev)

    def list_employees(self):
        for e in sorted(self.employees, key=lambda x: x.years_experience, reverse=True):
            print(e)

    def fire_employee(self, name):
        for e in self.employees:
            if e.name == name:
                self.employees.remove(e)
                print(f"Successfully fired:{name}")
                return 1
        print("Employee not found")
        return 0

    def hire_employee(self, dev):
        if dev.years_experience > 3:
            self.add_employee(dev)
            print(f"Successfully hired:{dev}")
            return 1
        else:
            print("Not enough experience")
            return 0


if __name__ == "__main__":
    p_dev = PythonDeveloper(5, "John")
    j_dev = JavaDeveloper(15, "Mark")
    r_dev = RubyDeveloper(1, "Kate")

    # Task 1
    print("Task #1")
    p_dev.about()
    p_dev.write_code()

    j_dev.about()
    j_dev.write_code()

    r_dev.about()
    r_dev.write_code()

    print(p_dev)

    j_dev()

    # Task 2
    print("Task #2")
    print(C.mro())
    print(D.mro())
    print(E.mro())

    # Task 3
    print("Task #3")
    somecompany = ItCompany()
    somecompany.add_employee(p_dev)
    somecompany.add_employee(j_dev)
    somecompany.add_employee(r_dev)

    print("before fire")
    somecompany.list_employees()
    somecompany.fire_employee("Kate")
    somecompany.fire_employee("Kate")
    print("after fire")
    somecompany.list_employees()
    print("trying to hire")
    somecompany.hire_employee(r_dev)
    somecompany.list_employees()
