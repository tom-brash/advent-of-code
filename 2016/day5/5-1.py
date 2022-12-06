import hashlib

n = 0
doorcode = 'ffykfhsq'

final_code = ''
while len(final_code) < 8:
    attempt = doorcode + str(n)
    result_hex = hashlib.md5(attempt.encode()).hexdigest()
    if result_hex[:5] == '00000':
        final_code += result_hex[5]
        print('Number found!', n)
    n += 1

print(final_code)
    
