from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random

def read_token():
    with open("env.txt", "r") as f:
        lines = f.readlines()
        return lines

def hand_typed_comment(comment, field):
    for i, v in enumerate(comment):
        field.send_keys(v)
        sleep(random.random() / 3)

# path to chromedriver
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://instagram.com/")

sleep(random.uniform(1, 3))

try:
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )

    lines = read_token()
    print(lines)

    # entering username and password
    username_input.send_keys(lines[0].strip())
    password_input.send_keys(lines[1].strip())

    sleep(random.uniform(1, 3))

    login_button = driver.find_element_by_xpath("//button[@type='submit']")
    login_button.click()

    # clicking not_now_btn first time
    not_now_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='Not Now']"))
    )
    not_now_btn.click()

    sleep(random.uniform(1, 3))

    # clicking not_now_btn second time
    not_now_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='Not Now']"))
    )
    not_now_btn.click()

    tag = 'bmw'

    sleep(random.uniform(8, 10))

    driver.get("https://www.instagram.com/explore/tags/bmw/")

    sleep(random.uniform(3, 5))

    sleep(random.uniform(1, 3))

    posts = driver.find_elements_by_css_selector("a[href*='/p/']")
    links = [elem.get_attribute('href') for elem in posts]

    comments = ["Nice job!", "Wow! So cool!", "Awesome!", "Superb!", "You have some skills!"]

    for link in links:
        random_time_addon = random.random()

        driver.get(link)
        sleep(3 + random_time_addon)

        like_btn = driver.find_element_by_css_selector(".fr66n .wpO6b")
        like_btn.click()
        sleep(0.5 + random_time_addon)

        like_btn = driver.find_element_by_css_selector("._15y0l .wpO6b")
        like_btn.click()
        sleep(0.5 + random_time_addon)

        comment_textarea = driver.find_element_by_css_selector("textarea")
        hand_typed_comment(random.choice(comments), comment_textarea)
        sleep(0.5 + random_time_addon)

        submit_comment = driver.find_element_by_xpath("//button[text()='Post']")
        submit_comment.click()
        sleep(2 + random_time_addon)

finally:
    print("finished")
    # driver.quit()
