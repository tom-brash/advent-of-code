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
            storage[n] = hashlib.md5(attempt.encode()).hexdigest()
        hash = storage[n]
        t = check_candidate(hash)

        if t != 'None':
            reg_string = t * 5
            reg_ex = re.compile(reg_string)
            for i in range(n + 1, n + 1001):
                if i not in storage:
                    attempt = salt + str(i)
                    storage[i] = hashlib.md5(attempt.encode()).hexdigest()
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


if __name__ == '__main__':
    main()
