
time_in_seconds = int(input("Enter seconds: "))

if (time_in_seconds < 600):
    conversion = 600 - time_in_seconds
    print(f"You still need {conversion} seconds to reach 10 minutes")
elif (time_in_seconds == 600):
    print("Same")
else:
    print("Bigger")