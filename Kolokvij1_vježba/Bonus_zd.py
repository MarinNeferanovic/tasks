# pokušaji ispočetka:
# count = 10
# a = 9
# for i in range(10):
#     for count in range(10):
#         print("-", end="")
#         if count == a:
#             print("*", end="")
#         a -= 1
#     print()

# moguće riješiti u dvije linije koda:
for a in range(9, -1, -1):
    print("-" * a + "*" + "-" * (9 - a))

# A obrnuto na isti način:

### for a in range(10): ###
###     print("-" * a + "*" + "-" * (9 - a)) ###
