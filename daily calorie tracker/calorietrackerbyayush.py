
import datetime

print("===================================")
print("     DAILY CALORIE TRACKER APP     ")
print("===================================\n")
print("This tool helps you log your meals and check if you're within your daily calorie goal.\n")


meal_names = []
calories_list = []

meal_count = int(input("How many meals did you eat today? "))

for i in range(meal_count):
    meal_name = input(f"\nEnter the name of meal {i+1}: ").strip().capitalize()
    calories = float(input(f"Enter calories for {meal_name}: "))
    
    meal_names.append(meal_name)
    calories_list.append(calories)


total_calories = sum(calories_list)
average_calories = total_calories / meal_count
limit = float(input("\nEnter your daily calorie limit: "))


if total_calories > limit:
    status = f" Warning: You are {total_calories - limit:.2f} calories OVER your limit!"
else:
    status = f" Great job! You are {limit - total_calories:.2f} calories UNDER your limit!"


print("\n================= SUMMARY =================")
print(f"{'Meal Name':<15}{'Calories':>10}")
print("-------------------------------------------")

for name, cal in zip(meal_names, calories_list):
    print(f"{name:<15}{cal:>10.2f}")

print("-------------------------------------------")
print(f"{'Total:':<15}{total_calories:>10.2f}")
print(f"{'Average:':<15}{average_calories:>10.2f}")
print("===========================================")
print(status)
print("===========================================\n")


save = input("Do you want to save this report to a file? (yes/no): ").lower()

if save == "yes":
    filename = f"calorie_log_{datetime.date.today()}.txt"
    with open(filename, "w") as file:
        file.write("===========================================\n")
        file.write("         DAILY CALORIE TRACKER LOG         \n")
        file.write("===========================================\n")
        file.write(f"Date: {datetime.datetime.now()}\n\n")
        file.write(f"{'Meal Name':<15}{'Calories':>10}\n")
        file.write("-------------------------------------------\n")
        for name, cal in zip(meal_names, calories_list):
            file.write(f"{name:<15}{cal:>10.2f}\n")
        file.write("-------------------------------------------\n")
        file.write(f"{'Total:':<15}{total_calories:>10.2f}\n")
        file.write(f"{'Average:':<15}{average_calories:>10.2f}\n")
        file.write("===========================================\n")
        file.write(status + "\n")
        file.write("===========================================\n")

    print(f"\n✅ Report saved successfully as '{filename}'!")
else:
    print("\nReport not saved. Thank you for using the app!")

