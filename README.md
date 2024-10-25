# RobotSpareBin Automation Project

This project automates the process of ordering robots from [RobotSpareBin Industries Inc.](https://robotsparebinindustries.com/#/robot-order). The robot performs the following tasks:
1. Downloads a CSV file containing order details.
2. Fills in the order form and submits it.
3. Saves the order receipt as a PDF.
4. Takes a screenshot of the ordered robot and embeds it into the PDF receipt.
5. Archives all receipt PDFs into a single ZIP file.

## Table of Contents
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Function Overview](#function-overview)
- [Troubleshooting](#troubleshooting)

---

## Installation

1. **Clone the Repository**
   ```bash
   git https://github.com/jerrykomane/robocorp-cert-two.git
   cd robotsparebin-automation

2. **Install Robocorp and Required Libraries**
Ensure you have Robocorp Lab or the Robocorp Code extension for VS Code installed. The following libraries are required:

RPA.Browser.Selenium (browser automation)
RPA.Tables (table and CSV handling)
RPA.Excel.Files (file management)
RPA.HTTP (HTTP requests for file download)
RPA.PDF (PDF generation and manipulation)
RPA.Archive (file archiving)
These libraries can be added via conda.yaml or requirements.txt for Robocorp environments.

Run the Robot Use Robocorp Lab or Robocorp Code to run the robot, or execute the following in a compatible environment:

rcc run


## Project Structure

robotsparebin-automation/
│
├── tasks.py              # Main script with task definitions and helper functions
├── output/               # Directory where PDF receipts and screenshots are saved
├── README.md             # Documentation for the project
└── conda.yaml            # Environment configuration file for dependencies

## Usage
Usage
Run the Automation
Configure Browser Settings: By default, the browser runs in headed mode (visible). You can switch to headless mode for faster execution by setting headless=True in browser.configure.

Start the Robot: The robot will:

Open the RobotSpareBin order page.
Close any modals.
Download and process the orders in the orders.csv file.
Submit each order and retry if it fails.
Generate PDFs and take screenshots for each order, embedding the screenshots in the PDFs.
Archive all PDFs into a single ZIP file named merged.zip.
Outputs:

PDF Receipts with embedded screenshots saved in the output/ directory.
A ZIP archive of all receipts saved as merged.zip.
Function Overview
order_robots_from_RobotSpareBin
Main function orchestrating the entire order process.

open_robot_order_website
Opens the RobotSpareBin website.

close_annoying_modal
Closes the modal that appears on the website.

download_excel_file
Downloads the orders.csv file containing robot order details.

get_orders
Reads the downloaded orders.csv file and yields each order as a row.

fill_the_form
Fills out the form for each order, submitting and retrying as needed.

store_receipt_as_pdf
Saves the order receipt as a PDF with a unique name.

screenshot_robot
Captures a screenshot of the robot image.

embed_screenshot_to_receipt
Embeds the screenshot into the respective PDF receipt.

archive_receipts
Zips all PDF receipts into a single ZIP file.

Troubleshooting
Headed vs Headless Mode: If you want to run the robot visibly, set headless=False in browser.configure. Headless mode is recommended for faster execution in production.

Retries on Order Submission: The robot automatically retries if an order fails. Check the console log for retry messages if an order submission does not go through on the first try.

Debugging: Set breakpoints in Visual Studio Code to pause execution and inspect variables. Use the Robocorp extension's debug mode for step-by-step inspection.

For further help, reach out on the Robocorp Slack in the #help-developer-training channel.