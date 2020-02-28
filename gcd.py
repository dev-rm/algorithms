#Calculate Greatest Common Divisor(gcd) of two numbers using Euclid's algorithm

def gcd(first_num, second_num):
    while(second_num!=0):
        temp = first_num
        first_num = second_num
        second_num = temp % first_num
    return first_num

print(gcd(96,0)) #GCD should be 96
print(gcd(45,38)) #GCD should be 1
print(gcd(12,144)) #GCD should be 12
