def power(base,exponent):
    
    """Excepts base and exponent and returns final answer"""
    
      
    if exponent == 0:
        return 1

    total = base * power(base, exponent - 1)
    
  
    
    return total