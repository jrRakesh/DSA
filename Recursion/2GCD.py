# Greatest Common Divisor
def GCD(a, b):
    if(b == 0):
        return a
    else:
        return GCD(b, a%b)

a, b = map(int, input("Enter two numbers: ").split())
result = GCD(a, b)
print(f"The GCD of {a} and {b} is {result}")


"""
    Euclidian Algorithm
    GCD(a, b)
        if(b == 0)
            return a;
        else{
            while(b! = 0){
                r = a % b
                a = b
                b = r
            }
            return a;
        }
"""