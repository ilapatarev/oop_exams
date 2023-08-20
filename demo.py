# value="85232323"
# valid_phone=True
# for i in range(len(value)):
# 	if not value[i].isdigit():
# 		valid_phone=False
#
# if value[0]!=0 and len(value)!=10:
# 	valid_phone=False
#
# if not valid_phone:
# 	raise ValueError("Invalid phone number!")

value="   "
a=all([value[x]==' ' for  x in range(len(value))])
print(a)

