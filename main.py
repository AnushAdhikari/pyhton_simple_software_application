import numbervalidation
import reverse
import conversion 
import calculation
def GreetingAtBeginning():
    print("<====================**WELCOME TO THE APPLICATION**====================>")
GreetingAtBeginning()

def to_check_the_number():
    while True:
        number=int(numbervalidation.number_validation())
        if (number>0 and number<256):
            break
        else:
            print(("\n")*1)
            print("*****ERROR!!!!*****")
            print("*****PLEASE ENTER NUMBERS BETWEEN 0-256 ONLY*****")
            print(("\n")*1)
            continue
    return number
def main_method():
    while True:
        print(("\n")*1)
        firstNum=to_check_the_number()
        print("Entered first number =",firstNum,)
        print(("\n")*1)
        binary_firstnum=conversion.conversion(firstNum)
        actual_first_binary=reverse.reverse(binary_firstnum)
        print("The list of converted binary number =",actual_first_binary[0])
        print(("\n")*1)
        print("The converted binary number =",actual_first_binary[1])
        print(("\n")*1)
        secondNum=to_check_the_number()
        print("Entered second number =",secondNum)
        print(("\n")*1)
        binary_secondNum=conversion.conversion(secondNum)
        actual_second_binary=reverse.reverse(binary_secondNum)
        print("The list of converted binary number =",actual_second_binary[0])
        print(("\n")*1)
        print("The converted binary number i =",actual_second_binary[1])
        print(("\n")*1)
        reversed_result=calculation.calculate_result(actual_first_binary[0],actual_second_binary[0])
        actual_result=reverse.reverse(reversed_result)
        print("The sum of numbers represented in the binary number list =",actual_result[0])
        print(("\n")*1)
        print("===>The sum of the binary number =",actual_result[1])
        print(("\n")*1)
        continuos=input("Do you wish to continue ?(Y?N)")
        if continuos.upper()=="Y":
            continue
        else:
            break

if __name__=='__main__':
    main_method()
print(("\n")*1)
def GreetingAtEnd():
    print("<====================**THANK YOU FOR USING THE APPLICATION**====================>")

GreetingAtEnd()

