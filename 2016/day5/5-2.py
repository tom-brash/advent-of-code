import hashlib

n = 0
doorcode = 'ffykfhsq'

final_code = ['_'] * 8
found_numbers = 0
while found_numbers < 8:
    attempt = doorcode + str(n)
    result_hex = hashlib.md5(attempt.encode()).hexdigest()
    if result_hex[:5] == '00000':
        loc = result_hex[5]
        if loc.isnumeric():
            loc = int(loc)
            if loc < 8:
                if final_code[loc] == '_':
                    final_code[loc] = result_hex[6]
                    print(' '.join(final_code))
                    found_numbers += 1
    n += 1

print(''.join(final_code))
    
