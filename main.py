from db import create_tables, add_habit, log_habit, list_habits
from graphs import show_progress, show_timeline

def menu():
    print("\n📊 Habit Tracker Menu")
    print("1. Add new habit")
    print("2. List habits")
    print("3. Log habit")
    print("4. Show habit progress (bar chart)")
    print("5. Show habit timeline (line chart)")
    print("6. Exit")

def main():
    create_tables()

    while True:
        menu()
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            name = input("Enter new habit name: ").strip()
            habit_type = input("Type (daily/weekly/monthly): ").strip().lower()
            add_habit(name, habit_type)

        elif choice == "2":
            habits = list_habits()
            if habits:
                print("\nYour Habits:")
                for h in habits:
                    print(f"- {h[0]} ({h[1]})")
            else:
                print("⚠️ No habits found.")

        elif choice == "3":
            name = input("Enter habit name to log: ").strip()
            log_habit(name)

        elif choice == "4":
            name = input("Enter habit name to view progress: ").strip()
            show_progress(name)

        elif choice == "5":
            name = input("Enter habit name to view timeline: ").strip()
            show_timeline(name)

        elif choice == "6":
            print("👋 Goodbye!")
            break

        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
