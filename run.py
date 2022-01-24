#!/usr/bin/env python3.9
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

def main():
    # print('WELCOME TO PASSLOCK')
    print('Use the following numbers to pick their corresponding values')
    while True:

        print(" 1) LOGIN \n 2) SIGN UP \n 3) ABOUT PASSLOCK \n 4) DISPLAY ACCOUNTS \n 5) SIGN OUT")

        choice = int(input())
        if choice == 1:
            print('Enter username')
            username = input()
            print('Enter passoword')
            password = input()
            account = find_accounts(username)
            if account.user_name == username and account.password == password:

                print('logged in ')
                while True:

                    print(
                        f'Welcome {username}, Use the following numbers to select their corresponding          values')

                    print(
                        ' 1) Save new password \n 2) Delete password \n 3) Display saved passwords \n 4) Log out ')

                    log_choice = int(input())
                    if log_choice == 1:
                        print('New page')
                        print('*'*100)

                        print('Page name')
                        page = input()

                        print('password')
                        password = input()

                    # created and saved page
                        save_page(create_page(page, password))

                    elif log_choice == 2:
                        print("Enter the name of the page you want to delete")

                        page = input()
                        if isexist_page(page):
                            remove_page = (page)
                            delete_page(remove_page)

                        else:
                            print(f'I cant find {page}')

                    elif log_choice == 3:
                        if display_pages():
                            for pag in display_pages():
                                print(
                                    f'{pag.page}:{pag.password}'
                                )
                        else:
                            print('NO PASSWORD SAVED YET')
                            print('\n')

                    elif log_choice == 4:
                        print('adios')
                        break
            else:
                print('wrong credentials')

        if choice == 2:
            print('NEW ACCOUNT')
            print('*'*100)

            print('FIRSTNAME')
            first_name = input()

            print('LASTNAME')
            last_name = input()

            print('USERNAME')
            user_name = input()

            print('PASSWORD')
            password = input()

            save_account(create_account(
                first_name, last_name, user_name, password))
            # create and save a new account
            print('ACCOUNT CREATED')
            while True:

                print(
                    f'Welcome {user_name}, Use the following numbers to select their corresponding values')
                print(
                    ' 1) Save new password \n 2) Delete password \n 3) Display saved passwords \n 4) Log out ')

                log_choice = int(input())
                if log_choice == 1:
                    print('New page')
                    print('*'*100)

                    print('Page name')
                    page = input()

                    print('password')
                    password = input()

                    # created and saved page
                    save_page(create_page(page, password))

                elif log_choice == 2:
                    print("Enter the name of the page you want to delete")

                    page = input()
                    if isexist_page(page):
                        remove_page = (page)
                        delete_page(remove_page)

                    else:
                        print(f'I cant find {page}')

                elif log_choice == 3:
                    if display_pages():
                        for pag in display_pages():
                            print(
                                f'{pag.page}:{pag.password}'
                            )
                    else:
                        print('NO PASSWORD SAVED YET')

                elif log_choice == 4:
                    break

        elif choice == 3:
            print('ABOUT PASSLOCK')
            print(
                '''
            Passlock is an sort of script application that allows you to store  password from different ccounts. In case of many accounts on social media passlock can be used to store the different password from the social media  accounts.Instead of having to use one password for all your sites so that you can remember  easily,you can use different password and store them in passlock and only have to remember your passlock password. This can prove to be very helpful especially  against hackers.
                                    ''')

        elif choice == 4:
            if display_accounts():
                for account in display_accounts():
                    print(
                        f'{account.user_name}'
                    )
            else:
                print('NO ACCOUNTS')

        elif choice == 5:
            print('adios')
            break


if __name__ == '__main__':
    main()

