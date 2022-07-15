from selene import have, command
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

from qa_guru_6.models.pages.assert_page import AssertTable
from qa_guru_6.models.pages.student_form_page import StudentRegistrationForm

form = StudentRegistrationForm()
results = AssertTable(s('.table'))


def arrange_student_registration_form_opened():
    browser.open('/automation-practice-form')
    browser.all('[id^=google_ads][id$=container__],[id$=Advertisement]').with_(timeout=10) \
        .should(have.size_less_than_or_equal(2)) \
        .perform(command.js.remove)

'''
OR:
class ApplicationManager:

    def __init__(self):
        self.form = StudentRegistrationForm()
        self.results = AssertTable(s('.table'))

    def arrange_student_registration_form_opened(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__],[id$=Advertisement]').with_(timeout=10) \
            .should(have.size_less_than_or_equal(2)) \
            .perform(command.js.remove)


app = ApplicationManager()
'''
