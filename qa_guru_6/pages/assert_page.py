from selene import have
from selene.core.entity import Element


class AssertTable:
    def __init__(self, element: Element):
        self.element = element

    def check_data(self, value, row_index: int, column_index: int):
        self.element.all('tr')[row_index].all('td')[column_index].should(have.text(value))
        return self

    '''
    OR:
        # def cell(self, row_index: int, column_index: int):
        # return self.element.all('tr')[row_index].all('td')[column_index]
    '''
