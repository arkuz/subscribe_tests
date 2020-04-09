from selenium import webdriver


def config_and_run_browser(config: dict):
    if config['browser'] == 'Chrome':
        capabilities = {
            "browserName": "chrome",
            "version": "80.0",
            "enableVNC": True,
            "enableVideo": False
        }

    if config['browser'] == 'Firefox':
        capabilities = {
            "browserName": "firefox",
            "version": "73.0",
            "enableVNC": True,
            "enableVideo": False
        }

    driver = webdriver.Remote(
        command_executor=config['selenoid_url'],
        desired_capabilities=capabilities
    )

    driver.implicitly_wait(config['implicitly_wait'])
    driver.maximize_window()

    return driver

