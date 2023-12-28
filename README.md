<p align="center">
      <img src="https://i.ibb.co/Wyf4BRW/people-generator-for-db.jpg" width="726">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/language-Python-blue?style=flat-square" alt="language">
   <img src="https://img.shields.io/badge/version-1.0.0-blue?style=flat-square" alt="version">
  <img src="https://img.shields.io/badge/License-free_to_use-blue?style=flat-square" alt="license">

</p>

## About

A generator of data about people in Russian for the database.  There are several modes and settings for generating data about people. You can add your own data for generation or, conversely, delete unnecessary data that is used for generation. :dizzy: <br>
The result of the program:
```
{'name': 'Элина', 'surname': 'Быкова', 'patronymic': 'Григориевна', 'sex': 'ж', 'age': 22, 'phone_number': '89451523196', 'phone_number+': '+79451523196', 'en_name': 'Elina', 'en_surname': 'Bykova', 'en_patronymic': 'Grigorievna', 'email': 'bykovaelina@gmail.com', 'birthday': '2001-10-04', 'number_card': '4050340630312383', 'pin': '6583'}  #dict
```
## Documentation

There is already an instance of the people generator in main.py file, you just need to change the instance attributes for more accurate generation.

```python
person = People(sex='w', age=[18, 25], payment_system='visa')
p = person.generate()
```
+ param sex: 'u'-man/woman 'm'-man 'w'-woman
+ param age: List[int] - [from 'x' to 'y' years]. Age range
+ param payment_system: 'visa' - visa 'mc' - mastercard 'mir' - mir 'all' - visa/mastercard/mir systems
___
In Fio.py you can add or remove male first and last names and female first and last names.
<br><br>**Warning !!!!** <br>
The generation of surnames works according to the rules of the Russian language, which means that an ending is provided for female surnames. For example: <br>
Щербаков (male surname) - Щербакова (female surname) <br><br>
**But there are indescribable surnames.** For example: <br><br>
Третьяк (male surname) - Третьяк (female surname) <br><br>
For such a case, in the file Fio.py there  is a list where surnames are entered.
```python
surname_exception = [  # indeclinable surnames
    'Третьяк',
]
```
To add or remove a first or last name, change the appropriate variables (in Fio.py)
+ `man_name`
+ `women_name`
+ `surname`

## Developers

- [MaximGit1](https://github.com/MaximGit1) :face_with_spiral_eyes: 
