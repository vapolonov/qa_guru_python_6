from typing import Optional

from selene import have
from selene.core.entity import Element
from selene.support.shared.jquery_style import ss


class TagsInput:
    def __init__(self, element: Element):
        self.element = element

    def add(self, option: str):
        self.element.set_value(option).press_enter()

    def autocomplete(self, /, *, from_: str, to_: str = None):
        self.element.type(from_)
        ss('.subjects-auto-complete__option').element_by(have.text(to_)).click()

    def add_or_auto(self, from_: str, /, *, autocomplete: Optional[str] = None):
        self.element.type(from_)
        ss(
            '.subjects-auto-complete__option'
        ).element_by(have.text(autocomplete or from_)).click()


'''
# element = ...

... - пустота, отличается от None
... - означает, что сейчас пустота, но скоро там будет какое то значение

    def autocomplete(selector: str, from_: str, to: str = None):
        s(selector).type(from_)
        ss('.subjects-auto-complete__option').element_by(have.exact_text(from_)).click()
    OR:
        ss('.subjects-auto-complete__option').element_by(have.exact_text(
            to if to else from_)).click()

    autocomplete('#subjectsInput', from_='Eng', to=Subjects.english)   


    # все, что до / нужно использовать только позиционный аргумент (т.е. нельзя использовать selector=...)
    # * обязывает написать при вызове функции option=... (ключ=значение)
    # между / и * можно использовать два варианта выше
'''