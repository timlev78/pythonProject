import re

def check_num(num):
    if re.fullmatch(r'[0-9]*',num):
        #print(num, ": Число корректно")
        return True
    else:
        print("Число некорректно!")
        return False