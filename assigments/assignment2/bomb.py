import time

def countdown_timer(start=10):
    """
    Counts down from the specified start value to 1, pausing 1 second between each number.
    """
    count = start
    while count >= 1:
        print(count)
        time.sleep(1)
        count -= 1
    print("Countdown finished.")

# Example usage:
# countdown_timer()
 