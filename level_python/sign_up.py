
class SignUp:
    name = "str"
    email = "email"
    tel = 345234
    password="qweqwe"

    def set_firstName(self, first_name):
        while True:
              try:
                  self.name=first_name
                 
              except ValueError:
                  print("Sorry!")
                  continue

              if not self.name:
                  print("Sorry, you must enter your first name!")
                  continue
              elif not self.name.isalpha():                
                  print ("Please enter a valid name!")
                  continue
              else:
                  break
        return self.name

    def set_lastName(self, last_name):

         while True:
              try:
                  self.name=last_name
                 
              except ValueError:
                  print("Sorry!")
                  continue

              if not self.name:
                  print("Sorry, you must enter your last name!")
                  continue
              elif not self.name.isalpha():                
                  print ("Please enter a valid name!")
                  continue
              else:
                  break
        
         return self.name

    def set_phoneNumber(self, tel):
        self.tel= tel
        return self.tel
        
    def set_email(self, email):
        self.email= email
        return self.email

    def set_password(self, pswd):
        self.password= pswd
        return self.password

    def get_name(self):
        print(self.name)
        print(sign_up.name)


if __name__ == '__main__':
    sign_up = SignUp()
    print(sign_up.set_firstName(input("Enter your first name: ")))
    print(sign_up.set_lastName(input("Enter your last name: ")))
    print(sign_up.set_phoneNumber(input("Enter your Telephone Number: ")))
    print(sign_up.set_email(input("Enter your email: ")))
    print(sign_up.set_password(input("Enter your password: ")))
    print ("You have registered successfully!")
    #print('User associated with id 0 is ', person.get_name(0))
