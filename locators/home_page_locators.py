from selenium.webdriver.common.by import By

class HomePageHeaderLocators:
    logo_yandex = (By.XPATH, ".//a[@class = 'Header_LogoYandex__3TSOI']")
    logo_scooter = (By.XPATH, ".//a[@class = 'Header_LogoScooter__3lsAR']")
    order_button = (By.XPATH, "(.//button[text() = 'Заказать'])[1]")
    order_status_button = (By.XPATH, ".//button[text() = 'Статус заказа']")
    number_order_field = (By.XPATH, ".//input[@class = 'Input_Input__1iN_Z Header_Input__xIoUq']")
    go_button = (By.XPATH, ".//button[text() = 'Go!']")
    track_field = (By.XPATH, ".//input[@placeholder='Введите номер заказа']")
    view_button = (By.XPATH, ".//button[text() = 'Посмотреть']")
    header_page_title = (By.XPATH, ".//div[text() = 'Учебный тренажер']")

class HomePageLocators:
    home_page_title = (By.XPATH, ".//div[@class = 'Home_Header__iJKdX']")
    order_button = (By.XPATH, "(//button[text() = 'Заказать'])[2]")
    accept_cookies_button = (By.XPATH, "//button[@id = 'rcc-confirm-button']")
    questions_title = (By.XPATH, "//div[text() = 'Вопросы о важном']")

    questions = [
        (By.ID, "accordion__heading-8"),
        (By.ID, "accordion__heading-9"),
        (By.ID, "accordion__heading-10"),
        (By.ID, "accordion__heading-11"),
        (By.ID, "accordion__heading-12"),
        (By.ID, "accordion__heading-13"),
        (By.ID, "accordion__heading-14"),
        (By.ID, "accordion__heading-15")
    ]

    questions_text = [
        (By.ID, "accordion__panel-8"),
        (By.ID, "accordion__panel-9"),
        (By.ID, "accordion__panel-10"),
        (By.ID, "accordion__panel-11"),
        (By.ID, "accordion__panel-12"),
        (By.ID, "accordion__panel-13"),
        (By.ID, "accordion__panel-14"),
        (By.ID, "accordion__panel-15")
    ]