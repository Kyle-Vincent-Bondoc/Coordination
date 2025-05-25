import random
import time
from config import *

def random_move(movesset):
  move = random.choice(moves)
  move()

def automoverandom(movesset, interval=MODE_INTERVAL, extra)
    print("Starting automatic random movement every ", interval, " seconds.")
    try:
        while True:
            random_move(moves)
            print(extra)
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nAuto movement stopped by user.")
