import time
from config import MODE_INTERVAL, MATH_MODE_EQUATION

def math_move(movesset, step):
    transformed_step = eval(MATH_MODE_EQUATION, {"step": step})
    move_index = transformed_step % 6
    movesset[move_index]()

def automovemath(movesset, interval=MODE_INTERVAL, extra=None):
    print("Starting math-based automatic movement every", interval, "seconds.")
    step = 0
    try:
        while True:
            math_move(movesset, step)
            if extra is not None:
                print("Current Position:", extra)  # Just print the list directly
            step += 1
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nMath auto movement stopped by user.")
