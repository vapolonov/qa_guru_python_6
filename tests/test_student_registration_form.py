from selene import have, by, command
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss

from qa_guru_6.utils import resource, upload_resource


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


def arrange_student_registration_form_opened():
    browser.open('/automation-practice-form')
    browser.all('[id^=google_ads][id$=container__],[id$=Advertisement]').with_(timeout=10)\
        .should(have.size_less_than_or_equal(2))\
        .perform(command.js.remove)


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

    # Select Subjects
    # s('#subjectsInput').set_value(Subjects.maths).press_enter()
    # s('#subjectsInput').set_value(Subjects.english).press_enter()
    # s('#subjectsInput').set_value(Subjects.physics).press_enter()

    def autocomplete(selector: str, from_: str):
        s(selector).type(from_)
        ss('.subjects-auto-complete__option').element_by(have.exact_text(from_)).click()
    '''
    def autocomplete(selector: str, from_: str, to: str = None):
        s(selector).type(from_)
        ss('.subjects-auto-complete__option').element_by(have.exact_text(from_)).click()
    OR:
        ss('.subjects-auto-complete__option').element_by(have.exact_text(
            to if to else from_)).click()
        
    autocomplete('#subjectsInput', from_='Eng', to=Subjects.english)   
    '''

    autocomplete('#subjectsInput', from_=Subjects.maths)
    autocomplete('#subjectsInput', from_=Subjects.english)
    autocomplete('#subjectsInput', from_=Subjects.physics)


    # Select hobbies - checkbox
    s('#hobbiesWrapper').s('label[for=hobbies-checkbox-2]').click()
    s('#hobbiesWrapper').s('label[for=hobbies-checkbox-1]').click()


    # Upload a file
    s('#uploadPicture').send_keys(resource('picture.png'))
    # s('#uploadPicture').send_keys(upload_resource('picture.png'))

    # Filling the address
    s('#currentAddress').type(f'{Student.address}')

    def select_dropdown(selector: str, /, *, option: str):
        # все, что до / нужно использовать только позиционный аргумент (т.е. нельзя использовать selector=...)
        # * обязывает написать при вызове функции option=... (ключ=значение)
        # между / и * можно использовать два варианта выше
        s(selector).click()
        ss('[id^=react-select][id*=option]').element_by(have.exact_text(option)).click()

    select_dropdown('#state', option=Student.state)
    select_dropdown('#city', option=Student.city)

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