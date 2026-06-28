countries = ['india','pakistan','bangladesh','nepal','srilanka']

print(countries)
print(countries[0])
print(countries[2] [1] )
print(countries [1:3] )
print(countries[1:])
print(type(countries))

countries[1] = 'saudi'
print(countries)
print(countries[-1])
print(countries[-3])

data = [ 'usa' , True , 20, 'uk']
print(data)

data2 = list(('india',False , 65 ,'nepal'))
print(data2)
print(type(data))
print(type(data2))

list1 = [1,2,3,4,5]
list2 = ['banana','apple','mango','oranges']
list1.extend(list2)
print(list1)
list2.append('cherry')
print(list2)
list2.insert(1,'rahman')
print(list2)
list2.remove('banana')
print(list2)
print(list2.index('mango'))
list2.clear()
print(list2)