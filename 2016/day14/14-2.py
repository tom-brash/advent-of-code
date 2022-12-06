import hashlib
import re

def main():
    salt = 'ngcjuoqr'

    n = 0
    found = []
    storage = {}
    while len(found) < 64:
        if n not in storage:
            attempt = salt + str(n)
            storage[n] = custom_hash(attempt)
        hash = storage[n]
        t = check_candidate(hash)

        if t != 'None':
            reg_string = t * 5
            reg_ex = re.compile(reg_string)
            for i in range(n + 1, n + 1001):
                if i not in storage:
                    attempt = salt + str(i)
                    storage[i] = custom_hash(attempt)
                hash_check = storage[i]
                if re.search(reg_ex, hash_check) != None:
                    found.append(n)
                    print(f'Found match number {len(found)} at {n}')
                    break

        n += 1

def check_candidate(hash):
    trips = re.search(r'([a-z0-9])\1\1', hash)
    if trips == None:
        return 'None'
    else:
        return trips.group(1)[0]


def custom_hash(attempt):
    for _ in range(2017):
        attempt = hashlib.md5(attempt.encode()).hexdigest()
    return attempt


if __name__ == '__main__':
    main()
