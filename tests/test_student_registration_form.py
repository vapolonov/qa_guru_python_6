from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

from qa_guru_6.data.data import Student, Subjects, Hobbies, Gender
from qa_guru_6.models import app


def test_submit_automation_practice_form():
    app.arrange_student_registration_form_opened()

    browser.should(have.title('ToolsQA'))
    s('.main-header').should(have.exact_text('Practice Form'))

    # Filling the form
    (
        app.form
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

    app.form.submit()

    # Assert data
    (
        app.results
        .check_data(1, 1, Student.name,
                    Student.surname)
        .check_data(2, 1, Student.email)
        .check_data(3, 1, Gender.male)
        .check_data(4, 1, Student.mobile_number)
        .check_data(5, 1, Student.date_of_birth)
        .check_data(6, 1, Subjects.maths,
                    Subjects.english,
                    Subjects.physics)
        .check_data(7, 1, Hobbies.reading,
                    Hobbies.sports)
        .check_data(8, 1, Student.avatar)
        .check_data(9, 1, Student.address)
        .check_data(10, 1, Student.state, Student.city)
    )

'''
    results.should_have_row_with_exact_text(Student.name, Student.surname)
    results.table.cells_of_row(1).should(have.exact_texts(Student.name, Student.surname)
'''