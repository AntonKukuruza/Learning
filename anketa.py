users = ['a.ivanov', 's.petrov', 'v.sidorov']
msg = 'update your profile'

# 1 ======================================
#for user in users:
#    print(user + ', ' + msg)
#    print(f'{user}, {msg}')

# 2 ======================================
# messages = []
# for user in users:
#     messages.append(f'{user}, {msg}')

# for message in messages:
#     print(message)

# 3 ======================================
message = [f'{user}, {msg}' for user in users]
print(message)