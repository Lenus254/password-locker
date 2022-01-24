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
