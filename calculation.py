def AND_Gate(upperBit,lowerBit):
    if upperBit==1 and lowerBit==1:
        return 1
    else:
        return 0
def OR_Gate(upperBit,lowerBit):
    if upperBit==1:
        return 1
    elif lowerBit==1:
        return 1
    else:
        return 0
def Complimentgate(bit):
    if bit==0:
        return 1
    elif bit==1:
        return 0
'''ef AND_Gate(upperBit,lowerBit):
    return upperBit & lowerBit
def OR_Gate(upperBit,lowerBit):
    return upperBit | lowerBit
def Complimentgate(bit):
    return ~bit'''
def XOR_Gate(upperBit,lowerBit):
    a=AND_Gate(Complimentgate(upperBit),lowerBit)
    b=AND_Gate(upperBit,Complimentgate(lowerBit))
    c=OR_Gate(a,b)
    return int(c)
def to_carry(upperBit,lowerBit,carry):
    p=XOR_Gate(upperBit,lowerBit)
    q=AND_Gate(upperBit,lowerBit)
    r=AND_Gate(carry,p)
    s=OR_Gate(r,q)
    return int(s)
def calculate_result(upperBit,lowerBit):
    result=[]
    carry=0
    upperBit.reverse()
    lowerBit.reverse()
    for i in range(len(upperBit)):
        sum1=XOR_Gate(upperBit[i],lowerBit[i])
        result.append(XOR_Gate(sum1,carry))
        carry=to_carry(upperBit[i],lowerBit[i],carry)
    return result
