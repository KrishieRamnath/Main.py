import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea
comp_models = pd.read_excel("DataSet.xlsx")
age_means = pd.read_excel("DataSetAge.xlsx")

age = int(input("How old are you?"))
budget = int(input("What is your budget ($)?"))
main_use = input("What will your main use be out of: WordProcessing (WP); OnlineMeetings (OM); School (S); Music Production (MP); Computer Programming (CP); and University (U)? Please type in one of the initials provided.")
usage_hours_per_week = int(input("What will your weekly usage hours be?"))
storage_needed = int(input("How much storage will you need (GB)?"))
memory_needed = int(input("How much memory will you need (GB)?"))
users = int(input("How many users will it have?"))
color = input("What color would you like it in out of: Grey (G); Silver (S); Blue (B); Pink (P); and Red (R)? Please type in one of the initials provided.")
touchscreen = input("Would you like it to have a touchscreen? Please type in y for yes or n for no.")

right_model = ""

answers = []

#if age ==

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

if main_use == "WP":
    if memory_needed >=16:
        if touchscreen == "n":
            right_model = "MacBook Air"
        elif touchscreen == "y":
            right_model = "Microsoft Surface Book"
    else:
        if budget >= 1100:
            right_model = "Microsoft Surface Laptop"
        else:
            right_model = "Samsung Galaxy Book"

if main_use == "OM":
    if budget >= 1100:
        right_model = "MacBook Air"
    else:
        if memory_needed >= 16:
            right_model = "Samsung Galaxy Book"
        else:
            right_model = "Lenovo Ideapad"

print(f"You should buy a {right_model}.")


question_1 = input("Would you like to see a graph? Please input y for yes or n for no.\nSGB - Samsung Galaxy Book\nLI - Lenovo Ideapad\nMSG - Microsoft Surface Go\nMSB - Microsoft Surface Book\nMBA - MacBook Air\nMSP - Microsoft Surface Pro\nMBP - MacBook Pro\nMSLG - Microsoft Surface Laptop Go\nMSL - Microsoft Surface Laptop")

if question_1 == "y":
    question_2 = input("Which of these would you like to see in relation to computer model bought: Age (A); Budget (B); Main Use (MU); Usage Hours Per Week (UHPW); Storage Needed (SN); Memory Needed  (MN); Users (U); Color (C); Touchscreen (T) or Model (M)? Please type in one of the initials provided.")

#grouped_data = comp_models.groupby('Model')['Age'].mean()
#means = grouped_data['Age'].mean()
#mean_data = grouped_data['Age'].mean()
#summary_df = grouped_data['Age'].agg(['mean']).reset_index()
#Work out the mean age for each computer model.
#Use those numbers in the bar chart.
#mean_for_category = means.loc['MSG']
#print(summary_df)
#print(means)


if question_2 == "A":
    Model = age_means['Model']
    Age = age_means['Age']
    plt.figure(figsize=(60, 8))
    plt.bar(Model, Age)
    plt.xlabel('Model')
    plt.ylabel('Age')
    plt.title('The Average Age Of User Of Each Computer Model', fontsize=16, fontweight='bold')
    plt.show()
    sea.set(style='whitegrid')
    #comp_models = sea.load_dataset("comp_models")
    sea.swarmplot(data=comp_models, x='Model', y='Age').set(title='The Age Of Each User Against Their Computer Model')
    plt.show()
    #correlation = comp_models['Age'].corr(comp_models['Model'])

if question_2 == "B":
    Model = comp_models['Model']
    Budget = comp_models['Budget']
    plt.figure(figsize=(60, 8))
    plt.bar(Model, Budget)
    plt.xlabel('Model')
    plt.ylabel('Budget')
    plt.title('How Budget Affects Computer Model Bought', fontsize=16, fontweight='bold')
    correlation = comp_models['Budget'].corr(comp_models['Model'])


#See corelation between aspect and model (if there is aspect).