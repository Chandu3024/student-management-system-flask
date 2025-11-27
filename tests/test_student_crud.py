# tests/test_student_crud.py
import time
from tests.pages.login_page import LoginPage
from tests.pages.dashboard_page import DashboardPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_success(driver, base_url):
    lp = LoginPage(driver, base_url)
    lp.load()
    lp.login("admin", "admin123")
    # after login should redirect to dashboard
    WebDriverWait(driver, 4).until(EC.url_contains("/dashboard"))
    assert "/dashboard" in driver.current_url

def test_add_student(driver, base_url):
    dp = DashboardPage(driver, base_url)
    dp.load()
    dp.click_add()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.NAME, "name")))
    driver.find_element(By.NAME, "name").send_keys("Test Student")
    driver.find_element(By.NAME, "usn").send_keys("TEST001")
    driver.find_element(By.NAME, "branch").send_keys("ISE")
    driver.find_element(By.NAME, "year").send_keys("4")
    driver.find_element(By.NAME, "email").send_keys("teststudent@example.com")
    driver.find_element(By.NAME, "phone").send_keys("9999999999")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    # back to dashboard
    WebDriverWait(driver, 3).until(EC.url_contains("/dashboard"))
    rows = dp.get_rows()
    assert any("TEST001" in r.text for r in rows)

def test_search_student(driver, base_url):
    dp = DashboardPage(driver, base_url)
    dp.load()
    dp.search("TEST001")
    WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "table.students-table tbody tr")))
    rows = dp.get_rows()
    assert len(rows) >= 1
    assert "TEST001" in rows[0].text

def test_edit_student(driver, base_url):
    dp = DashboardPage(driver, base_url)
    dp.load()
    # find row with TEST001
    rows = dp.get_rows()
    target = None
    for r in rows:
        if "TEST001" in r.text:
            target = r
            break
    assert target is not None
    edit_link = target.find_element(By.LINK_TEXT, "Edit")
    edit_link.click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.NAME, "name")))
    name = driver.find_element(By.NAME, "name")
    name.clear()
    name.send_keys("Test Student Edited")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    WebDriverWait(driver, 3).until(EC.url_contains("/dashboard"))
    rows = dp.get_rows()
    assert any("Test Student Edited" in r.text for r in rows)

def test_delete_student(driver, base_url):
    dp = DashboardPage(driver, base_url)
    dp.load()
    rows = dp.get_rows()
    target = None
    for r in rows:
        if "TEST001" in r.text:
            target = r
            break
    if target is None:
        pytest.skip("test student not present")
    # click delete form button
    btn = target.find_element(By.CSS_SELECTOR, "form button[type='submit']")
    btn.click()

    # Accept JS confirm alert
    alert = driver.switch_to.alert
    alert.accept()

    # Wait until redirect happens
    WebDriverWait(driver, 3).until(EC.url_contains("/dashboard"))

    rows = dp.get_rows()
    assert not any("TEST001" in r.text for r in rows)
