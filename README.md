<h1 align="center">Emscrape</h1>

<p align ="center"><b>Web scraping utility designed for max scrape, min hassle!</b></p>

<br>

## How Does Emscrape Work?

Emscrape uses a combination of beautifulsoup and selenium to scrape company data from LinkedIn based on a list of customer data the output is then saved as a csv file. The only catch is that you do need to provide the script with a linkedin account for it to be able to scrape the data (This can be a throw away account, its just required for selenium to be able to scrape the linkedin website effectively). The code is fairly basic at its core and can be easily modified to scrape other websites or to take in different types of data. Heres a basic overview of the main functions:

1. <h5>Reads system OS to determine which webdriver to use:</h5>

```py
if sys.platform.startswith("linux"):
    driver = webdriver.Chrome("drivers/linux_chromedriver", options=Options)
elif sys.platform.startswith("darwin"):
    driver = webdriver.Chrome("drivers/mac_chromedriver", options=Options)
elif sys.platform.startswith("win32"):
    driver = webdriver.Chrome("drivers/win32_chromedriver.exe", options=Options)
```

2. <h5>Logs into linkedin using selenium webdriver</h5>

```py
# Open linkedin
driver.get("https://linkedin.com/uas/login")

# Find username field and prompt for input
username = driver.find_element_by_id("username")
username.send_keys(input("Enter your username: "))

# Find password field and prompt for input
pword = driver.find_element_by_id("password")
pword.send_keys(getpass("Enter your password: "))

# Log in
driver.find_element_by_xpath("//button[@type='submit']").click()
```

3. <h5>Reads in customer data from JSON file. This can be modified to read in data from a csv file</h5>

```py
# Read mock customer data from file (replace with real customer data later)
with open("customer_db.json", "r") as customer_db:
    mock_data = json.load(customer_db)

# Loop through the mock data to get company name and email
print("Fetching Results...")
for customer in mock_data:
    company = customer["company"]
```

4. <h5>Searches for company on linkedin</h5>

```py
# Create search query for each customers company
query_url = f"https://www.linkedin.com/company/{company}/about/"
driver.get(query_url)
```

5. <h5>Scrapes company data from linkedin source code</h5>

```py
# Get page source code
src = driver.page_source
# Parse page source code
soup = BeautifulSoup(src, "lxml")
```

6. <h5>Isolates the information we want to scrape from the source code</h5>

```py
# Find the industry of the company
industry_tag = soup.find("section", {"class": "artdeco-card p5 mb4"})
industry = industry_tag.find_all_next("dd", {"class": "mb4 text-body-small t-black--light"})
industry = industry[1].get_text().strip()
print(industry)
```

7. <h5>Saves the scraped data to a csv file</h5>

```py
# Write the industry to csv
with open("industry.csv", "a+", newline="", encoding="UTF8") as industry_csv:
    writer = csv.writer(industry_csv)
    writer.writerow([company, industry, query_url])
```

---

### Getting Started

The only prerequisite is a working installation of Python so feel free to skip the below steps if you already have Python installed on your system. There are a number of ways you can install Python, the below is my personal preference but of course feel free to install Python on your machine in any manner you prefer.

### Windows

Use the keyboard shortcut `WIN` + `X` followed by `I` to open powershell then copy and paste the following commands to get up and running.

> Note: You may need to close and reopen your terminal after installing miniconda.<br>Note: When the installer asks if you wish to initialize Miniconda3 **select yes**.

```sh
cd ~/Downloads/
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe --output miniconda.exe
./miniconda.exe
conda create -n emscrape python=3.9.7
conda activate emscrape
git clone https://github.com/jodisfields/emscrape.git
cd emscrape
pip install -r requirements.txt
python emscrape.py
```

---

## Mac / Linux

I have NOT personally tested this on a Mac however as it is a Unix based operating system at its core I dont expect any issues. So if you're on a Mac press `Command` + `Space Bar`, type in `Terminal` and then open the application. Once you have the terminal open, copy and paste the following commands to get up and running.

> Note: You may need to close and reopen your terminal after installing miniconda.<br>Note: When the installer asks if you wish to initialize Miniconda3 **select yes**.

```sh
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -O ~/miniconda.sh
bash ~/miniconda.sh -b -p $HOME/miniconda
conda create -n emscrape python=3.9.7
conda activate emscrape
git clone https://github.com/jodisfields/emscrape.git
cd emscrape
pip install -r requirements.txt
python emscrape.py
```

## Usage


https://user-images.githubusercontent.com/46502355/201451986-19a887fe-5546-4b52-8f6e-ba075205187b.mp4


