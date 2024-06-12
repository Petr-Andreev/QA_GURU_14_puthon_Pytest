import pytest
from selene import browser, be, have

def test_google_search_pos():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_google_search_neg_ya():
    browser.open('https://ya.ru ')
    if browser.element('[class="Text_typography_body-long-m"]').should(have.text(
            "Нам очень жаль, но запросы с вашего устройства похожи на автоматические."
    )):
        pass
    else:
        text = "kgfksdgslfgsdgjosjgs"
        browser.element('[class=".mini-suggest__input"]').should(be.blank).type(text).press_enter()
        browser.element('[class="EmptySearchResults-Title"]').should(have.text("Ничего не нашли"))

def test_google_search_neg_duck():
    browser.open(' https://duckduckgo.com')
    text = "kgfksdgslfgsdgjosjgs"
    browser.element('[class="searchbox_input__bEGm3"]').should(be.blank).type(text).press_enter()
    browser.element('[class="w7syQmNN6Yjvw6guGJuQ"]').should(have.text(f"По запросу {text} результаты не найдены."))
