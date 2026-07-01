from z3 import *
import random
from itertools import permutations
from tqdm import tqdm


def encrypt_stage_one(message, key):
    res = []
    for i in key:
        for j in range(i, len(message), len(key)):
            res += [message[j]]

    return res


def decrypt_stage_two(message, now):
    random.seed(now)
    key = [random.randrange(256) for _ in message]

    return [m ^ k for (m, k) in zip(message, key + [0x42] * len(now))][:-18]


def main() -> None:
    with open("flag.enc", "rb") as f:
        flag_enc = f.read()
    now = bytes([0x42 ^ x for x in flag_enc[-18:]])
    flag_enc = bytes(decrypt_stage_two(flag_enc, now))
    print(flag_enc)
    keys = list(permutations(range(8)))
    flag_init = [BitVec(f"flag_{i}", 8) for i in range(len(flag_enc))]
    for k in tqdm(keys[6000:]):
        s = Solver()
        flag = flag_init.copy()
        print(k)
        for i, c in enumerate(b"FIAP{"):
            s.add(flag[i] == c)
        s.add(flag[-1] == ord("}"))
        for _ in range(42):
            flag = encrypt_stage_one(flag, k)
        for i, c in enumerate(flag_enc):
            s.add(flag[i] == c)
        if s.check() == sat:
            print("Found:")
            print(bytes([s.model()[x].as_long() for x in flag_init]))
            break


main()