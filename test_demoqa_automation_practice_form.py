import time

from selene import browser, be, have
import os


def test_practice_form():
    browser.element('[id="firstName"]').click().type("Pavel")
    browser.element('[id="lastName"]').click().type("Kalinchuk")
    browser.element('[id="userEmail"]').click().type("pavelkalinchuk@mail.tst")
    browser.element('label[for="gender-radio-1"]').click()
    browser.element('#userNumber').click().type("8992367011")
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker-popper').should(be.visible)
    browser.element('.react-datepicker__month-select').should(be.visible).element('[value="0"]').click()
    browser.element('.react-datepicker__year-select').should(be.visible).element('[value="2000"]').click()
    browser.element('.react-datepicker__week').should(be.visible).element('.react-datepicker__day.react'
                                                                          '-datepicker__day--001').click()
    browser.element('#subjectsInput').click().type("computer")
    browser.element('#react-select-2-option-0').click()
    browser.driver.execute_script("window.scrollBy(0,400)", "")
    browser.element('label[for="hobbies-checkbox-1"]').click()
    browser.element('label[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('test_file.png'))
    browser.element('#currentAddress').should(be.visible).click().send_keys("г. Москва, ул. 1-я Строителей, д.1, кв.1")
    browser.driver.execute_script("window.scrollBy(0,400)", "")
    browser.element('#state').should(be.visible).click().element('#react-select-3-option-3').click()
    browser.element('#city').should(be.visible).click().element('#react-select-4-option-1').click()
    browser.driver.execute_script("window.scrollBy(0,400)", "")
    browser.element("#submit").click()
    assert browser.element('.table-responsive').should(have.text("Pavel"))
    assert browser.element('.table-responsive').should(have.text("Kalinchuk"))
    assert browser.element('.table-responsive').should(have.text("pavelkalinchuk@mail.tst"))
    assert browser.element('.table-responsive').should(have.text("8992367011"))
    assert browser.element('.table-responsive').should(have.text("01 January,2000"))
    assert browser.element('.table-responsive').should(have.text("Computer Science"))
    assert browser.element('.table-responsive').should(have.text("Sports"))
    assert browser.element('.table-responsive').should(have.text("Music"))
    assert browser.element('.table-responsive').should(have.text("test_file.png"))
    assert browser.element('.table-responsive').should(have.text("г. Москва, ул. 1-я Строителей, д.1, кв.1"))
    assert browser.element('.table-responsive').should(have.text("Rajasthan"))
    assert browser.element('.table-responsive').should(have.text("Jaiselmer"))
    browser.element('.modal-footer').click()
