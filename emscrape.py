import csv
import json
import os
import sys
from getpass import getpass

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Create CSV
header = ["company", "industry", "URL"]
with open("industry.csv", "a+", newline="", encoding="UTF8") as industry_csv:
    writer = csv.writer(industry_csv)
    writer.writerow(header)

# Make window headless
Options = Options()
Options.headless = True
Options.add_argument("--log-level=3")

# Create webdriver instance
if sys.platform.startswith("linux"):
    driver = webdriver.Chrome("drivers/linux_chromedriver", options=Options)
elif sys.platform.startswith("darwin"):
    driver = webdriver.Chrome("drivers/mac_chromedriver", options=Options)
elif sys.platform.startswith("win32"):
    driver = webdriver.Chrome("drivers/win32_chromedriver.exe", options=Options)

# Open linkedin
driver.get("https://linkedin.com/uas/login")

# Find username field and prompt for input
username = driver.find_element_by_id("username")
if sys.platform.startswith("linux"):
    os.system('clear')
elif sys.platform.startswith("darwin"):
    os.system('clear')
elif sys.platform.startswith("win32"):
    os.system('cls')

# username.send_keys(input("Enter your username: "))
username.send_keys(input("Enter your username: "))

# Find password field and prompt for input
pword = driver.find_element_by_id("password")
if sys.platform.startswith("linux"):
    os.system('clear')
elif sys.platform.startswith("darwin"):
    os.system('clear')
elif sys.platform.startswith("win32"):
    os.system('cls')
# pword.send_keys(getpass("Enter your password: "))
pword.send_keys(getpass("Enter your password: "))

# Log in
driver.find_element_by_xpath("//button[@type='submit']").click()
if sys.platform.startswith("linux"):
    os.system('clear')
elif sys.platform.startswith("darwin"):
    os.system('clear')
elif sys.platform.startswith("win32"):
    os.system('cls')

# Read mock customer data from file (replace with real customer data later)
with open("customer_db.json", "r") as customer_db:
    mock_data = json.load(customer_db)

    # Loop through the mock data to get company name and email
    print("Fetching Results...")
    for customer in mock_data:
        company = customer["company"]
        email = customer["email"]
        name = customer["name"]

        # Create search query for each customers company
        query_url = f"https://www.linkedin.com/company/{company}/about/"

        # Fetch the industry of each company from linkedin
        driver.get(query_url)

        # Get page source code
        src = driver.page_source

        # Parse page source code
        soup = BeautifulSoup(src, "lxml")

        # Find the industry of the company
        industry_tag = soup.find("section", {"class": "artdeco-card p5 mb4"})
        industry = industry_tag.find_all_next(
            "dd", {"class": "mb4 text-body-small t-black--light"}
        )
        industry = industry[1].get_text().strip()
        print(industry)

        # Write the industry to csv
        with open("industry.csv", "a+", newline="", encoding="UTF8") as industry_csv:
            writer = csv.writer(industry_csv)
            writer.writerow([company, industry, query_url])

# Success message
print("All Done!")
