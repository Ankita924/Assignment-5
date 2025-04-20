my_dict = {'Alice':85, 'Mary':60, 'Mike':76}
name = (input("Enter the student's name: "))
if name in my_dict:
    print(name,"'s marks is:", my_dict[name])
else:
    print('Student not found')
