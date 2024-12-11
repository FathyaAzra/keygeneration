from django.shortcuts import render
import random

# Function to check prime using Fermat's Little Theorem
def checkPrimeFermat(p):
    assert p > 2 and p % 2 == 1  # Ensure p is an odd integer greater than 2
    numberOfTrials = len(str(p)) * 3  # Adjust trials based on the size of the number
    for i in range(numberOfTrials):
        a = random.randint(2, p - 1)  # Random base
        if pow(a, p - 1, p) != 1:  # Fermat's Little Theorem
            return False
    return True

# Function to check if p and q are Blum integers
def isBlumInteger(p, q):
    return p % 4 == 3 and q % 4 == 3  # p and q should both be congruent to 3 mod 4

# Function to generate two primes p and q
def generateTwoPrime(bit_length):
    prime_list = []
    lower_bound = 2 ** (bit_length - 1)
    upper_bound = 2 ** bit_length - 1

    while len(prime_list) < 2:
        candidate = random.randint(lower_bound, upper_bound) | 1  # Ensure odd number
        if checkPrimeFermat(candidate) and candidate not in prime_list:
            prime_list.append(candidate)

    p, q = prime_list
    if isBlumInteger(p, q):
        n = p * q  # Calculate n as the product of p and q
        return p, q, n
    else:
        return generateTwoPrime(bit_length)  # Retry if p and q don't satisfy the condition

def keygeneration(request):
    p, q, n = None, None, None  # Initial values for GET requests

    if request.method == "POST":
        # Get the bit length from the form
        bit_length = int(request.POST.get("bit_length"))
        
        # Generate the two primes and n
        p, q, n = generateTwoPrime(bit_length)

    return render(request, 'template/base/keygeneration.html', {'p': p, 'q': q, 'n': n})
