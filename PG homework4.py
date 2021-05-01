# -*- coding: utf-8 -*-
"""
Created on Sat May  1 10:21:31 2021

@author: emmet
"""
class Pet():
    def __init__(self, name, weight, color, jender, age, speed):
        self.name = name
        self.weight = weight
        self.color = color
        self.jender = jender
        self.age = age
        self.speed = speed
        
class Dog(Pet):
    def __init__(self, name, weight, color, jender, age, speed):
        super().__init__(name, weight, color, jender, age, speed)
        self.Dpower = 100
        self.Dposition = 0
    def DRun(self):
        if self.Dpower > 0:
            self.Dpower -=1
            self.Dposition = self.Dposition + self.speed
            
class Cat(Pet):
    def __init__(self, name, weight, color, jender, age, speed):
        super().__init__(name, weight, color, jender, age, speed)
        self.CPower = 50
        self.CPosition = 0
        
    def CRun(self):
        if self.CPower > 0:
            self.CPower -=1
            self.CPosition = self.CPosition +self.speed
            
            

Dog1 = Dog("app", 20, (127, 199, 255), "boy", 10, 30)

for i in range(100):
    Dog1.DRun()
    
print("Dog's power is: "+ str(Dog1.Dpower))
print("Dog's position is: "+ str(Dog1.Dposition))


Cat1 = Cat("asd", 18, (200, 200, 200), "boy",14, 50)


for u in range(100):
    Cat1.CRun()
    
print("Cat's power is: "+str(Cat1.CPower))
print("Cat's position is: "+str(Cat1.CPosition))