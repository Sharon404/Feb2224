class Person:
  def __init__(self, name, age, gender):
      #creating class instance
    self.name = name
    self.age = age
    self.gender = gender

p1 = Person("John", 36, "Male")

#displaying the information of the person
print(p1.name)
print(p1.age)
print(p1.gender)
