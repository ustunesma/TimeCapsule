# time_capsule.py
# COE203 Project 1 - Time Capsule
# Your Name - Fall 25-26

import datetime
import os
from datetime import date 

FILE_NAME = "capsule.txt"
IMAGE_FOLDER = "capsule_images"

# Create image folder if it doesn't exist

if not os.path.exists(IMAGE_FOLDER):
    os.mkdir(IMAGE_FOLDER)


# ---------------- Functions ---------------- #

def add_message(messages):
    try:
     name = input("Enter your name: ")

     text = input("Enter your message: ")
     year = int(input("Unlock year (e.g., 2026): "))
     if year < 2025:
         print("Unlock year must be more than 2024!")
         return                        
     month = int(input("Unlock month (1-12): "))
     day = int(input("Unlock day (1-31): "))
    except:
        print("Invalid input! Please enter valid numbers for year, month, and day.")
        return
    
    # Format: 2026-12-25|Hello future me!
    message = f"{year}-{month:02d}-{day:02d}|{text}"
    messages.append(message)
    print("Message sealed in capsule!")
    save_capsule(messages)

def save_capsule(messages):
    with open("capsule.txt", "w") as file:
        for msg in messages:
            file.write(msg + "\n")

def load_capsule():
    messages = []
    try:
        with open("capsule.txt") as file:
            for line in file:
                line = line.strip()
                if line:
                    messages.append(line)
    except FileNotFoundError:
        print("No capsule found. Starting fresh!")
    return messages

def is_unlocked(date_str):
    try:
        year = int(date_str.split('-')[0])
        current_year = 2025  # Update this if needed
        return current_year >= year
    except:
        return False

def view_unlocked(messages):
    unlocked = []
    for msg in messages:
        parts = msg.split('|', 1)
        if len(parts) == 2:
            date_part, text = parts
            if is_unlocked(date_part):
                unlocked.append(text)
    
    if unlocked:
        print("\nUnlocked Messages:")
        for i, msg in enumerate(unlocked, 1):
            print(f"{i}. {msg}")
    else:
        print("No messages unlocked yet. Come back later!")

def main():
    print("--------------------------------")
    print("Welcome to Your Time Capsule!")
    print("--------------------------------")
    messages = load_capsule()
    
    while True:
        print("\n" + "="*30)
        print("1. Add Message")
        print("2. View Unlocked")
        print("3. Exit")
        print("="*30)
        choice = input("Choose: ")
        
        if choice == "1":
            add_message(messages)
        elif choice == "2":
            view_unlocked(messages)
        elif choice == "3":
            print("Capsule sealed. See you in the future!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()