s = 'krxano xgrakauuiie oppfend aeaiffi'

o = ''
for c in s:
    if c == ' ':
        o += c
    elif c in 'abdegopq':
        o += 'V'
    else:
        o += 'C'

print(o)
