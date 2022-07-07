from selene import have
from selene.support.shared.jquery_style import s, ss


def dropdown(selector: str, /, *, option: str):
    s(selector).click()
    ss('[id^=react-select][id*=option]').element_by(have.exact_text(option)).click()

'''
    # все, что до / нужно использовать только позиционный аргумент (т.е. нельзя использовать selector=...)
    # * обязывает написать при вызове функции option=... (ключ=значение)
    # между / и * можно использовать два варианта выше
'''