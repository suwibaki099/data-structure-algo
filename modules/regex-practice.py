import re

pattern = re.compile(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$")

password = pattern.search('asdw@aa@3223A')

# print(pattern.fullmatch('awdwadwadawd@sA23'))

print(__name__)

# if not password:
#     print('Invalid Password')
