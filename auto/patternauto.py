import time
from config import MODE_INTERVAL

def pattern_move(movesset, interval=MODE_INTERVAL, extra):
    print("Starting pattern movement every", interval, "seconds.")
    try:
        while True:
            for move in movesset:
                move()
                print(extra)
                time.sleep(interval)
    except KeyboardInterrupt:
        print("\nPattern movement stopped by user.")
