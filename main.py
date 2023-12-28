from config import People

person = People(sex='w', age=[18, 25], payment_system='visa')
print(person.generate())
