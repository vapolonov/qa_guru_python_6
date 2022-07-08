
from selene import have, by, command
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss

from qa_guru_6.controls import set_hobbies
from qa_guru_6.controls.dropdown import Dropdown
from qa_guru_6.controls.tags_input import TagsInput
from qa_guru_6.utils import resource, arrange_student_registration_form_opened


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

    browser.open('/automation-practice-form')
    browser.should(have.title('ToolsQA'))
    s('.main-header').should(have.exact_text('Practice Form'))

    # Filling the form
    s('#firstName').type('Vasiliy')
    s('#lastName').type('Apolonov')
    s('#userEmail').type('test@mail.com')

    mobile_number = s('#userNumber')
    mobile_number.type('9101112233')

    # Select Gender (radio-button)
    gender_group = s('#genterWrapper')
    gender_group.all('.custom-radio').element_by(have.exact_text('Male')).click()

    # Select Date of Birth
    s('#dateOfBirthInput').click()
    s('.react-datepicker__year-select').s('[value="1974"]').click()
    s('.react-datepicker__month-select').s('[value="8"]').click()
    s('.react-datepicker__day--009').click()

    '''
    browser.execute_script('document.querySelector("#dateOfBirthInput").value = "27 Jun 2022";')
    browser.element('#dateOfBirthInput').perform(command.js.set_value('09 Sep 1974')).press_enter()
    browser.element('#dateOfBirthInput').with_(set_value_by_js=True).set_value('09 Sep 1974')
    '''

    # Set Subjects
    subject = TagsInput(s('#subjectsInput'))
    subject.add(Subjects.maths)
    subject.autocomplete(from_='Eng', to_=Subjects.english)
    subject.add_or_auto('Phys')

    # Set hobbies - checkbox
    set_hobbies.set_hobby(Hobbies.sports)
    set_hobbies.set_hobby(Hobbies.music)

    # Load a file
    s('#uploadPicture').send_keys(resource('picture.png'))

    # Filling the address
    s('#currentAddress').type('Russia, Nizhny Novgorod')

    set_state = Dropdown(s('#stateCity-wrapper'))
    set_state.select(state='Uttar Pradesh')
    set_city = Dropdown(s('#stateCity-wrapper'))
    set_city.autocomplete(city='Lucknow')

    # Sending the form
    '''
    # s('footer').perform(command.js.remove)
    # s('#submit').click()
    '''
    s('#submit').perform(command.js.click)

    # Assert
    s('.table-responsive').should(have.text('Vasiliy Apolonov'))
    s('.table-responsive').should(have.text('test@mail.com'))
    s('.table-responsive').should(have.text('Male'))
    s('.table-responsive').should(have.text('9101112233'))
    s('.table-responsive').should(have.text('09 September,1974'))
    s('.table-responsive').should(have.text('Maths, English, Physics'))
    s('.table-responsive').should(have.text('Sports, Music'))
    s('.table-responsive').should(have.text('picture.png'))
    s('.table-responsive').should(have.text('Russia, Nizhny Novgorod'))
    s('.table-responsive').should(have.text('Uttar Pradesh Lucknow'))

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
    #
    # browser.all('table tr')[5].all('td')[1].should(have.exact_text('09 September,1974'))
    #
    # def cells_of_row(index, should_have_texts: list[str]):
    #     browser.element('.modal-dialog').all('table tr')[index].all('td').should(have.exact_texts(*should_have_texts))
    #
    # cells_of_row(index=5, should_have_texts=[
    #     'Date of Birth', '09 September,1974'
    # ])
    #
    # cells_of_row(index=6, should_have_texts=['Subjects', 'Maths, English, Physics'])