# write your code here
person={ 'name': 'manal' ,
        'age':43,
        'hobbies':['singing', 'drawing','swiming']
}

print(person.get('name'))
print(person.get('age'))

person['age']=26
person['country']='kuwait'
print(person)

print(len(person))
  
person['hobbies'].append('Dancing')

def check_hobbies(person):
    if len(person['hobbies'])>=3:
     print('WOW YOU ARE AMAZING')

