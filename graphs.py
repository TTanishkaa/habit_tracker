import matplotlib.pyplot as plt
from db import get_progress, get_timeline

def show_progress(habit_name):
    progress = get_progress(habit_name)
    plt.bar([habit_name], [progress], color="skyblue")
    plt.title(f"Progress for {habit_name}")
    plt.ylabel("Total Logs")
    plt.show()

def show_timeline(habit_name):
    dates = get_timeline(habit_name)
    if not dates:
        print(f"⚠️ No logs found for {habit_name}.")
        return
    plt.plot(dates, [i+1 for i in range(len(dates))], marker="o", color="green")
    plt.title(f"Timeline of {habit_name}")
    plt.xlabel("Date")
    plt.ylabel("Times Completed")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
