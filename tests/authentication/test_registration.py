import pytest
import allure

from pages.dashboard.dashboard_page import DashboardPage
from pages.authentication.registration_page import RegistrationPage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from allure_commons.types import Severity


@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.REGISTRATION)
class TestRegistration:
    @allure.title('Registration with correct email, username and password')
    @allure.severity(Severity.CRITICAL)
    def test_successful_registration(self, registration_page: RegistrationPage, dashboard_page: DashboardPage):
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.registration_form.fill('email', 'username', 'password')
        registration_page.check_visible_registration_button()
        registration_page.click_registration_button()
        dashboard_page.dashboard_toolbar_view.check_visible()





    # chromium_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    #
    # email_input = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
    # email_input.fill('user@gmail.com')
    #
    # username_input = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
    # username_input.fill('username')
    #
    # password_input = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
    # password_input.fill('password')
    #
    # registration_button = chromium_page.get_by_test_id('registration-page-registration-button')
    # registration_button.click()
    #
    # dashboard_title = chromium_page.get_by_test_id('dashboard-toolbar-title-text')
    # expect(dashboard_title).to_be_visible()
