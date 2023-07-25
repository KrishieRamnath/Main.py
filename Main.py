import pandas as pd
import matplotlib.pyplot as plt
churn_data = pd.read_excel("DataSet.xlsx")

age = int(input("How old are you?"))
budget = int(input("What is your budget ($)?"))
main_use = input("What will your main use be out of: WordProcessing (WP); OnlineMeetings (OP); School (S); Music Production (MP); Computer Programming (CP); and University (U)? Please type in one of the initials provided.")
usage_hours_per_week = int(input("What will your weekly usage hours be?"))
storage_needed = int(input("How much storage will you need (GB)?"))
memory_needed = int(input("How much memory will you need (GB)?"))
users = int(input("How many users will it have?"))
color = input("What color would you like it in out of: Grey (G); Silver (S); Blue (B); Pink (P); and Red (R)? Please type in one of the initials provided.")
touchscreen = input("Would you like it to have a touchscreen? Please type in y for yes or n for no.")

right_model = ""

if main_use == "MP":
    if touchscreen == "n":
        right_model = "MacBook Pro"
    elif touchscreen == "y":
        right_model = "Microsoft Surface Book"

if main_use == "CP":
    if touchscreen == "n":
        if budget <= 1200:
            right_model = "MacBook Air"
        else:
            right_model = "MacBook Pro"
    if touchscreen == "y":
        if budget <= 2000:
            right_model = "Samsung Galaxy Book"
        else:
            right_model = "Microsoft Surface Book"

if main_use == "S":
    if touchscreen == "n":
        right_model = "Microsoft Surface Laptop Go"
    elif touchscreen == "y":
        right_model = "Microsoft Surface Go"

if main_use == "U":
    if storage_needed >= 512:
        right_model = "Microsoft Surface Laptop"
    else:
        right_model = "Microsoft Surface Pro"


print(f"You should buy a {right_model}.")