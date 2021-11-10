def check_password(username, password, min_length = 8, check_username=True):
    if len(password)<8:
        print('password is to short')
        return False
    elif check_username and username in password:
        print('password contains username')
        return False
    else:
        print(f'password for user {username} has passed all checks')
        return True



def add_user_to_file(user, users_filename='users.txt'):
    while True:
        password = input(f'Enter password for user {user}: ')
        if check_password(user, password):
            break
    with open(users_filename, 'a') as f:
        f.write(f'{user},{password}\n')

username = input('enter username: ')
add_user_to_file("vlado")
