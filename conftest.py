# import pytest
#
# @pytest.fixture(scope='session',autouse=True)
# def tc_setup(browser):
#     if browser=='chrome':
#         print('launch chrome')
#     elif browser=='firefox':
#         print('launch firefox')
#     else:
#         print('provide valid browser')
#     print('login')
#     print('browse product')
#     yield
#     print('logoff')
#     print('close browser')
#
# def pytest_addoption(parser):
#     parser.addoption('--browser')
#
#
# @pytest.fixture(scope='session',autouse=True)
# def browser(request):
#     return request.config.getoption('--browser')
#
#


# import pytest
#
#
# @pytest.fixture(scope='module',autouse=False)
# def setup():
#     print('launch the browser')
#     print('login')
#     print('browse the product')
#     yield
#     print('logoff')
#     print('close the browser')





