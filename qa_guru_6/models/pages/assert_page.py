from selene import have
from selene.core.entity import Element


class AssertTable:
    def __init__(self, element: Element):
        self.element = element

    def check_data(self, row_index: int, column_index: int, *values: str):
        for value in values:
            self.element.all('tr')[row_index].all('td')[column_index].should(have.text(value))
        return self

    '''
    OR:
        # def cell(self, row_index: int, column_index: int):
        # return self.element.all('tr')[row_index].all('td')[column_index]
    '''
    '''
    def __init__(self):
        self.element = browser.element('.modal-dialog')
        self.table = Table(self.element.element('.table'))

    def should_have_row_with_exact_text(self, *values):
        self.table.cells_of_row(1).should(have.exact_texts(Student.name, Student.surname))
    '''
