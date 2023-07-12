import time

def focus_timer(duration):
    print(f"Focus timer started for {duration} minutes.")
    duration_seconds = duration * 60
    end_time = time.time() + duration_seconds

    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        print(f"Time remaining: {minutes:02d}:{seconds:02d}", end='\r')
        time.sleep(1)

    print("\nTime's up! Focus timer ended.")

# 提示用户输入专注时间
focus_time = int(input("Enter the focus time in minutes: "))
focus_timer(focus_time)
