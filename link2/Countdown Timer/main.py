import time

def countdown_timer():
    total_seconds = int(input("Enter the time in seconds: "))

    while total_seconds:
        mins, secs = divmod(total_seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')  
        time.sleep(1)
        total_seconds -= 1

    print("⏰ Time's up!")

countdown_timer()
