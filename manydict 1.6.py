the_dict = {'Kirill':2000,'Oleg':2001,'Sancho':1900}
print(the_dict)
print(the_dict['Kirill'])
print(the_dict.get('Sasha', 'Без ошибки'))
the_dict.update({'Misha':1999,
                 'Larisa':2000})
print(the_dict)
del the_dict ['Oleg']
print(the_dict)

my_set = {1, 2, 3, 'Kirill', True, 2.1, 1, 2, 3, 'Kirill', True, 2.1}
print(my_set)
my_set.discard(2)
my_set.remove('Kirill')
print(my_set)
my_set.add(5)
my_set.add(3.5)
print(my_set)