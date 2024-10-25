from robocorp.tasks import task
from robocorp import browser  # Import browser here
from RPA.HTTP import HTTP
from RPA.Tables import Tables
from RPA.Archive import Archive
from RPA.PDF import PDF  # Import PDF class here
from robot_order_page import RobotOrderPage  # Import the page object

# Initialize the PDF and Archive tools
pdf = PDF()
archive = Archive()

# Helper Functions
def download_orders_file():
    http = HTTP()
    http.download(url="https://robotsparebinindustries.com/orders.csv", overwrite=True)

def get_orders():
    csv_file = Tables()
    orders = csv_file.read_table_from_csv("orders.csv", columns=["Order number", "Head", "Body", "Legs", "Address"])
    for row in orders:
        yield row

def embed_screenshot_to_receipt(screenshot_path, order_number):
    pdf.add_files_to_pdf(  
        files=[screenshot_path],
        target_document=f"output/{order_number}.pdf",
        append=True
    )

def archive_receipts():
    archive.archive_folder_with_zip('output/', 'output/merged.zip')

# Main Task
@task
def order_robots_from_RobotSpareBin():
    # Configure the browser instance here
    browser.configure(headless=True)
    
    # Create an instance of the page object
    robot_order_page = RobotOrderPage()

    # Open the robot order page and close the modal
    robot_order_page.open()
    robot_order_page.close_annoying_modal()

    # Download and get orders from CSV
    download_orders_file()
    orders = get_orders()

    # Loop through orders and process each one
    for order in orders:
        robot_order_page.select_head(order["Head"])
        robot_order_page.select_body(order["Body"])
        robot_order_page.fill_legs(order["Legs"])
        robot_order_page.fill_address(order["Address"])

        # Submit order and retry if necessary
        while True:
            robot_order_page.submit_order()
            if robot_order_page.is_order_successful():
                # Capture and save the receipt PDF and screenshot
                receipt_path = robot_order_page.capture_pdf_receipt(order["Order number"])
                screenshot_path = robot_order_page.capture_screenshot(order["Order number"])
                embed_screenshot_to_receipt(screenshot_path, order["Order number"])

                # Prepare for the next order
                robot_order_page.click_order_another()
                robot_order_page.close_annoying_modal()
                print(f"Order {order['Order number']} successful.")
                break
            else:
                print(f"Order {order['Order number']} failed, retrying...")

    # Archive all the receipts after processing all orders
    archive_receipts()
