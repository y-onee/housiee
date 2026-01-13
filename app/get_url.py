from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re
import pandas as pd

df = pd.read_csv("data/nova_scotia_without_prices.csv", dtype=str)

options = webdriver.ChromeOptions()
options.add_argument('--headless=new')

driver = webdriver.Chrome(options=options)

# address = "10 CLARKE AVE COXHEATH"

def get_data(address):
    try:
        driver.get("https://www.viewpoint.ca/")
        print(f"Current URL: {driver.current_url}")
        
        search_box = driver.find_element(By.NAME, "search")
        search_box.send_keys(address)
        search_box.send_keys(Keys.RETURN)
        
        time.sleep(4)
        
        # Find the first listing
        listing = driver.find_element(By.CLASS_NAME, "vpiw-nolisting")
        table = listing.find_element(By.CLASS_NAME, "vpiw-nolisting-info-table")
        rows = table.find_elements(By.TAG_NAME, "tr")

        assessment = "N/A"
        pid = "N/A"
        lot_size = "N/A"

        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) != 2:
                continue
            label = cells[0].text.strip().lower()
            value = re.sub(r'[^0-9.]', '', cells[1].text)
            if 'assessment' in label:
                assessment = value
            elif 'pid' in label:
                pid = value
            elif 'lot size' in label:
                lot_size = value

        print(f"Assessment: {assessment}, PID: {pid}, Lot Size: {lot_size}")
        
        results_url = driver.current_url
        print(f"Results URL: {results_url}")
        return assessment, pid, lot_size
    
    except Exception as e:
        print(f"Error for {address}: {e}")
        return "N/A", "N/A", "N/A"
        
# Lists to store results
assessments = []
pids = []
lot_sizes = []

for index, row in df.iterrows():
    address = f"{row['Civic Number']} {row['Civic Street Name']} {row['Civic Street Suffix']}, {row['Civic City Name']}"
    print(f"Processing: {address}")
    assessment, pid, lot_size = get_data(address)
    assessments.append(assessment)
    pids.append(pid)
    lot_sizes.append(lot_size)
        
# Quit driver after all addresses
driver.quit()

# Append results to dataframe
df["Assessment"] = assessments
df["PID"] = pids
df["Lot Size"] = lot_sizes

# Save CSV
df.to_csv("data/nova_scotia_with_prices.csv", index=False)

# for index, row in df.iterrows():
#     address = f"{row['Civic Number']} {row['Civic Street Name']} {row['Civic Street Suffix']}, {row['Civic City Name']}"
#     print(address)
#     get_data(address)