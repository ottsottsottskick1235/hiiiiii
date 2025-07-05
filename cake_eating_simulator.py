import time

def eat_cake(pieces=8):
    for piece in range(pieces, 0, -1):
        slice_num = pieces - piece + 1
        print(f"\U0001F370 Eating slice {slice_num}")
        time.sleep(0.5)
        remaining = piece - 1
        if remaining:
            plural = 's' if remaining != 1 else ''
            print(f"{remaining} slice{plural} remaining...")
        else:
            print("No more cake left!")

if __name__ == "__main__":
    eat_cake()

