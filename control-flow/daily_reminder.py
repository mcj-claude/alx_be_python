task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
while priority not in ["high", "medium", "low"]:
    priority = input("Invalid priority. Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
while time_bound not in ["yes", "no"]:
    time_bound = input("Invalid input. Is it time-bound? (yes/no): ").lower()

if time_bound == "yes":
    extra = " that requires immediate attention today!"
else:
    extra = ""

match priority:
    case "high":
        print(f"Reminder: '{task}' is a high priority task{extra}")
    case "medium":
        print(f"Reminder: '{task}' is a medium priority task{extra}")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task{extra}")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")