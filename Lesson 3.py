# 1 =================================================== 
# nums = []
# for i in range(10):
#     nums.append(i)
# print(nums)

# 2 ===================================================
# nums = []
# nums = [i for i in range(10)]
# print (nums)

# 3 ===================================================
# squares_map = {
# i: i ** 2
# for i in range(2,10) 
# }
# print(squares_map)

# 4 ===================================================
# def make_squares(range_num):
#     print('Start making squares with', range_num)
#     for i in range(range_num):
#         print ('+ process num', i)
#         yield i ** 2


# make_squares()

# 5 ===================================================
# emails = ['Anton.Kukuruza@gmail.com', 'NosovaMarina@gpn.com']
# for email in emails:
#     email = email.lower()
#     print(email)

# 6 ===================================================
emails = ['Anton.Kukuruza@gmail.com', 'NosovaMarina@gpn.com']
def check_domains(emails):
    for email in emails:
        name, _, domain = email.partition('@')
        print(domain)

check_domains(email.lower() for email in emails)    