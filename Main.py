import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea
comp_models = pd.read_excel("DataSet.xlsx")
age_means = pd.read_excel("DataSetAge.xlsx")
budget_means = pd.read_excel("DataSetBudget.xlsx")
most_common_main_use_means = pd.read_excel("DataSetMostCommonMainUse.xlsx")
number_of_times_it_is_main_use_means = pd.read_excel("DataSetNumberOfTimesItIsMainUse.xlsx")
usage_hours_per_week = pd.read_excel("DataSetUsageHoursPerWeek.xlsx")
storage_needed = pd.read_excel("DataSetMostCommonStorageAmountNeeded.xlsx")
memory_needed = pd.read_excel("DataSetMostCommonMemoryAmountNeeded.xlsx")
mean_number_of_users = pd.read_excel("DataSetMeanNumberOfUsers.xlsx")
most_common_color = pd.read_excel("DataSetMostCommonColor.xlsx")
number_of_times__main_color = pd.read_excel("DataSetNumberOfTimesMainColor.xlsx")
percentage_of_touchscreens = pd.read_excel("DataSetPercentageOfPeopleWhoWantATouchscreen.xlsx")

age = int(input("How old are you?"))
budget = int(input("What is your budget ($)?"))
main_use = input("What will your main use be out of: WordProcessing (WP); OnlineMeetings (OM); School (S); Music Production (MP); Computer Programming (CP); and University (U)? Please type in one of the initials provided.")
usage_hours__per_week = int(input("What will your weekly usage hours be?"))
storage__needed = int(input("How much storage will you need (GB)?"))
memory__needed = int(input("How much memory will you need (GB)?"))
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
    if storage__needed >= 512:
        right_model = "Microsoft Surface Laptop"
    else:
        right_model = "Microsoft Surface Pro"

if main_use == "WP":
    if memory__needed >= 16:
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

#Ideas for improvement:
#list of inputs = numpy.arr[]
#numreator = 0 (Numerator is the number of answers which match a set on the data set.)
#if numerator == 6:
#   Model = ['Model']
#elif numerator == 5:
#   Model = ['Model']
#elif numerator == 4:
# Model = ['Model']
#...

