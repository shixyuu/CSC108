def double (num:float) -> float:
    return (num*2)

def our_maximum (num1:float, num2: float) -> float:
    ndt=max(num1,num2)
    return (ndt)

def max_of_min (num1:float, num2:float, value1:float, value2:float) -> float:
    comp_num = min(num1,num2)
    comp_val = min(value1,value2)
    comp_max = max(comp_num,comp_val)
    return (comp_max)


print (double(7.0))
print (our_maximum(1.5,2.5))
print (max_of_min(4.0,3.7,6.0,3.5))
print (max_of_min(1.0,1.7,4.5,3.0))