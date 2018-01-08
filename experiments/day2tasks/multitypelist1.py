multi_type_list = ["hi",12,13.99,"bye"]
print(multi_type_list)

for x in multi_type_list:

 if isinstance(x,str):
    print(x.upper());
 if isinstance(x,float):
    print(x+1);
 if isinstance(x,int):
    print(x+1);
 