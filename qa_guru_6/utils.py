from pathlib import Path

from selene.core.entity import Element
from selene.core.wait import Command

import qa_guru_6


def resource(path):
    return str(
        Path(qa_guru_6.__file__).
        parent.
        parent.
        joinpath(f'resources/{path}'))


def upload_resource(path: str) -> Command[Element]:
    def fn(element: Element):
        element.send_keys(resource(path))
    return fn


