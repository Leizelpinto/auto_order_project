from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
import time
import os
import json

class OrderBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)

    def open_app(self, url):
        self.driver.get(url)
        print("Opened app...")
        time.sleep(2)

    def slow_type(self, element, text, delay=0.2):
        for char in text:
            element.send_keys(char)
            time.sleep(delay)

    def login(self, username, password):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        email_box = wait.until(EC.presence_of_element_located((By.ID, "username")))
        print("Typing username...")
        self.slow_type(email_box, username)

        pass_box = wait.until(EC.presence_of_element_located((By.ID, "password")))
        print("Typing password...")
        self.slow_type(pass_box, password)

        login_btn = wait.until(EC.element_to_be_clickable((By.ID, "loginBtn")))
        print("Clicking login button...")
        login_btn.click()
        time.sleep(2)

        try:
            alert = driver.switch_to.alert
            print(f"Alert detected: {alert.text}")
            alert.accept()
        except NoAlertPresentException:
            pass

        time.sleep(2)

    def place_order(self, item_name, quantity, price):
        driver = self.driver
        driver.find_element(By.ID, "itemName").send_keys(item_name)
        driver.find_element(By.ID, "quantity").send_keys(str(quantity))
        driver.find_element(By.ID, "price").send_keys(str(price))
        driver.find_element(By.ID, "addToCart").click()
        time.sleep(1)

        try:
            alert = driver.switch_to.alert
            print(f"Alert detected: {alert.text}")
            alert.accept()
        except NoAlertPresentException:
            pass

        time.sleep(2)
        print(f"Order Placed → {item_name} (Qty: {quantity})")

    def show_bill_tab(self, orders):
        # Create HTML for bill
        table_html = "<h2>Receipt</h2><table border='1' style='border-collapse: collapse; padding:5px;'>"
        table_html += "<tr><th>Item</th><th>Quantity</th><th>Price</th><th>Total</th></tr>"
        grand_total = 0
        for o in orders:
            total = o['Quantity'] * o['Price']
            grand_total += total
            table_html += f"<tr><td>{o['ItemName']}</td><td>{o['Quantity']}</td><td>{o['Price']}</td><td>{total}</td></tr>"
        table_html += f"<tr><td colspan='3'><b>Grand Total</b></td><td>{grand_total}</td></tr>"
        table_html += "</table>"

        # Create temporary HTML file
        html_content = f"""
        <html>
        <head>
            <title>Bill</title>
        </head>
        <body>
            {table_html}<br><br>
            <button onclick="window.print()">Download / Print PDF</button>
        </body>
        </html>
        """

        tmp_path = os.path.join(os.getcwd(), "bill.html")
        with open(tmp_path, "w") as f:
            f.write(html_content)

        # Open in new tab
        self.driver.execute_script(f"window.open('file:///{tmp_path.replace(os.sep, '/')}');")
        self.driver.switch_to.window(self.driver.window_handles[-1])
        print("Bill page opened with Download PDF button.")
        time.sleep(1)

    def close(self):
        self.driver.quit()
        print("Browser closed.")
