# current_version = list(map(int, input().split('.')))
#
# for num in current_version[::-1]:
#
#     if num < 9:
#         num += 1
#         current_version.pop(2)
#         current_version.append(num)
#         break
#     elif num == 9:
#         num == 0
#         if num < 9:
#             num += 1
#             current_version.pop(1)
#             current_version.append(num)
#             break
#         elif num == 9:
#             num == 0
#             num += 1
#             current_version.pop(0)
#             current_version.append(num)
#             break
#
# print(current_version)

current_version = input().split('.')

old_version_string = ""     #defining epmty variable for current version as whole number
new_version_string = 0      #defining empty variable for new version as whole number


for digit in current_version:
    old_version_string += digit     #creating old version as string (whole number) to ensure 9 is the largest digit

new_version = str(int(old_version_string) + 1)      #adding one version

print(f"{new_version[0]}.{new_version[1]}.{new_version[2]}")        #printing the new one separated with dots
