import pandas as pd
import matplotlib.pyplot as plt
churn_data = pd.read_excel("DataSet.xlsx")

age = input("How old are you?")
budget = input("What is your budget?")
main_use = input("What will your main use be out of: WordProcessing (WP); OnlineMeetings (OP); School (S); Music Production (MP); Computer Programming (CP); and University (U)? Please type in one of the initials provided.")
usage_hours_per_week = input("What will your weekly usage hours be?")
storage_needed = input("How much storage will you need (GB)?")
memory_needed = input("How much memory will you need (GB)?")
users = input("How many users will it have?")
color = input("What color would you like it in out of: Grey (G); Silver (S); Blue (B); Pink (P); and Red (R)? Please type in one of the initials provided.")
touchscreen = input("Would you like it to have a touchscreen? Please type in y for yes or n for no.")
