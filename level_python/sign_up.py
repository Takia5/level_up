class SignUp:
    def __init__(self):
        self.f_name = self.add_first_name()
        self.l_name = self.add_last_name()
        self.tel = self.add_tel()
        self.email = self.add_email()
        self.password = self.add_password()
        
        
    def add_first_name(self):
       
        while True:
              try:
                  fName = input('Enter your first name')
              except ValueError:
                  print("Sorry!")
                  continue

              if not fName:
                  print("Sorry, you must enter your first name!")
                  continue
              elif not fName.isalpha():                
                  print ("Please enter a valid name!")
                  continue
              else:
                  break
                              
        return fName.capitalize()

    def add_last_name(self):
       
        while True:
              try:
                  lName = input('Enter your last name')
              except ValueError:
                  print("Sorry!")
                  continue

              if not lName:
                  print("Sorry!")
                  continue
              elif not lName.isalpha():                
                  print ("Please enter a valid name!")
                  continue
              else:
                  break
        return lName

    def add_tel(self):
        
        while True:
              try:
                  telephone = input('Enter your phone number')
              except ValueError:
                  print("Sorry!")
                  continue

              if not telephone:
                  print("Sorry, enter a valid a valid telephone number!")
                  continue
              
              else:
                  break
        return telephone

    def add_email(self):
       
        while True:
              try:
                   email = input('Enter your email')
              except ValueError:
                  print("Sorry!")
                  continue

              if not email:
                  print("Sorry, you must enter your email!")
                  continue
              else:
                  break
        return email

    def add_password(self):
        
        while True:
              try:
                   pswd = input('Enter your password')
              except ValueError:
                  print("Sorry!")
                  continue

              if not pswd:
                  print("Sorry, you must enter your password!")
                  continue
              else:
                  break
        return pswd
       

    def sign_up(self):
        print("You have successfully registered!")

sign = SignUp()
sign.sign_up()