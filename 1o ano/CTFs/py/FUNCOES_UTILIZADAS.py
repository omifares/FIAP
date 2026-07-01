import time
import random

def encrypt_stage_one(message, key):
    u = [s for s in sorted(zip(key, range(len(key))))]
    res = ''

    for i in u:
        for j in range(i[1], len(message), len(key)):
            res += message[j]

    return res

def encrypt_stage_two(message):
    now = str(time.time()).encode('utf-8')
    now = now + "".join("0" for _ in range(len(now), 18)).encode('utf-8')
    
    random.seed(now)
    key = [random.randrange(256) for _ in message]
    print("key", key, "end")
    return [m ^ k for (m,k) in zip(message + now, key + [0x42]*len(now))]
