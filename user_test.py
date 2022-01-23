import unittest # Importing the unittest module
from user import User # Importing the User class
# import pyperclip

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the User class behaviours.
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("linus","lin","lin@lin","12345") # create user object

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []



    def test_init(self):
        '''
        test_init test case to test if the user object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"linus")
        self.assertEqual(self.new_user.last_name,"lin")
        self.assertEqual(self.new_user.user_name,"lin@lin")
        self.assertEqual(self.new_user.password,"12345")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the use_list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)

    # def test_save_multiple_users(self):
    #     '''
    #     a test that checks whether both values appended to the array are actually present\ and returns the acount itself
    #     '''
    #     self.new_user.save_account()
    #     test_userAc = User('er', 'ro', 'ro@ro', '234')
    #     test_userAc.save_account()
    #     self.assertEqual(len(User.user_list), 2)


if __name__ == '__main__':
    unittest.main()
