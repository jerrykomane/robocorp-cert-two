from robocorp import browser  # Import browser from Robocorp
from PIL import Image
from RPA.PDF import PDF  # Import PDF class
import time

# Initialize PDF instance
pdf = PDF()

class RobotOrderPage:
    def __init__(self):
        self.page = browser.page()

    def open(self):
        browser.goto('https://robotsparebinindustries.com/#/robot-order')

    def close_annoying_modal(self):
        self.page.click("text=OK")

    def select_head(self, head_option):
        head_map = {
            '1': 'Roll-a-thor head',
            '2': 'Peanut crusher head',
            '3': 'D.A.V.E head',
            '4': 'Andy Roid head',
            '5': 'Spanner mate head',
            '6': 'Drillbit 2000 head'
        }
        self.page.select_option('#head', head_map[head_option])

    def select_body(self, body_option):
        body_map = {
            '1': '#id-body-1',
            '2': '#id-body-2',
            '3': '#id-body-3',
            '4': '#id-body-4',
            '5': '#id-body-5',
            '6': '#id-body-6'
        }
        self.page.click(body_map[body_option])

    def fill_legs(self, legs):
        self.page.fill("input[placeholder='Enter the part number for the legs']", legs)

    def fill_address(self, address):
        self.page.fill("#address", address)

    def submit_order(self):
        self.page.click("css=#order")

    def is_order_successful(self):
        return self.page.query_selector("css=#order-another") is not None

    def click_order_another(self):
        self.page.click("css=#order-another")

    def capture_screenshot(self, order_number):
        element = self.page.query_selector("#robot-preview-image")
        path = f"output/{order_number}.png"
        element.screenshot(path=path)
        image = Image.open(path)
        resized_image = image.resize((500, int(image.height * (500 / image.width))))
        resized_image.save(path)
        return path

    def capture_pdf_receipt(self, order_number):
        order_html = self.page.locator("#receipt").inner_html()
        path = f"output/{order_number}.pdf"
        pdf.html_to_pdf(order_html, path)  # Using the PDF instance to save HTML as PDF
        return path
