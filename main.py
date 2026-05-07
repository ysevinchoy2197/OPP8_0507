# 8
class Teacher:
    def __init__(self, name, subject, salary):
        self.name = name
        self._subject = subject
        self.__salary = salary

    def teach(self, hours):
        self._subject += hours

    def increase_salary(self, x):
        self.__salary += x

    def info(self):
        print(f"name: {self.name}, subject: {self._subject}, salary: {self.__salary}")


t1 = Teacher("Jamshid", 0, 800)

t1.teach(2)
t1.increase_salary(400)
t1.info()
