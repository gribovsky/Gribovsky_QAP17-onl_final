import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options


@pytest.fixture
def driver():
    edge_options = Options()
    edge_options.add_argument("--start-maximized")
    driver = webdriver.Edge(options=edge_options)
    driver.implicitly_wait(5)
    driver.get("https://www.onliner.by")
    yield driver
