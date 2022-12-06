'''
DAY 4-2: Check for passport validity with rules for each field

Now we check passports both for the presence of required fields, but also
use a series of helper function for each of the rules to check that the value conforms
to what has been input
'''


import re

def main():

    with open('day4/4-1-input.txt', 'r') as input_data_file:
        input_data = input_data_file.read()

    passports = input_data.split('\n\n')
    

    passports = [str_to_dict(x.replace('\n', ' ')) for x in passports]
    
    valid = 0

    for passport in passports:
        if check_passport(passport) == True:
            valid += 1

    print(valid)

def str_to_dict(string):
    d = {}
    components = string.split(' ')
    for component in components:
        if component != '':
            key_val = component.split(':')
            d[key_val[0]] = key_val[1]
    return d


def check_passport(passport):
    req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
       
    for field in req_fields:
        if field not in passport:
            return False

    if (check_year(int(passport['byr']), 1920, 2002) == True and 
        check_year(int(passport['iyr']), 2010, 2020) == True and 
        check_year(int(passport['eyr']), 2020, 2030) == True and
        check_hgt(passport['hgt']) == True and
        check_hcl(passport['hcl']) == True and
        check_ecl(passport['ecl']) == True and
        check_pid(passport['pid']) == True):
        return True
    
    return False


def check_year(year, min, max):
    if year >= min and year <= max:
        return True
    return False

def check_hgt(hgt):
    unit = hgt[-2:]
    hgt = int(hgt[:-2])
    if unit == 'cm':
        if hgt >= 150 and hgt <= 193:
            return True
    if unit == 'in':
        if hgt >=59 and hgt <= 76:
            return True
    return False

def check_hcl(hcl):
    pattern = re.compile('#([a-f]|[0-9]){6}$')
    if pattern.match(hcl) != None:
        return True
    return False

def check_ecl(ecl):
    if ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True
    return False

def check_pid(pid):
    pattern = re.compile('([0-9]){9}$')
    if pattern.match(pid) != None:
        return True
    return False

if __name__ == '__main__':
    main()   