import csv
import sys

# --- Helper Function: Shows a pretty menu ---
def show_welcome_message():
    print("\n" + "="*50)
    print("      STUDENT PERFORMANCE ANALYZER (v2.0)      ")
    print("="*50)
    print("Welcome! Please select an operation below:\n")
    print("   [1] Start a New Class List (Type names manually)")
    print("   [2] Import Data from File (Load a .csv file)")
    print("   [3] Quit / Exit Program")
    print("-" * 50)

# --- Function 1: Get Data Manually ---
def get_manual_input():
    print("\n>>> ENTERING MANUAL DATA MODE")
    print("-----------------------------------")
    
    student_data = {}
    
    # Friendly prompt
    print("How many students would you like to grade today?")
    count = int(input(">> Enter number: "))
    
    print(f"\nGreat. Let's enter details for {count} students.\n")
    
    for i in range(count):
        print(f"--- Student #{i+1} ---")
        name = input("   Name: ").title()
        score = int(input(f"   Score for {name} (0-100): "))
        student_data[name] = score
        
    print("\n[Success] All data recorded successfully.")
    return student_data

# --- Function 2: Get Data from File ---
def get_csv_input():
    print("\n>>> FILE IMPORT MODE")
    print("-----------------------------------")
    print("Tip: Ensure your CSV file is in the same folder.")
    
    filename = input(">> Please enter the exact filename (e.g., grades.csv): ")
    student_data = {}
    
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader) # Skip header
        
        print("... Reading file ...")
        for row in reader:
            if row:
                name = row[0].title()
                score = int(row[1])
                student_data[name] = score
                
    print(f"\n[Success] Successfully loaded {len(student_data)} students.")
    return student_data

# --- Function 3: Grading Logic ---
def calculate_grade(score):
    if score >= 90: return 'A'
    if score >= 80: return 'B'
    if score >= 70: return 'C'
    if score >= 60: return 'D'
    return 'F'

# --- Function 4: The Report Generator ---
def generate_report(student_data):
    if not student_data:
        print("\n[Error] No data found to analyze.")
        return

    scores = list(student_data.values())
    total_students = len(scores)
    
    # Calculate Stats
    average_score = sum(scores) / total_students
    sorted_scores = sorted(scores)
    mid_index = total_students // 2
    median_score = sorted_scores[mid_index]
    max_score = max(scores)
    min_score = min(scores)

    # --- Print The Report ---
    print("\n\n")
    print("*"*50)
    print("           FINAL CLASS REPORT CARD           ")
    print("*"*50)
    
    print(f"  > Total Students:  {total_students}")
    print(f"  > Class Average:   {average_score:.2f}")
    print(f"  > Median Score:    {median_score}")
    print(f"  > Highest Score:   {max_score}")
    print(f"  > Lowest Score:    {min_score}")
    
    print("\n" + "-"*50)
    print(f"{'Student Name':<20} | {'Score':^10} | {'Grade':^10}")
    print("-" * 50)

    rows_to_save = [['Name', 'Score', 'Grade']]
    passed_count = 0
    
    for name in sorted(student_data.keys()):
        s = student_data[name]
        g = calculate_grade(s)
        
        if s >= 40: passed_count += 1
            
        print(f"{name:<20} | {s:^10} | {g:^10}")
        rows_to_save.append([name, s, g])
        
    print("-" * 50)
    print(f"SUMMARY: Passed: {passed_count}  |  Failed: {total_students - passed_count}")
    print("=" * 50)

    # --- Save Option ---
    print("\nWould you like to save this report to a file?")
    save = input(">> Type 'yes' to save, or press Enter to skip: ").lower()
    
    if save == 'yes' or save == 'y':
        save_name = input(">> Enter a name for the new file: ")
        with open(save_name, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows_to_save)
        print(f"\n[Saved] Report saved as '{save_name}'.")

# --- Main Loop ---
def main():
    while True:
        show_welcome_message()
        choice = input(">> Enter your choice (1, 2, or 3): ")

        if choice == '1':
            data = get_manual_input()
            generate_report(data)
            input("\nPress Enter to return to menu...") # Pause so user can read
            
        elif choice == '2':
            data = get_csv_input()
            generate_report(data)
            input("\nPress Enter to return to menu...") # Pause so user can read
            
        elif choice == '3':
            print("\nExiting program. Have a nice day!")
            sys.exit()
            
        else:
            print("\n[!] Invalid selection. Please try again.")

if __name__ == "__main__":
    main()