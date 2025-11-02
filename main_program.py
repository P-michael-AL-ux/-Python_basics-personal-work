#!/usr/bin/python
from helper_functions import validate_input, convert_to_binary, create_message
from file_manager import save_message, read_message
from greetings import show_intro, show_exit_message

def get_user_info():        
        while True:
            ur_name = input("Please Enter your name: ")
            if   validate_input(ur_name) == True and ur_name.isalpha():
                  print(f"Hi {ur_name}! You have a nice name.")
                  break
            else:
                print("Invalid input, Please try again")
                continue     
        while True: 
            ur_age = input("Please enter your age: ")
            if   validate_input(ur_age) == True and ur_age.isdigit():
                  print("valid age.")
                  break
                  
            else:
                print("Invalid input, Please try again")
                continue
        return ur_name, ur_age


if __name__ == "__main__":
     show_intro()
     inputs=get_user_info()
     text=convert_to_binary(inputs[0],inputs[1])
     message=create_message(inputs[0], inputs[1], text[0], text[1])
     message_file="user_message.txt"
     save_message(message)
     read_message(message_file)
     show_exit_message()