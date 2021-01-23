from vars import *
import sys
sys.path.append("Functions")
import opr_function
import login_function
print("---------------------------------------------Welcome----------------------------------------------")
login_function.login()
for i in range(0,1000):
    if i !=0:
        print("1. Add a user\n"
        "2. Delete a user\n"
        "3. Check book status\n"
        "4. Check full database\n")
    if i == 0:
        print("")
    opr = int(input("Select on of the above!\n"))
    if opr==1:
        from opr_function import add_user
        opr_function.add_user()
    elif opr==2:
        opr_function.del_user()
    elif opr==3:
        opr_function.book_status()
    elif opr==4:
        opr_function.database()
    else:
        print("Select only from the four available options")
