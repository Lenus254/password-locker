class User:
    """
    Class that generates new instances of users.
    """

    user_list=[] #Empty list to store users

    def __init__(self,first_name,last_name,user_name,password):

        """instance of a class"""
    
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password

    
    def save_user(self):
        '''
        this is a save function that appends the account to the user_accounts array
        '''
        User.user_list.append(self)

    def delete_user(self):

        '''
        delete_contact method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)  

    @classmethod
    def search_by_user_name(cls, user_name):
        '''
        this is a function tha checks whether the username provided exist and displays a searched user record
        '''
        for user in cls.user_list:
            if user.user_name == user_name:
                return user   

    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  true or false if we cannot find the contact.
        '''

        self.new_user.save_user()
        test_user_account = User("Test","user","0711223344","test@user.com") # new user
        test_contact.save_contact()

        contact_exists = Contact.contact_exist("0711223344")

        self.assertTrue(contact_exists)
