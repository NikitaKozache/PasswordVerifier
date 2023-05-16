passwordtrue= 2233
logintrue='artem@gmail'

i = 0


while i < 3:
    password= int(input('input your password: '))
    login= str(input("input your login: "))
    if password== passwordtrue and login == logintrue :
        print(" welocome ")
        break
    else:
        print(' password or login is wrong ')
    i += 1
