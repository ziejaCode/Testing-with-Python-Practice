import random





def get_code():    
    rand_int = random.randint(3, 19)
    return f'CX-{rand_int}'


print(get_code()) # test