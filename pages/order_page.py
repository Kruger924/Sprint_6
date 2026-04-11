import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from data import CONFIRM_ORDER, RENT, SCOOTER_FOR
from locators import order_page_locators as Loc
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Получение заголовка формы оформления заказа.')
    def get_form_title(self):
        '''Получение заголовка формы оформления заказа.'''
        return self.get_element(Loc.ORDER_FORM_TITLE).text

    @allure.step('Заполнение поля «Имя» формы «Для кого самокат».')
    def set_name(self, name):
        '''Заполнение поля «Имя» формы «Для кого самокат».'''
        self.fill_form_field(Loc.NAME_FIELD, name)

    @allure.step('Заполнение поля «Фамилия» формы «Для кого самокат».')
    def set_surname(self, surname):
        '''Заполнение поля «Фамилия» формы «Для кого самокат».'''
        self.fill_form_field(Loc.SURNAME_FIELD, surname)

    @allure.step('Заполнение поля «Адрес» формы «Для кого самокат».')
    def set_address(self, address):
        '''Заполнение поля «Адрес» формы «Для кого самокат».'''
        self.fill_form_field(Loc.ADDRESS_FIELD, address)

    @allure.step('Заполнение поля «Метро» формы «Для кого самокат».')
    def set_metro(self, metro):
        '''Заполнение поля «Метро» формы «Для кого самокат».'''
        self.fill_form_field(Loc.METRO_FIELD, metro, Keys.DOWN, Keys.ENTER)

    @allure.step('Заполнение поля «Телефон» формы «Для кого самокат».')
    def set_phone(self, phone):
        '''Заполнение поля «Телефон» формы «Для кого самокат».'''
        self.fill_form_field(Loc.PHONE_FIELD, phone)

    @allure.step('Нажатие кнопки «Далее» формы «Для кого самокат».')
    def next_btn_click(self):
        '''Нажатие кнопки «Далее» формы «Для кого самокат».'''
        self.click_element(Loc.NEXT_BTN)

    def fill_customer_form(self, name, surname, address, metro, phone):
        '''Заполнение всех полей формы «Для кого самокат»
        и нажатие кнопки «Далее».'''
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_metro(metro)
        self.set_phone(phone)
        self.next_btn_click()

    @allure.step('Заполнение поля «Когда привезти самокат» формы «Про аренду».')
    def set_date(self, date):
        '''Заполнение поля «Когда привезти самокат» формы «Про аренду».'''
        self.fill_form_field(Loc.DELIVERY_DATE, date, Keys.ESCAPE)

    @allure.step('Заполнение поля «Срок аренды» формы «Про аренду».')
    def set_days(self, days):
        '''Заполнение поля «Срок аренды» формы «Про аренду».'''
        self.click_element(Loc.DAYS)
        self.click_element((By.XPATH, Loc.TEXT_IN_DIV.format(days)))

    @allure.step('Заполнение поля «Цвет самоката» формы «Про аренду».')
    def set_color(self, color):
        '''Заполнение поля «Цвет самоката» формы «Про аренду».'''
        self.click_element((By.ID, color))

    @allure.step('Заполнение поля «Комментарий для курьера» формы «Про аренду».')
    def set_comment(self, comment):
        '''Заполнение поля «Комментарий для курьера» формы «Про аренду».'''
        self.fill_form_field(Loc.COMMENT_FIELD, comment)

    @allure.step('Нажатие кнопки «Заказать» формы «Про аренду».')
    def confirm_btn_click(self):
        '''Нажатие кнопки «Заказать» формы «Про аренду».'''
        self.click_element(Loc.CONFIRM_ORDER_BTN)

    def fill_rent_form_and_confirm(self, date, days, color, comment):
        '''Заполнение всех полей формы «Про аренду» и нажатие кнопки
        «Заказать» для формирования заказа.'''
        self.set_date(date)
        self.set_days(days)
        self.set_color(color)
        self.set_comment(comment)
        self.confirm_btn_click()

    @allure.step('Получение заголовка окна «Хотите оформить заказ».')
    def get_confirmation_title(self):
        '''Получение заголовка окна «Хотите оформить заказ».'''
        return self.get_element(Loc.CONFIRMATION_TITLE).text

    @allure.step('Нажатие кнопки «Да» окна «Хотите оформить заказ».')
    def yes_btn_click(self):
        '''Нажатие кнопки «Да» окна «Хотите оформить заказ».'''
        self.click_element(Loc.YES_BTN)

    @allure.step('Получение заголовка окна «Заказ оформлен».')
    def get_order_confirmed_title(self):
        '''Получение заголовка окна «Заказ оформлен».'''
        return self.get_element(Loc.ORDER_CONFIRMED_TITLE).text

    def create_order(self, customer, rent):
        '''Создание нового заказа.'''
        assert self.get_form_title() == SCOOTER_FOR
        self.fill_customer_form(**customer)
        assert self.get_form_title() == RENT
        self.fill_rent_form_and_confirm(**rent)
        assert CONFIRM_ORDER in self.get_confirmation_title()
        self.yes_btn_click()