from collections import defaultdict

'''
This one is another one where the challenge is working out what the tablet instructions
are actually executing, and then quickly doing it in a more efficient way. 

This program takes two values in registers b and c, and searches through them at a specified
jump (from instruction 31, the jump here is 17). For each number, it *exhaustively* tests whether
that number is prime, performing every possible multiplication on a grid of size n where n is the number.
If the number is not prime, one is added to the total.

In sum then, we can solve it by finding all non-primes between 108,100 and 125,100, stepping in multiples
of 17. The search space is 1,001 numbers total (in the code, the upper bound is the lower bound + 17,000).

Of note is that the 1 added to register 'a' does not change the function of the program, but rather skips what
otherwise would have been a jump and dramatically increases the values of b and c, making it impractical to run
naively.
'''

def main():
    lower_bound = 108100
    upper_bound = 125100
    prime_c = 0
    primes = []
    for i in range(lower_bound, upper_bound + 1, 17):
        prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                prime = False
                break
        if prime:
            prime_c += 1
            primes.append(i)
    
    print(1001 - len(primes))

if __name__ == '__main__':
    main()