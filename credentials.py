class Credentials:
    def __init__(self, site_name, password):
        self.site_name = site_name
        self.password = password

    user_credentials = []

class TestCredentials(unittest.TestCase):