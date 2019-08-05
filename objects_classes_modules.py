
#problem statement https://www.codewars.com/kata/thinkful-object-drills-vectors/train/python

#my attempt

class Vector(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def add(self, a, b):
        return self.add = a + b

#codewars solution

class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def add(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y) 



#--------------------------------

#problem statement https://www.codewars.com/kata/thinkful-object-drills-puzzlebox

#absolutely no idea what I'm supposed to do here. Instructions very unclear. I just skipped this one.


#codewars solution

    def answer(puzzlebox):
    #print(dir(puzzlebox))
    #puzzlebox.hint
    #print(puzzlebox.hint_two)
    #print(puzzlebox.lock(puzzlebox.key))
    return 42
    pass


#--------------------------------
#problem statement https://www.codewars.com/kata/thinkful-object-drills-quarks/train/python

#my code

class Quark(object):
    
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
        
baryon_number = 1/3

    def interact(self, other_quark):
        self.color, other_quark.color = other_quark.color, self.color


#codewars solution

class Quark():
    baryon_number = 1 / 3
    def __init__(self, color, flavor):
        self.color, self.flavor = color, flavor
    def interact(self, other):
        self.color, other.color = other.color, self.color

