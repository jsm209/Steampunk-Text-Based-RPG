import time


class PrintSlow:

    # Pre: Given a string of text
    # Post: Will split into lines and print each line out one at a time, waiting the specified time between lines.
    def print_slow(str=""):
        for line in str.splitlines():
            print(line)
            time.sleep(0.38)