# validation for commonly used passwords in Registration & Password changing time

import string
import time
start_time = time.process_time()
try:
    password = input("Enter the password : ")
    with open('rockyou.txt' , encoding='latin-1') as pswd :
        common = pswd.read().splitlines()
    if password in common:
        print("This Password is in commonly used passwords....")
        # exit()
    else:
        print("This password is PASS commonly used password TEST")
except Exception as e: 
    print("Some error occured! \n",e)
    pass
print("--- %s seconds ---" % (time.process_time() - start_time))