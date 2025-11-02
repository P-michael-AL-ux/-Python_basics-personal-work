#!/usr/bin/python
from helper_functions import create_message
message_file="user_message.txt"
def save_message(message):
    with open(message_file, "a") as fil:
       fil.write(message + "\n")
    print("Message saved successfully")
# save_message()

def read_message(a):
    print("====================================")
    try:
        with open(a,"r") as fil:
            content =fil.read()
            print(content)
    except:
        print("File not found")
    print("====================================")
# read_message(message_file)


