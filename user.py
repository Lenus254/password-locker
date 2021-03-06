from ast import If


class User:
    """
    Class that generates new instances of users.
    """

    user_list = []  # Empty list to store users

    def __init__(self, first_name, last_name, user_name, password):
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

    @classmethod
    def user_exist(cls, user_name):
        '''
        Method that checks if a user exists from the user list.
        Args:
            user_name:  to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.user_name == user_name:
                    return True

        return False

    @classmethod
    def check_user(cls, first_name, password):
        current_user = ''
        for user in User.user_list:
            if(user.first_name == first_name and user.password == password):
                current_user = user.first_name
                return current_user

    @classmethod
    def display_users(cls):
        return cls.user_list


    