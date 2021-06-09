
def salt_password(password):
    # For every 2 characters, insert 'hi'
    password_arr = []
    jump_two = 2
    for c in range(len(password)):
        if c == jump_two:
            password_arr.append('+')
            jump_two += 2
        
        password_arr.append(password[c])


    return ''.join(password_arr)
