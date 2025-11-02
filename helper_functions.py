#!/usr/bin/python
def validate_input(input): 
    if isinstance(input, str) and input !="":
        return True
    else:
        return False
    

def create_message(ur_name, ur_age, name_binary, age_binary):
    message = f"Hello {ur_name}, you are {ur_age} years old.\n"
    message += "Name in Binary: " + ' '.join(name_binary) + "\n"
    message += f"Age in Binary: {age_binary}\n"
    return message

def convert_to_binary(a,b):
   name_binary= [bin(ord(letter)) for letter in a]  
   age_binary = bin(int(b)) 
   return name_binary, age_binary
