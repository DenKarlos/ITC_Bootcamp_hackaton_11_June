from stdiomask import getpass
from datetime import datetime

class Logger:
    def __init__(self):
        self.login = ''
        self.password = ''

    def to_log(self):
        self.login = input('Input login (> 5 symbols) -> ')
        if len(self.login) < 5:
            print('Login is too short. It should be more than 5 symbols.')
            self.login = ''
        else:
            self._passwording()
    
    def _passwording(self):
        while len(self.password) < 8:
            self.password = getpass('Input password (> 7 symbols) -> ')
        if self._chek_password():
            self._log_to_file()
            self._log_time()
        else:
            print('Password have failed verification!!!')

    def _chek_password(self):
        chek = getpass('Repeat your password -> ')
        if chek == self.password:
            return True
        else:
            return False
    
    def _log_to_file(self, filename='users.txt'):
        with open(filename,'a') as fl:
            print(f'Login: {self.login} - Password: {self.password}', file=fl)

    def _log_time(self, filename='log.txt'):
        with open(filename,'a') as fl:
            time = datetime.time(datetime.now())
            print(f'User registered successfully {time}', file=fl)



sim_log = Logger()
sim_log.to_log()


