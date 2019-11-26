start,end = [int(x) for x in input('Enter the start and end numbers: ').split()]

# op_list = []
# for i in range(start,end):
#     if i%2 != 0:
#         x=str(i)
#         if x==x[::-1]:
#             op_list.append(int(x))
                  
my_list = [x for x in range(start,end) if x%2!=0 if str(x)==str(x)[::-1]]
print(my_list)
