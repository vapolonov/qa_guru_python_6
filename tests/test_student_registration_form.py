from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

from qa_guru_6.data import data
from qa_guru_6.pages.assert_page import Table
from qa_guru_6.pages.student_form_page import StudentRegistrationForm
from qa_guru_6.utils import arrange_student_registration_form_opened


def test_submit_automation_practice_form():
    arrange_student_registration_form_opened()

    browser.should(have.title('ToolsQA'))
    s('.main-header').should(have.exact_text('Practice Form'))

    # Filling the form
    StudentRegistrationForm().set_first_name(data.Student.name).set_last_name(data.Student.surname)

    StudentRegistrationForm().set_email(data.Student.email)
    StudentRegistrationForm().set_mobile(data.Student.mobile_number)

    # Select Gender
    StudentRegistrationForm().set_gender(data.Gender.male)

    # Select Date of Birth
    StudentRegistrationForm().set_birth_date(data.Student.year,
                                             data.Student.month,
                                             data.Student.day)

    # Select Subjects
    (
        StudentRegistrationForm()
        .select_subjects(data.Subjects.maths)
        .select_subjects(data.Subjects.english)
        .select_subjects(data.Subjects.physics)
    )

    # Select hobbies - checkbox
    StudentRegistrationForm().select_hobbies(data.Hobbies.reading).select_hobbies(data.Hobbies.sports)

    # Upload a file
    StudentRegistrationForm().upload(data.Student.avatar)

    # Filling the address
    StudentRegistrationForm().set_address(data.Student.address)

    # Set state and city
    StudentRegistrationForm().set_state_city(data.Student.state, data.Student.city)

    # Sending the form
    StudentRegistrationForm().submit()

    # Assert
    results = Table(s('.modal-content .table'))
    results.cell(1, 1).should(have.text(f'{data.Student.name} {data.Student.surname}'))
    results.cell(2, 1).should(have.text(data.Student.email))
    results.cell(3, 1).should(have.text(data.Gender.male))
    results.cell(4, 1).should(have.text(data.Student.mobile_number))
    results.cell(5, 1).should(have.text(data.Student.date_of_birth))
    results.cell(6, 1).should(have.text(f'{data.Subjects.maths}, '
                                        f'{data.Subjects.english}, '
                                        f'{data.Subjects.physics}'))
    results.cell(7, 1).should(have.text(f'{data.Hobbies.reading}, {data.Hobbies.sports}'))
    results.cell(8, 1).should(have.text(data.Student.avatar))
    results.cell(9, 1).should(have.text(data.Student.address))
    results.cell(10, 1).should(have.text(f'{data.Student.state} {data.Student.city}'))
