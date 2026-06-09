from bs4 import BeautifulSoup
import requests
import pandas as pd

# motorsportstats.com splits the race history across multiple pages.
# Each URL below corresponds to one page of Lewis Hamilton's F1 start records.

base_url = 'https://www.motorsportstats.com/driver/lewis-hamilton/stats/series/fia-formula-one-world-championship/starts'
urls = [f"{base_url}?page={i}" for i in range(1, 5)]

dataframes = []

for url in urls:
    # Fetch the page and parse its HTML
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Locate the stats table on the page
    table = soup.find('table')

    # Extract column headers from <th> elements
    titles = soup.find_all('th')
    table_titles = [title.text.strip() for title in titles]

    # Extract all rows from the table
    rows_data = table.find_all('tr')

    all_rows = []
    for row in rows_data:
        # Pull text content from each cell in the row
        row_data = row.find_all('td')
        individual_row_data = [data.text.strip() for data in row_data]
        all_rows.append(individual_row_data)

    # Build a DataFrame from this page and store it
    df = pd.DataFrame(all_rows, columns=table_titles)
    dataframes.append(df)

# Concatenate all pages into one complete dataset
combined_df = pd.concat(dataframes, ignore_index=True)