class Person:
  def __init__(self, name, age, gender):
      #creating class instance
    self.name = name
    self.age = age
    self.gender = gender

p = Person("Jane", 25, "Female")

#displaying the information of the person
print(p.name)
print(p.age)
print(p.gender)
