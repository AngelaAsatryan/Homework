class Dog:
  def __init__(self, name, age, bread, sex, body, head, tail, legs, hair):
    self.name = name
    self.age = age
    self.bread=bread
    self.sex=sex
    self.body=body
    self.head=head
    self.tail=tail
    self.legs=legs
    self.hair=hair
  #methods
  def bark(arg):
    print("haf haf haf")
  def run(arg):
    print("The" + " " + arg.name + " " + "moving his" + " " + arg.legs +" "+ "legs"+ " "+"fast.")

#instance
dog1 = Dog("Rex", 3, "German shepherd", "male", "long and full", "big", "long and hairy", "long and strong", "dense and long")

print(dog1.name)
print(dog1.bread)
dog1.bark()
dog1.run()
