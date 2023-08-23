#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

# class Dog:

#     def set_name(self):
#         # self.name = name
#         print("Working")
#     #     if (type(name)) in (str) and (1<=len(name)<=25):
#     #         print(name)
#     #     else:
#     #          "Name must be string between 1 and 25 characters."
#     #     #  self.name = name    
#     # name= property(set_name)

# guido= Dog("Guido")
# guido.set_name()    
# class Dog:
#     def __init__(self, name):
#         self.name = name

#     def set_name(self):
#         # self.name = name
#         # return self.name
#         # print("Working")
#         if (type(name)) in (str) and (1<=len(name)<=25):
#             return  self.name   
#         else:
#             return "Name must be string between 1 and 25 characters."
        
#     name= property(set_name) 
# fido = Dog("Kelvin")
# print(fido.set_name())
class Dog:
    def __init__(self, name="Simba", breed="Corgi"):
        self.name = name
        self.breed = breed

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")
    name = property(get_name, set_name)        
# fido= Dog("Fido")
# print(fido.set_name())
    def get_breed(self):
        return self._breed
    
    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")
    breed = property(get_breed, set_breed)        