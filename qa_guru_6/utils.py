from pathlib import Path
from selene import have, command
from selene.support.shared import browser

import qa_guru_6


def resource(path):
    return str(
        Path(qa_guru_6.__file__).
        parent.
        parent.
        joinpath(f'resources/{path}'))


def arrange_student_registration_form_opened():
    browser.open('/automation-practice-form')
    browser.all('[id^=google_ads][id$=container__],[id$=Advertisement]').with_(timeout=10)\
        .should(have.size_less_than_or_equal(2))\
        .perform(command.js.remove)
