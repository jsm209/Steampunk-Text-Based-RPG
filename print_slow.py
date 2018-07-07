import sys
import time


class PrintSlow:

    def print_slow(text):
        for letter in text:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.1)