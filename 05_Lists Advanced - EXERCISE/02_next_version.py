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