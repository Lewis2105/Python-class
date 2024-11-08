# Python inheritance
class Animal:
    def __init__(self, limbs, claws, nose):
        self.limbs = limbs
        self.claws = claws
        self.nose = nose

    def fur(self):
        print("I have fur all over my body")

class Dog(Animal):
    def __init__(self, limbs, claws, nose, tail):
        super().__init__(limbs, claws, nose)
        self.tail = tail

    def bark(self):
        print("Dog Barking")

    def walk(self):
        print("Dog Walking")

class Puppy(Dog):
    def __init__(self, limbs, claws, nose):
        super().__init__(limbs, claws, nose, tail=True)

    def play(self):
        print("I play all the time")

bosco = Puppy(4, 10, "wet")
bosco.play()
bosco.bark()