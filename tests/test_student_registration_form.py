from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

from qa_guru_6.data.data import Student, Subjects, Hobbies, Gender
from qa_guru_6.pages.assert_page import AssertTable
from qa_guru_6.pages.student_form_page import StudentRegistrationForm
from qa_guru_6.utils import arrange_student_registration_form_opened


def test_submit_automation_practice_form():
    arrange_student_registration_form_opened()

    browser.should(have.title('ToolsQA'))
    s('.main-header').should(have.exact_text('Practice Form'))

    # Filling the form
    (
        StudentRegistrationForm
        .set_first_name(Student.name)
        .set_last_name(Student.surname)
        .set_email(Student.email)
        .set_mobile(Student.mobile_number)
        .set_gender(Gender.male)
        .set_birth_date(Student.year,
                        Student.month,
                        Student.day)
        .select_subjects(Subjects.maths,
                         Subjects.english,
                         Subjects.physics)
        .select_hobbies(Hobbies.reading,
                        Hobbies.sports)
        .upload(Student.avatar)
        .set_address(Student.address)
        .set_state_city(Student.state, Student.city)
    )

    StudentRegistrationForm().submit()

    # Assert data
    results = AssertTable(s('.table'))
    (
        results.check_data(Student.name, 1, 1)
        .check_data(Student.surname, 1, 1)
        .check_data(Student.email, 2, 1)
        .check_data(Gender.male, 3, 1)
        .check_data(Student.mobile_number, 4, 1)
        .check_data(Student.date_of_birth, 5, 1)
        .check_data(Subjects.maths, 6, 1)
        .check_data(Subjects.english, 6, 1)
        . check_data(Subjects.physics, 6, 1)
        .check_data(Hobbies.reading, 7, 1)
        .check_data(Hobbies.sports, 7, 1)
        .check_data(Student.avatar, 8, 1)
        .check_data(Student.address, 9, 1)
        .check_data(Student.state, 10, 1)
        .check_data(Student.city, 10, 1)
    )
