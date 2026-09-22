# Multilevel inheritance means inheritance happens in multiple levels

# Grandfather
#      ↓
#    Father
#      ↓
#     Son

class Grandfather:
    def house(self):
        print("Grandfather's house")
class Father(Grandfather):
    def car(self):
        print("Father's car")
class son(Father):
    def bike(self):
        print("Son's bike")
s=son()
s.house()
s.car()
s.bike()

# -----output:
# Grandfather's house
# Father's car
# Son's bike