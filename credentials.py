class Credentials:
    def __init__(self, site_name, password):
        self.site_name = site_name
        self.password = password

    def save_credentials(self):
        Credentials.user_credentials.append(self)