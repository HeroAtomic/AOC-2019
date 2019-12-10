input = '172930-683082'
input = input.split('-')

start = int(input[0])
stop = int(input[1])

print('Start:', start)
print('Stop:', stop)

valid_passwords = []

print('Checking...')

def possible_passwords():
    for i in range (start, stop):
        i = str(i)
        if i[0] == i[1] or i[1] == i[2] or i[2] == i[3] or i[3] == i[4] or i[4] == i[5]:
            if i[0] <= i[1] and i[1] <= i[2] and i[2] <= i[3] and i[3] <= i[4] and i[4] <= i[5]:
                valid_passwords.append(i)
            else:
                pass
        else:
            pass
    return valid_passwords

valid_passwords = possible_passwords()
print('Number of valid passwords:', len(valid_passwords))