import re

def email():
    while True:
        UserId = input('Enter Email/UserId : ')
        if UserId[0].isalpha():
            if '@' in UserId and UserId.count('@') == 1:
                if UserId.endswith('.com') or UserId.endswith('.in'):
                    if UserId.index('@')+1 != UserId.rfind('.'):
                        return UserId
        print('Enter correct Email/UserId!!! ')
        continue

def passwd():
    while True:
        password = input('Enter Password :')
        if len(password) > 5 and len(password) < 16:
            if re.search('[a-z]', password):
                if re.search('[A-Z]', password):
                    if re.search('[0-9]', password):
                        if re.search('[!@#$%&*~]', password):
                            return password
        print('Enter valid password!!! ')
        continue
def data():
    global user_data
    global passwd_data
    user_data = []
    passwd_data = []

def register():
    UserId = email()
    password = passwd()
    user_data.append(UserId)
    passwd_data.append(password)
    print('You have successfully Registered...')
    op()

def login():
    global j
    UserId = email()
    for i in user_data:
        if i == UserId:
            j = i
            password = passwd()
            if password == passwd_data[user_data.index(i)]:
                print('You have successfully Logged in...')
                op()
            else:
                print('You have entered wrong password!!!')
                reset()
        else:
            continue
    print("Your credentials doesn't exist!!!")
    op()

def reset():
    choice = input('''Choose an option :
    To change the password  Press 1 
    To go to Main menu      Press 2 
    To Exit                 Press 3''')
    if choice == '1':
        print('Please enter new password.')
        password = passwd()
        passwd_data[user_data.index[j]] = password
        print('You have successfully changed the password...')
        op()
    elif choice == '2':
        op()
    elif choice == '3':
        exit()
    else:
        print('Enter number 1/2/3 only...')
        reset()

def op():
    option = input('''Please choose any One :
    For Registration   press 1 
    For Login          press 2 
    To Exit            press 3 ''')
    if option == '1':
        register()
    elif option == '2':
        login()
    elif option == '3':
        exit()
    else:
        print('Enter number 1/2/3 only...')
        op()

def exit():
    print('Thank you!!!')

data()
op()
