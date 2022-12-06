import hashlib

vecs = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}
vecs = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}

attempt = 'x'
result = hashlib.md5(attempt.encode()).hexdigest()