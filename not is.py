def is_group_member(group_data,n):
   for value in group_data:
       if n== value:
          return True
   return False
a=input("enter the group")
b=input("enter the group_member")
print (is_group_member(a,b))
