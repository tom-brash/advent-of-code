test_string = "ZAFBOLTZAYEMETHJPNNAMSLESWEEGYBRAMLIUKRGINNGACHNMCOLTUPOLBELCANAUTSSDTURPAKPERBHRIDNCOLGEO"

remove_letters = 'bluepikachBLUEPIKACH'

for letter in remove_letters:
    test_string = test_string.replace(letter, '')

print(test_string)