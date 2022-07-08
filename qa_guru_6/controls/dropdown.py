from selene import command, by
from selene.core.entity import Element
from selene.support.shared.jquery_style import s


class Dropdown:
    def __init__(self, element: Element):
        self.element = element

    def select(self, state: str):
        self.element.perform(command.js.scroll_into_view)
        s('#state').click()
        s(by.text(state)).click()

    def autocomplete(self, city: str):
        self.element.s('#react-select-4-input').type(city).press_tab()

