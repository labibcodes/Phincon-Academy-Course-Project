this_time = int(input("what time is it now?"))

if this_time < 12:
    print("Good Morning")
elif 12 <= this_time <= 17:
    print("Good Afternoon")
else:
    print("Good Evening")