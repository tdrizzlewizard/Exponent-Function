def power(base,exponent):
    
    """Determines final answer"""
     
    adder = 1
    final = base
    
    while adder < exponent:
        final = final * base
        adder = adder + 1
    
    return final



base = int(raw_input("Give me a number:"))

exponent = int(raw_input("Give me an exponent:"))

if exponent == 0:
    print("The answer is 1")
    exit()

answer = power(base,exponent)

print("The answer is {}".format(answer))
   