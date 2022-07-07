from selene import have
from selene.support.shared.jquery_style import s, ss

# element = ...
'''
... - пустота, отличается от None
... - означает, что сейчас пустота, но скоро там будет какое то значение
'''


def add(subjects, from_: str):
    s(subjects).type(from_)
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