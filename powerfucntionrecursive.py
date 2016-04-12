import powerfunction




def int_input(question):
    
    answer = raw_input(question)
    
    
    try:
        answer = int(answer)
        return answer
    
    except ValueError:
        return int_input("Thats not an integer try again:")
    
    
def float_input(question):
    
    answer = raw_input(question)
    
    
    try:
        answer = float(answer)
        return answer
    
    except ValueError:
        return float_input("Thats not an number try again:")
    
    



base = float_input("Give me a number:")

exponent = int_input("Give me an exponent:")


answer = powerfunction.power(base,exponent)

print("The answer is {}".format(answer))


