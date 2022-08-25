import re

def email():
    while True:
        userid = input(' Enter UserId/email : ')
        if len(userid) >= 6:
            if userid[0].isalpha():
                if "@" in userid and userid.count("@") == 1:
                    if userid[-5] == "@" or userid[-4] == "@":
                        print(' Enter Valid email/UserId : ')
                        continue
                    else:
                        if userid[-3] == "." or userid[-4] == ".":
                            return userid
        print(' Enter Valid email/UserId : ')
        continue

def passwd():
    while True:
        password = input(' Enter your password : ')
        if len(password) > 5 and len(password) < 16:
            if re.search('[$%&!@#]', password):
                if re.search('[a-z]', password):
                    if re.search('[A-Z]', password):
                        if re.search('[0-9]', password):
                            return password
        print(' Enter valid password : ')
        continue

def data(List):
  option = input(''' To Register press 1 \n To Login press 2 \n To Exit press 3  ''')
  if (option != '1' and option != '2' and option != '3'):
    data()
  if option == '1':
    UserId = email()
    password = passwd()
    L1 = [UserId,password]
    List.append(L1)
    print('Registered successfully!!!')
    data(List)
  elif option == '2':
    UserId = email()
    for i in List:
      if UserId == i[0]:
        password=passwd()
        if password == i[1]:
          print('Logged in successfully!!!')
          break
        else:
          print('wrong password!')
          ch = input('If you want to change the password press 1 ')
          if ch == '1':
            password=passwd()
            i[1]=password
          else:
            data(List)
      else:
        print('UserId/email does not exist.')
        print('Please do registration first to Log in')
        op = input('To register press 1 ')
        if op == 1:
          UserId = email()
          password = passwd()
          List = List.append([UserId,password])
          print('Registered successfully!!!')
        else:
          data(List)
    data(List)
  elif option == '3':
    print('Thank You!!!')

List = []
data(List)