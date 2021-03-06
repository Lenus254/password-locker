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

    def test_delete_credentials(self):
        '''
        checks whether delete function is working to remove credentials
        '''
        self.new_credential.save_credentials()
        test_credential = Credentials('facebook', '54321')
        test_credential.save_credentials()
        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.user_credentials), 1)

    def test_display_credentials(self):
        self.assertEqual(Credentials.display_credentials(), Credentials.user_credentials)

    def test_search_credential(self):
        '''
        this test checks whether saved credentials can be searched
        '''
        self.new_credential.save_credentials()
        test_credential = Credentials('facebook', '54321')  # credential
        test_credential.save_credentials()
        found_credentials = Credentials.search_by_site('facebook')
        self.assertEqual(found_credentials.site_name, test_credential.site_name)

    def test_credentials_exists(self):
        '''
        return boolean true if the password searched if found
        '''
        self.new_credential.save_credentials()
        test_credential = Credentials('facebook', '54321')  # new credential
        test_credential.save_credentials()
        site_exist = Credentials.credential_exists('facebook')
        self.assertTrue(site_exist)


if __name__ == '__main__':
    unittest.main()
