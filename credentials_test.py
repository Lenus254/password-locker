from credentials import Credentials
import unittest

user_credentials = []

class TestCredentials(unittest.TestCase):

    def tearDown(self):
        '''
        this test clears the credentialss list after every test
        '''
        Credentials.user_credentials = []

    def setUp(self):
        '''
        this test creates a new instance of the credential class
        before each test
        '''
        self.new_credential = Credentials('twitter', '4321')

    def test_init(self):
        '''
        this test checks whether the data enterd into the properties if called wll appear
        '''
        self.assertEqual(self.new_credential.site_name, 'twitter')
        self.assertEqual(self.new_credential.password, '4321')

    def test_save_credential(self):
        '''
        this is a test to check whether the credentials are appended to the credential list
        '''
        self.new_credential.save_credentials()
        self.assertEqual(len(Credentials.user_credentials), 1)

    def test_save_multiple(self):
        '''
        Test function to test whetther several credentials can be appended to credentials list
        '''
        self.new_credential.save_credentials()
        test_credential = Credentials('facebook', '54321')
        test_credential.save_credentials()
        self.assertEqual(len(Credentials.user_credentials), 2)


if __name__ == '__main__':
    unittest.main()
