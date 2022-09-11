# Exercise in capturing inputs and playing it back
username: str = input('whats is your username?')
password = input ('please enter your password: ')

password_length = len(password)
hidden_password = password_length * '*'

print(f'hey {username}, your password {hidden_password} is {(password_length)} characters long')