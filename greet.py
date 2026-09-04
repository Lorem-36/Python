import time
current_time = time.localtime().tm_hour
if current_time < 10:
    print("Good morning!")
elif current_time < 18:
    print("Good afternoon!")
else:
    print("Good evening!")
    