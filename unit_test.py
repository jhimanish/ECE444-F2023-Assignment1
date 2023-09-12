class utils:
    """A simple utils class"""

    def reversed(num):
        # takes in a number and returns the number reversed
        # parameter: integer
        num = int(num)
        if num >= 0:
            return int(str(num)[::-1])
        else:
            return -1 * int(str(-1 * num)[::-1])

    def formatter(num):
        # takes in a number and returns the number in base 2 (binary) and base 8 (octal) format
        # parameter: int
        num = int(num)
        num_binary = bin(num)
        num_octal = oct(num)
        return num_binary, num_octal
