#!/usr/bin/env python3.9
from ast import Break
from signal import siginterrupt
from user import User
from credentials import Credentials

def create_user(first_name, last_name, user_name, password):
    users = User(first_name, last_name, user_name, password)
    return users

def save_users(user):
    user.save_user()

def search_users(user_name):
    return User.search_by_user_name(user_name)

def delete_users(user):
    user.delete_user()

def isexist_user(user_name):
    return User.user_exist(user_name)

def display_users():
    return User.display_users()

def create_credentials(site_name, password):
    credentials = Credentials(site_name, password)
    return credentials

def save_site(credentials):
    credentials.save_credentials()

def search_site(site_name):
    return Credentials.search_by_site(site_name)

def credentials_exists(site_name):
    return Credentials.credential_exists(site_name)

def display_credentials():
    return Credentials.display_credentials()

def delete_credentials(credentials):
    credentials.delete_credentials()

def confirm_user(first_name,password):
	'''
	Function that verifies the existance of the user before creating credentials
	'''
	c = User.check_user(first_name,password)
	return c

def main():
    # print('SITES PASSWORD MANAGER')
    print('Select from letters below for corresponding actions:')
    while True:

        print(" b) LOGIN \n a) CREATE ACCOUNT \n c) ABOUT SITE \n d) DISPLAY USERS \n e) LOGOUT")

        option = str(input())
        if option == 'a':
            print('NEW ACCOUNT')
            print('-'*60)

            print('FIRSTNAME')
            first_name = input()

            print('LASTNAME')
            last_name = input()

            print('USERNAME')
            user_name = input()

            print('PASSWORD')
            password = input()

            save_users(create_user(
                first_name, last_name, user_name, password))
            # create and save a new user
            print('User created succesfully')
            
        elif option =='b':
            print('Enter username')
            username = input()
            print('Enter passoword')
            password = input()
            user = confirm_user(first_name,password)
            if user == username:

                print('User logged in ')
            else:
                print('Invalid user credentials')
                # break
                
                while True:

                    print(
                        f'Welcome {username}, Use the following numbers to select their corresponding options')

                    print(
                        ' 1) Save new credential \n 2) Delete credential \n 3) Display saved credentials \n 4) check out ')

                    login_option = int(input())
                    if login_option == 1:
                        print('New credential')
                        print('-'*80)

                        print(' Enter site name')
                        site_name = input()

                        print('Enter password')
                        password = input()

                    
                        save_site(create_credentials(site_name, password))

                    elif login_option == 2:
                        print("Enter the name of the site you want to delete")

                        site_name = input()
                        if credentials_exists(site_name):
                            remove_site = (site_name)
                            delete_credentials(remove_site)

                        else:
                            print(f' {site_name} not found')

                    elif login_option == 3:
                        if display_credentials():
                            for user in display_credentials():
                                print(
                                    f'{user.site_name}:{user.password}'
                                )
                        else:
                            print('You have no credentials so far')
                            print('\n')

                    elif login_option == 4:
                        print('no credentials to display')
                        break
            
        
        elif option == 'c':
            print('ABOUT THE SITE')
            print(
                '''
            Passlock is a terminal application that allows a user  credentials from different sites. In case of many sites like social media and others , passlock can be used to save different login credentials from the social media  accounts and other sites.Instead of having to gram credentials for all your sites so that you can remember  easily,you can use different login credentials and save them in passlock and only have to remember your passlock user account details only. This can prove to be very helpful especially  if you have many accounts.
                ''')

        elif option == 'd':
            if display_users():
                for user in display_users():
                    print(
                        f'{user.user_name}'
                    )
            else:
                print('NO ACCOUNTS')

        elif option == 'e':
            print('EXIT')
            break


if __name__ == '__main__':
    main()

