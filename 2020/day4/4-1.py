'''
DAY 4-1: Check for passport validity

We hardcode a set of required passport fields, and then go through each one,
checking that they are present
'''

def main():

    with open('day4/4-1-input.txt', 'r') as input_data_file:
        input_data = input_data_file.read()

    passports = input_data.split('\n\n')
    req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    passports = [x.replace('\n', ' ') for x in passports]

    valid = 0

    for passport in passports:
        if check_passport(passport, req_fields):
            valid += 1

    print(valid)


def check_passport(passport, req_fields):
    valid = True
    for field in req_fields:
        field_str = field + ':'
        if field_str not in passport:
            valid = False
            break
    return valid


if __name__ == '__main__':
    main()   