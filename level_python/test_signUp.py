
import unittest
from sign_up import SignUp

class Testing(unittest.TestCase):

    def test_set_first(self):
         user = SignUp()
         user.set_firstName("takiii")
         self.assertTrue(user.set_firstName("test"))

    def test_set_last(self):
         user = SignUp()
         user.set_lastName("seqwe")
         self.assertTrue(user.set_firstName("test"))

    
    def test_set_tel(self):
         user = SignUp()
         user.set_phoneNumber(2391)
         self.assertTrue(user.set_phoneNumber(2344))

    
    def test_set_email(self):
         user = SignUp()
         user.set_email("takiii")
         self.assertTrue(user.set_email("test"))
        


if __name__ == '__main__':
    unittest.main()

