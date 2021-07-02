import random
import string
import time

random.seed(time.time_ns())


def random_string(n: int) -> string:
    return "".join(random.choices(string.ascii_lowercase, k=n))