while True:
    question_1 = input("Would you like to see graphs? Please input y for yes or n for no.\nSGB - Samsung Galaxy Book\nLI - Lenovo Ideapad\nMSG - Microsoft Surface Go\nMSB - Microsoft Surface Book\nMBA - MacBook Air\nMSP - Microsoft Surface Pro\nMBP - MacBook Pro\nMSLG - Microsoft Surface Laptop Go\nMSL - Microsoft Surface Laptop")

    if question_1 == "y":
        question_2 = input("Which of these would you like to see in relation to computer model bought: Age (A); Budget (B); Main Use (MU); Usage Hours Per Week (UHPW); Storage Needed (SN); Memory Needed  (MN); Users (U); Color (C); or Touchscreen (T)? Please type in one of the initials provided.")

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
        plt.figure(figsize=(60, 8))
        sea.swarmplot(data=comp_models, x='Model', y='Age').set(title='The Age Of Each User Against Their Computer Model')
        plt.show()

    if question_2 == "B":
        Model = budget_means['Model']
        Budget = budget_means['Budget ($)']
        plt.figure(figsize=(60, 8))
        plt.bar(Model, Budget)
        plt.xlabel('Model')
        plt.ylabel('Budget ($)')
        plt.title('The Average Budget Of The User Of Each Computer Model', fontsize=16, fontweight='bold')
        plt.show()
        sea.set(style='whitegrid')
        plt.figure(figsize=(60, 8))
        sea.swarmplot(data=comp_models, x='Model', y='Budget').set(title='The Budget Of Each User Against Their Computer Model')
        plt.show()

    if question_2 == "MU":
        MainUse = number_of_times_it_is_main_use_means['MainUse']
        NumberOfTimesItIsMainUse = number_of_times_it_is_main_use_means['NumberOfTimesItIsMainUse']
        plt.figure(figsize=(40, 8))
        plt.bar(MainUse, NumberOfTimesItIsMainUse)
        plt.xlabel('MainUse')
        plt.ylabel('NumberOfTimesItIsMainUse')
        plt.title('The Number Of Computer Models That Each Use Is The Main Use Of', fontsize=16, fontweight='bold')
        plt.show()
        sea.set(style='whitegrid')
        plt.figure(figsize=(40, 8))
        sea.swarmplot(data=comp_models, x='Model', y='MainUse').set(title='The Main Uses Of Each Computer Model')
        plt.show()

    if question_2 == "UHPW":
        Model = usage_hours_per_week['Model']
        UsageHoursPerWeek = usage_hours_per_week['UsageHoursPerWeek']
        plt.figure(figsize=(60, 8))
        plt.bar(Model, UsageHoursPerWeek)
        plt.xlabel('Model')
        plt.ylabel('UsageHoursPerWeek')
        plt.title('The Average Weekly Usage Hours Of Each Computer Model', fontsize=16, fontweight='bold')
        plt.show()
        sea.set(style='whitegrid')
        plt.figure(figsize=(60, 8))
        sea.swarmplot(data=comp_models, x='Model', y='UsageHoursPerWeek').set(title='The Weekly Usage Hours Of Each User Against Their Computer Model')
        plt.show()

    if question_2 == "SN":
        Model = storage_needed['Model']
        MostCommonStorageAmountNeeded = storage_needed['MostCommonStorageAmountNeeded (GB)']
        plt.figure(figsize=(60, 8))
        plt.bar(Model, MostCommonStorageAmountNeeded)
        plt.xlabel('Model')
        plt.ylabel('Most Common Storage Amount Needed (GB)')
        plt.title('The Most Common Amount Of Storage Space Needed For Each Computer Model', fontsize=16, fontweight='bold')
        plt.show()
        sea.set(style='whitegrid')
        plt.figure(figsize=(60, 8))
        sea.swarmplot(data=comp_models, x='Model', y='StorageNeeded').set(title='The Storage Needed By Each User Compared To Their Computer Model')
        plt.show()

    if question_2 == "MN":
        Model = memory_needed['Model']
        MostCommonMemoryAmountNeeded = memory_needed['MostCommonMemoryAmountNeeded (GB)']
        plt.figure(figsize=(60, 8))
        plt.bar(Model, MostCommonMemoryAmountNeeded)
        plt.xlabel('Model')
        plt.ylabel('Most Common Memory Amount Needed (GB)')
        plt.title('The Most Common Amount Of Memory Needed For Each Computer Model', fontsize=16, fontweight='bold')
        plt.show()
        sea.set(style='whitegrid')
        plt.figure(figsize=(60, 8))
        sea.swarmplot(data=comp_models, x='Model', y='MemoryNeeded').set(title='The Memory Needed By Each User Compared To Their Computer Model')
        plt.show()

    if question_2 == "U":
        Model = mean_number_of_users['Model']
        MeanNumberOfUsers = mean_number_of_users['MeanNumberOfUsers']
        plt.figure(figsize=(60, 8))
        plt.bar(Model, MeanNumberOfUsers)
        plt.xlabel('Model')
        plt.ylabel('Mean Number Of Users')
        plt.title('The Mean Number Of Users Of Each Computer Model (Per Computer)', fontsize=16, fontweight='bold')
        plt.show()
        sea.set(style='whitegrid')
        plt.figure(figsize=(60, 8))
        sea.swarmplot(data=comp_models, x='Model', y='Users').set(title='The Number Of Users Of Each Computer Of Each Model')
        plt.show()

    if question_2 == "C":
        Color = number_of_times__main_color['Color']
        NumberOfTimesMainColor = number_of_times__main_color['NumberOfTimesMainColor']
        plt.figure(figsize=(60, 8))
        plt.bar(Color, NumberOfTimesMainColor)
        plt.xlabel('Color')
        plt.ylabel('Number Of Times It Is Most Common Color')
        plt.title('The Number Of Computer Models That Each Color Is The Most Common Color Of', fontsize=16, fontweight='bold')
        plt.show()
        sea.set(style='whitegrid')
        plt.figure(figsize=(60, 8))
        sea.swarmplot(data=comp_models, x='Model', y='Color').set(title='The Colors Of Each Model')
        plt.show()

    if question_2 == "T":
        Model = percentage_of_touchscreens['Model']
        Touchscreeners = percentage_of_touchscreens['Percentage Of People Who Want A Touchscreen']
        plt.figure(figsize=(60, 8))
        plt.bar(Model, Touchscreeners)
        plt.xlabel('Model')
        plt.ylabel('Percentage Of People Who Want A Touchscreen')
        plt.title('The Percentage Of People Who Want A Touchscreen', fontsize=16, fontweight='bold')
        plt.show()
        sea.set(style='whitegrid')
        plt.figure(figsize=(60, 8))
        sea.swarmplot(data=comp_models, x='Model', y='Touchscreen').set(title='The Touchscreen Needs Of Each Person For Each Model')
        plt.show()