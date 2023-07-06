
# 1.1 ======================================
#for user in users:
#    print(user + ', ' + msg)
#    print(f'{user}, {msg}')

# 1.2 ======================================
# messages = []
# for user in users:
#     messages.append(f'{user}, {msg}')

# for message in messages:
#     print(message)

# 1.3 ======================================
# message = [f'{user}, {msg}' for user in users]
# print(message)

# 2.1 ======================================
# messages = []
# for user in users:
#     if user.startswith('a'):
#         messages.append(f'{user}, {msg}')

# for message in messages:
#     print(message)

# 2.2 ======================================
# messages = [f'{user}, {msg}' 
#             for user in users 
#             if user.startswith('a')]

# for message in messages:
#     print(message)

# 3.1 ======================================
# functions

def make_messages(users, msg):
    """
    Make list of the mesagges
    """
    messages = []
    for user in users:
        messages.append(f'{user}, {msg}')
    return messages

def send_messages(messages):
    for message in messages:
        print(message)


# users = ['a.ivanov', 's.petrov', 'a.sidorov']
# msg = 'update your profile'
# messages = make_messages(users, msg)
# send_messages(messages)

msg = 'update your profile'
users = ['a.ivanov', 's.petrov', 'a.sidorov']
msgs = make_messages(users, msg)
send_messages(msgs)

users_2 = ['a.kukuruza', 'v.derevyanko']
msgs_2 = make_messages(msg = 'delete your profile', users = users_2)
send_messages(msgs_2)