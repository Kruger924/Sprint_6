import allure
import pytest

from locators.urls import MAIN_PAGE, ORDER_PAGE, DZEN
from pages.header_page import HeaderPage


class TestHeaderPage:
    @allure.title('Перенаправление по нажатию на логотип «Яндекс» и «Самокат»')
    @pytest.mark.parametrize(
        'name, url',
        [pytest.param('yandex', DZEN, id='Yandex'),
         pytest.param('scooter', MAIN_PAGE, id='Scooter')]
    )
    def test_logo_click_redirect(self, driver, name, url):
        '''По нажатию на логотип «Яндекс» открывается страница «Дзен».
        По нажатию на логотип «Самокат» открывается главная страница.'''
        header_page = HeaderPage(driver)
        header_page.order_button_click()
        assert header_page.get_current_url() == ORDER_PAGE
        getattr(header_page, f'{name}_logo_click')()
        header_page.switch_window(url)
        assert header_page.get_current_url() == url