multi_type_list = ["hi",12,13.99,"bye"]
print(multi_type_list)

for x in range(0,len(multi_type_list)):
 a=type(multi_type_list[x]) is float
 b=type(multi_type_list[x]) is int
 c=type(multi_type_list[x]) is str
 if a:
    print(multi_type_list[x]+1);
 if b:
    print(multi_type_list[x]+1);
 if c:
    print(multi_type_list[x].upper());