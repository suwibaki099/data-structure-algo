user1 = {
    'name': 'Sorna',
    'valid': True
}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        if user1['valid']:
            return fn(*args, **kwargs)
        else:
            return print('Invalid User!!')

    return wrapper


@authenticated
def message_friends(user):
    name = user['name']
    print(f'{name}, message has been sent')


message_friends(user1)
