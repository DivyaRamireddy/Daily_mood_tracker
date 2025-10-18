import datetime

# Function to record today's mood
def record_mood():
    mood = input("How are you feeling today? 😊 : ").capitalize()
    date = datetime.date.today()
    with open("mood_log.txt", "a") as file:
        file.write(f"{date} - {mood}\n")
    print(f"✅ Mood saved for {date}!\n")

# Function to view mood history
def view_history():
    try:
        with open("mood_log.txt", "r") as file:
            moods = file.readlines()
            if not moods:
                print("No moods recorded yet!\n")
                return
            print("📅 Your Mood History:\n")
            for line in moods:
                print(line.strip())
    except FileNotFoundError:
        print("No mood data found yet!\n")

# Function to show the most frequent mood
def most_common_mood():
    try:
        with open("mood_log.txt", "r") as file:
            moods = [line.strip().split(" - ")[1] for line in file.readlines()]
            if not moods:
                print("No moods recorded yet!\n")
                return
            mood_count = {}
            for mood in moods:
                mood_count[mood] = mood_count.get(mood, 0) + 1
            most_common = max(mood_count, key=mood_count.get)
            print(f"💖 Your most common mood is: {most_common}\n")
    except FileNotFoundError:
        print("No mood data found yet!\n")

# Main menu
def main():
    while True:
        print("\n=== Daily Mood Tracker ===")
        print("1. Record Mood")
        print("2. View Mood History")
        print("3. Most Common Mood")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            record_mood()
        elif choice == "2":
            view_history()
        elif choice == "3":
            most_common_mood()
        elif choice == "4":
            print("👋 See you tomorrow!")
            break
        else:
            print("Invalid choice, try again!\n")

if __name__ == "__main__":
    main()
