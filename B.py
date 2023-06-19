# flag_inc = True
# flag_dec = True
# flag_const = True
# flag_eq = False
# n = int(input())
# while n != -2e9:
#     m = int(input())
#     if m != -2e9:
#         if n > m:
#             flag_inc = False
#             flag_const = False
#         elif n < m:
#             flag_dec = False
#             flag_const = False
#         elif n == m:
#             flag_eq = True
#     n = m

# if flag_const:
#     print("CONSTANT")
# elif flag_dec and flag_eq:
#     print("WEAKLY DESCENDING")
# elif flag_inc and flag_eq:
#     print("WEAKLY ASCENDING")
# elif flag_inc:
#     print("ASCENDING")
# elif flag_dec:
#     print("DESCENDING")
# else:
#     print("RANDOM")

def f():
    return 1, 2, 3


a, b, c = f()
print(a, b, c)