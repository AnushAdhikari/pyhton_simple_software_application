def number_validation():
    while True:
        try:
            print(("\n")*1)
            num=int(input("Enter a number:")) 
            print("=========================================") 
        except ValueError:
            print(("\n")*1)
            print("*****ERROR!!!!*****")
            print("PLEASE ENTER NUMBERS ONLY")
            continue
        else:
            break
    return num


    
    

