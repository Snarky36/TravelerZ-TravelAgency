from hashlib import sha256

class SecurityService:
    def __init__(self):
        self.securityKey = 'secretkeyfortravelerz2001'

    def getSecurityKey(self):
        return self.securityKey

    def encodePassword(self, password):
        return sha256(password.encode()).hexdigest()

    def verifyUser(self, user, loginCredentials):
        encodedPassword = self.encodePassword(loginCredentials['password'])
        userPassword = user['password']

        return user['email'] == loginCredentials['email'] and encodedPassword == userPassword


