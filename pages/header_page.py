import allure
from selenium.webdriver.common.by import By

from locators.patterns import A_CLS_CONTAINS, BUTTON, DIV_CLS_CONTAINS
from pages.base_page import BasePage


class HeaderPage(BasePage):
    ORDER_BTN = (
        By.XPATH,
        DIV_CLS_CONTAINS.format('Header') + BUTTON.format('Заказать')
    )
    SCOOTER_LOGO = By.XPATH, A_CLS_CONTAINS.format('Scooter')
    YANDEX_LOGO = By.XPATH, A_CLS_CONTAINS.format('Yandex')

    @allure.step('Нажатие на логотип «Яндекс»')
    def yandex_logo_click(self):
        '''Нажатие на логотип «Яндекс».'''
        self.click_element(self.YANDEX_LOGO)

    @allure.step('Нажатие на логотип «Самокат».')
    def scooter_logo_click(self):
        '''Нажатие на логотип «Самокат».'''
        self.click_element(self.SCOOTER_LOGO)

    @allure.step('Нажатие на кнопку «Заказать».')
    def order_button_click(self):
        '''Нажатие на кнопку «Заказать».'''
        self.click_element(self.ORDER_BTN)