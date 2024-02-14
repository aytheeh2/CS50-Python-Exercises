def convert(time_str):
    # Split the time string into hours and minutes
    hours, minutes = map(int, time_str.split(':'))
    # Convert the time to the corresponding number of hours as a float
    return hours + minutes / 60

def main():
    # Get user input for the time
    time_input = input("Enter the time in 24-hour format (e.g., 7:30 or 15:45): ")

    # Convert the input time to a float representation
    time_in_hours = convert(time_input)

    # Define the meal time ranges in hours
    breakfast_start = 7.0
    breakfast_end = 8.0
    lunch_start = 12.0
    lunch_end = 13.0
    dinner_start = 18.0
    dinner_end = 19.0

    # Check if it's breakfast time
    if breakfast_start <= time_in_hours <= breakfast_end:
        print("breakfast time")
    # Check if it's lunch time
    elif lunch_start <= time_in_hours <= lunch_end:
        print("lunch time")
    # Check if it's dinner time
    elif dinner_start <= time_in_hours <= dinner_end:
        print("dinner time")

if __name__ == "__main__":
    main()
