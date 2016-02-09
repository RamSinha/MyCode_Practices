import math
def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0: 
                return False
        return True
    return False


def get_primes(number):
    while True:
        print 'entering while again with', number
        if is_prime(number):
            print 'first ' + str(number)
            number = yield number
            print 'next ' + str(number)
        number += 1

def print_successive_primes(iterations, base=10):
    print 'entered print_successive_primes'
    prime_generator = get_primes(base)
    print 'generated first time'
    prime_generator.send(None)
    print 'sent value None to generator'
    for power in range(iterations):
        print 'in the last loop sending', base ** power 
        print(prime_generator.send(base ** power))

print_successive_primes(1,10)
"""
entered print_successive_primes
generated first time
entering while again
entering while again
first 11
sent value None to generator
in the last loop sending 1
next 1
entering while again
first 2
2
"""
