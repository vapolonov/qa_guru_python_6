from dataclasses import dataclass


class Student:
    name = 'Vasily'
    surname = 'Apolonov'
    email = 'test@mail.com'
    mobile_number = '9101112233'
    day = '09'
    month = '8'
    year = '1974'
    date_of_birth = '09 September,1974'
    address = 'Russia, Nizhny Novgorod'
    state = 'Uttar Pradesh'
    city = 'Lucknow'
    avatar = 'picture.png'


class Gender:
    male = 'Male'
    female = 'Female'
    other = 'Other'


class Subjects:
    maths = 'Maths'
    english = 'English'
    physics = 'Physics'


class Hobbies:
    sports = 'Sports'
    reading = 'Reading'
    music = 'Music'


'''
OR:
class Hobbies:
    def __init__(self, *hobbies):
        self.sports = 'Sports'
        self.reading = 'Reading'
        self.music = 'Music'

@dataclass
class Hobbies:
    values = list[str]
'''
