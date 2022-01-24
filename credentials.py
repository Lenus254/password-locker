class Credentials:
    def __init__(self, site_name, password):
        self.site_name = site_name
        self.password = password

    user_credentials = []

    def save_credentials(self):
        Credentials.user_credentials.append(self)

    def delete_credentials(self):
        Credentials.user_credentials.remove(self)

    @classmethod
    def display_credentials(cls):
        return cls.user_credentials

    @classmethod
    def search_by_site(cls, site_name):
        for site in cls.user_credentials:
            if site.site_name == site_name:
                return site

    @classmethod
    def credential_exists(cls, site_name):
        for site in cls.user_credentials:
            if site.site_name == site_name:
                return site
        return False
