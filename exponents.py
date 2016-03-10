def power(base,exponent):
    
    """Excepts base and exponent and returns final answer"""
     
    adder = 1
    final = base
    
    
    if exponent == 0:
        return 1
    
    while adder < exponent:
        final = final * base
        adder = adder + 1
    
    return final



base = int(raw_input("Give me a number:"))

exponent = int(raw_input("Give me an exponent:"))


answer = power(base,exponent)

print("The answer is {}".format(answer))
   