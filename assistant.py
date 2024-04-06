import datetime
from time import sleep
from keyboard import press_and_release, write
import webbrowser

flag = False

try:
    with open("username.txt", "r") as file:
        username = file.read()

    #checking for banned words usage
    if username == " ":
        print("Error: Unvalid username!")
    elif username.lower() == "hitler" or username.lower() == "nazi":
        print("Banned words cannot be used.\nThis incident will be reported.")
        flag = False
    else:
        with open("passw.txt", "r") as file:
            password = file.read()
        passw = input("Enter your password: ")
        if passw == password:
            flag = True
        else:
            print("Wrong password. Try again.")


    #file not found error
except FileNotFoundError:
    print("No user database found.")
    sleep(1.5)
    print("Creating new user...")
    sleep(1)
    u_name = input("Enter new username: ")
    username = u_name
    password = input("Create password: ")

    #checking for banned words usage
    if username.lower() == "hitler" or username.lower() == "nazi":
        print("Banned words cannot be used.\nThis incident will be reported.")
        flag = False
    else:
        with open("username.txt", "w") as file:
            file.write(username)
        with open("passw.txt", "w") as file:
            file.write(password)
        print("Username added to database.")
        flag = True

while flag:
    print("How may I be of your service?")
    task = input()

    #prompts
    if "time" in task.lower():
            current_datetime = datetime.datetime.now()
            current_time = current_datetime.time()
            print("The time is ", current_time)
            loop_turn = input(f"Anything else {username}?\n")
            if loop_turn.lower() == "no" or loop_turn.lower() == "nah" or loop_turn.lower() == "na":
                print(f"Thanks for using this prototype!\nHope you liked it {username}!")
                sleep(1.5)
                break
            else:
                continue
            
    elif "weather" in task.lower():
        sleep(1)
        print("Searching query...")
        sleep(1)
        webbrowser.open('https://www.msn.com/en-in/weather/forecast/in-Haora,WB?loc=eyJsIjoiSGFvcmEiLCJyIjoiV0IiLCJjIjoiSW5kaWEiLCJpIjoiSU4iLCJnIjoiZW4taW4iLCJ4IjoiODguMzA4MTA1NDY4NzUiLCJ5IjoiMjIuNTczNDM4NjQ0NDA5MTgifQ%3D%3D&weadegreetype=C&ocid=winp2fphotkey&cvid=b493dba7906043e696875f1645f14534')
        sleep(5.5)
        press_and_release('alt + tab')
        loop_turn = input(f"Anything else {username}?\n")
        if loop_turn.lower() == "no" or loop_turn.lower() == "nah" or loop_turn.lower() == "na":
            print(f"Thanks for using this prototype!\nHope you liked it {username}!")
            sleep(1.5)
            break
        else:
            continue
    elif "joke" in task.lower():
        print("Thinking...")
        sleep(2)
        print("What did one eye tell the other?")
        sleep(2)
        print("Between you and me, something smells👃🏽")
        loop_turn = input()
        if loop_turn.lower() == "not funny" or loop_turn.lower() == "bruh":
            print("I think you didn't like the joke.\nI'll try later.")
            sleep(1.5)
            break
        else:
            print(f"Ha ha! Got you good {username}!")
            sleep(2)
            loop_turn = input(f"Anything else?\n")
            if loop_turn.lower() == "no" or loop_turn.lower() == "nah" or loop_turn.lower() == "na":
                print(f"Thanks for using this prototype!\nHope you liked it {username}!")
                sleep(1.5)
                break
            else:
                continue
    elif "bye" or "goodbye" in task.lower():
        print(f"Goodbye {username}! See you soon!")
        sleep(1)
        print(f"Feel free to ask me if you need help.")
        sleep(1.5)
        break
    else:
        print("Sorry, I couldn't understand.")
        sleep(1)
        print("Let's try that again!")
        sleep(1)
        continue