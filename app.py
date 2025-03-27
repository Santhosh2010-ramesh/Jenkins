from datetime import datetime

def mark_attendance(name):
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")

    with open("attendance_log.txt", "a") as file:
        file.write(f"{name} - {formatted_time}\n")

    print(f"Attendance marked for {name} at {formatted_time}")

user_name = input("Enter your name: ")
mark_attendance(user_name)
