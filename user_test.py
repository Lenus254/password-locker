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

    def test_save_multiple_users(self):
        '''
        test function to acertain if one can save multiple users to user list
        '''
        self.new_user.save_user()
        test_user_account = User('er', 'ro', 'ro@ro', '2345')
        test_user_account.save_user()
        self.assertEqual(len(User.user_list), 2)

    def test_delete_user(self):
        '''
        test that check if the delete function works
        '''
        self.new_user.save_user()
        test_user_account = User('er', 'ro', 'ro@ro', '2345')
        test_user_account.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 1)

    def test_search_account_by_username(self):
        '''
        test to check whether the function used to find accounts really works
        '''
        self.new_user.save_user()
        test_user_account = User('er', 'ro', 'ro@ro', '2345')
        test_user_account.save_user()
        found_user = User.search_by_user_name('ro@ro')
        self.assertEqual(found_user.user_name, test_user_account.user_name)

if __name__ == '__main__':
    unittest.main()
