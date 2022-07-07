from typing import Optional

from selene import have, command
from selene.core.entity import Element
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

from qa_guru_6.controls import select
# from qa_guru_6.controls import tags_input
from qa_guru_6.utils import resource, arrange_student_registration_form_opened


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


def test_submit_automation_practice_form():
    arrange_student_registration_form_opened()

    browser.should(have.title('ToolsQA'))
    s('.main-header').should(have.exact_text('Practice Form'))

    # Filling the form
    s('#firstName').type(Student.name)
    s('#lastName').type(Student.surname)
    s('#userEmail').type(Student.email)
    s('#userNumber').type(Student.mobile_number)

    # Select Gender
    gender_group = s('#genterWrapper')
    gender_group.all('.custom-radio').element_by(have.exact_text(Gender.male)).click()

    # Select Date of Birth
    s('#dateOfBirthInput').click()
    s('.react-datepicker__year-select').s(f'[value="{Student.year}"]').click()
    s('.react-datepicker__month-select').s(f'[value="{Student.month}"]').click()
    s(f'.react-datepicker__day--0{Student.day}').click()

    class TagsInput:
        def __init__(self):
            self.element: Element = ...

        def add(self, from_: str, /, *, autocomplete: Optional[str] = None):
            self.element.type(from_)
            browser.all(
                '.subjects-auto-complete_option'
            ).element_by(have.text(autocomplete or from_)).click()


    # Select Subjects

    subjects = TagsInput()
    subjects.element = browser.element('#subjectInput')
    subjects.add('Ma', autocomplete='Maths')
    subjects.add('English')
    subjects.add('Physics')

    # Select hobbies - checkbox
    s('#hobbiesWrapper').s('label[for=hobbies-checkbox-2]').click()
    s('#hobbiesWrapper').s('label[for=hobbies-checkbox-1]').click()

    # Upload a file
    s('#uploadPicture').send_keys(resource('picture.png'))
    # s('#uploadPicture').send_keys(upload_resource('picture.png'))

    # Filling the address
    s('#currentAddress').type(f'{Student.address}')
    select.dropdown('#state', option=Student.state)
    select.dropdown('#city', option=Student.city)

    # Sending the form
    s('#submit').perform(command.js.click)

    # Assert
    s('.table-responsive').should(have.text(f'{Student.name} {Student.surname}'))
    s('.table-responsive').should(have.text(Student.email))
    s('.table-responsive').should(have.text(Gender.male))
    s('.table-responsive').should(have.text(Student.mobile_number))
    s('.table-responsive').should(have.text(Student.date_of_birth))
    s('.table-responsive').should(have.text(f'{Subjects.maths}, {Subjects.english}, {Subjects.physics}'))
    s('.table-responsive').should(have.text(f'{Hobbies.reading}, {Hobbies.sports}'))
    s('.table-responsive').should(have.text(Student.avatar))
    s('.table-responsive').should(have.text(Student.address))
    s('.table-responsive').should(have.text(f'{Student.state} {Student.city}'))

    '''
    OR
    s('.table').ss('tr').should(have.texts('Values',
                                           'Vasiliy Apolonov',
                                           'test@mail.com',
                                           'Male',
                                           '9101112233',
                                           '09 September,1974',
                                           'Maths, English, Physics',
                                           'Reading, Sports',
                                           'example.txt',
                                           'Russia, Nizhny Novgorod',
                                           'Uttar Pradesh Lucknow'))
    '''