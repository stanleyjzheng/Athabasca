import random
import sys

def random_userID():
    return random.randint(100, 1000)

def random_list():
    l1 = sys.argv[1:]
    try:
        random_idx = random.sample(range(0, len(l1)), 3)
        out = [l1[i] for i in random_idx]
        return out
    except:
        return l1
