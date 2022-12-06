'''
DAY 22-2: Shuffling a deck of 119,315,717,514,047 cards

Woof. The most brutal puzzle so far, and freely admit to looking at other resources
in order to 'solve' this one. Modular arithmetic and its various properties are 
essential to be able to solve this one. While through clever tracking you can solve
the problem of the 119t card deck extremely quickly, there isn't really a way to solve
the 101t iterations of shuffling without using modular arithmetic.

Crucially, each operation can be thought of as satisfying the form f(x) = (ax + b) % m
where c is the deck size. This form is known as a linear congruential function (LCF). 

When we apply multiple LCFs in a row, we can simplify down to applying a single LCF. 
Specifically, if we apply g(f(x)) where g(x) = cx + d, the overall function becomes
acx + bc + d mod m. Back in the original notation, the new A, B become (ac mod m) and 
(bc + d mod m) respectively. Thus we can reduce the entire sequence of shuffles to a single
LCF.

We can also use powers to apply the same LCF multiple times in a row. Here, with over 10t 
shuffles, we need to use a hack in order to get there, taking advantage of exponentiation
by squaring. This allows us to rapidly compute extremely large powers efficiently.

Recognizing that we are not tracking the position of a single card, but instead are trying
to work out which card lands in a specific position, we have to reverse our shuffle function
before raising it to the power of the iteration count.

We can do this as:
    a_inverse = modular multiplicative inverse (a)
    b_inverse = (-a_inverse * b) % m
where m is the deck size. Note that in Python we can get the modular multiplicative inverse
by using pow(a, -1, m), using the optional third modulo argument of the pow() function.

Having done this, the problem of shuffling a 100+ trillion card deck 100+ trillion times 
resolves to a single LCF, which can be applied on the desired index value (2020) to get
the answer efficiently
''' 
import re
import math
import numpy as np

def main():
    with open('day22/22-1-input.txt', 'r') as open_file:
        input_data = open_file.read()

    ds = 119315717514047
    iterations = 101741582076661
    x = 2020
    
    instructions = input_data.split('\n')
    shuffle_function = (1, 0)  # identity LCF
    for instruction in instructions:
        n = re.search(r'(\-?[0-9]+)', instruction)
        if n is None:
            # STACK
            shuffle_function = mod_combine(shuffle_function, (-1, -1), ds)
        else:
            n = int(n[0])
            if re.match(r'deal with increment', instruction) is not None:
                # DEAL                   
                shuffle_function = mod_combine(shuffle_function, (n, 0), ds)
            elif re.match(r'cut', instruction) is not None:
                # CUT
                shuffle_function = mod_combine(shuffle_function, (1, -n), ds) 
    
    
    a, b = shuffle_function    
    
    # invert the LCM
    inv_a = pow(a, -1, ds)
    inv_b = (-inv_a * b) % ds

    # use exponentation by squaring to adjust the function to work over 10t times
    inverse_function = pow_compose((inv_a, inv_b), iterations, ds)
    a, b = inverse_function

    # apply LCM to the index we are looking for (x)    
    print((a * x + b) % ds)


# combine 2 LCFs to a single LCF
def mod_combine(f, g, m):
    a, b = f
    c, d = g
    return ((a * c) % m, (b * c + d) % m)


# compose a new LCF that is the equivalent of the previous LCF f to the power of k
def pow_compose(f, k, m):
    g = (1, 0)
    while k > 0:
        if k % 2 != 0:
            g = mod_combine(g, f, m)
        k = math.floor(k / 2)
        f = mod_combine(f, f, m)
    return g                    


if __name__ == "__main__":
    main()