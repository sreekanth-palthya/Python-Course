class Employee:
    def work(self):
        print("Employee works")

class Developer(Employee):
    def code(self):
        print("Developer writes code")

class Manager(Employee):
    def manage(self):
        print("Manager manages the team")

class TechLead(Developer, Manager):
    def lead(self):
        print("Tech Lead leads the technical team")

t = TechLead()
t.work()
t.code()
t.manage()
t.lead()
