Overview
The Auto Order Project automates the process of placing orders on a web app using Python and Selenium. It reads item details from an Excel file (items.xlsx), places the order, and displays a bill popup with an option to download the bill in PDF format.

Features

Automated Login: Automatically logs into the web app with visible typing for better debugging and user experience.

Order Placement: Reads item details from items.xlsx and places orders accordingly.

Browser Alerts: Confirms order placement via browser alerts.

Bill Popup: After placing an order, a bill popup is displayed with an option to download the bill as a PDF.

Extensibility: The script is easy to extend, allowing for future updates and additional features.

Tech Stack

Python 3.10+

Selenium: For automating web interactions.

Pandas: For handling data manipulation.

OpenPyXL: For reading and writing Excel files.

Google Chrome + ChromeDriver: For web automation.

Excel: For input data (items.xlsx).
