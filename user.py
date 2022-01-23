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