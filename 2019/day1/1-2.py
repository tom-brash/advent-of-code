'''
--- Part Two ---
During the second Go / No Go poll, the Elf in charge of the Rocket Equation Double-Checker stops the launch sequence.
Apparently, you forgot to include additional fuel for the fuel you just added.

Fuel itself requires fuel just like a module - take its mass, divide by three, round down, and subtract 2. However, that
 fuel also requires fuel, and that fuel requires fuel, and so on. Any mass that would require negative fuel should
 instead be treated as if it requires zero fuel; the remaining mass, if any, is instead handled by wishing really hard,
which has no mass and is outside the scope of this calculation.

So, for each module mass, calculate its fuel and add it to the total. Then, treat the fuel amount you just calculated as
 the input mass and repeat the process, continuing until a fuel requirement is zero or negative. For example:

A module of mass 14 requires 2 fuel. This fuel requires no further fuel (2 divided by 3 and rounded down is 0, which
 would call for a negative fuel), so the total fuel required is still just 2.

At first, a module of mass 1969 requires 654 fuel. Then, this fuel requires 216 more fuel (654 / 3 - 2). 216 then
 requires 70 more fuel, which requires 21 fuel, which requires 5 fuel, which requires no further fuel. So, the total
 fuel required for a module of mass 1969 is 654 + 216 + 70 + 21 + 5 = 966.

The fuel required by a module of mass 100756 and its fuel is:
 33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.

What is the sum of the fuel requirements for all of the modules on your spacecraft when also taking into account
the mass of the added fuel? (Calculate the fuel requirements for each module separately,
then add them all up at the end.)
'''

def main():
    with open('day1/1-1-input.txt','r') as input_file:
        input_lines = input_file.read()

    masses = input_lines.split('\n')
    masses.remove('')
    print(masses)
    total = 0
    for mass in masses:
        total += check_fuel_inclusive(int(mass))

    print(total)


def check_fuel_inclusive(mass):
    complete = False
    total = 0
    while not complete:
        additional_fuel = max(mass // 3 - 2, 0)
        if additional_fuel < 9:  # any additional fuel under 9 will not need additional fuel to carry itself
            complete = True
        total += additional_fuel
        mass = additional_fuel

    return total


if __name__ == '__main__':
    main()