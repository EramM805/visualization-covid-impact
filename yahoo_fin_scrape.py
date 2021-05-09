import requests
from bs4 import BeautifulSoup as bs
import csv

def djia_fetcher(period1, period2):
    """ 
    This function will fetch Dow Jones Industrial Average historical data from yahoo news.
    Input: 2 epoch time data, from period1 to period2
    Output: A tuple of headings and the body of the table
    """
    url = f"https://finance.yahoo.com/quote/%5EDJI/history?period1={period1}&period2={period2}&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true"
    try:
        page = requests.get(url)
        page.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("HTTP Error:", e)
    except requests.exceptions.ConnectionError as e:
        print("Error Connecting:", e)
    except requests.exceptions.Timeout as e:
        print("Timeout Error:", e)
    except requests.exceptions.RequestException as e:
        print("Request exception: ", e)

    # Parsing & Organizing Data
    headings = []  # A container to hold headings in the table
    data = []     # A container to hold contents in the table
    soup = bs(page.content, "lxml")
    table = soup.table
    # Read in table headings
    table_head = table.find('thead')
    table_headrows = table_head.find_all('th')
    for row in table_headrows:
        col = row.text.strip()
        headings.append(col.replace('*', ''))

    # Read in body content
    table_body = table.find('tbody')
    table_bodyrows = table_body.find_all('tr')
    for row in table_bodyrows:
        cols = row.select('td span')
        cols = [col.get_text() for col in cols]
        data.append(cols)

    return (headings,data)

data_2020 = djia_fetcher(1577836800,1609459200)
print(data_2020)
data_2008 = djia_fetcher(1199145600,1230768000)
print(data_2008)

filename = "DJIA.csv"

#with open(filename, 'w') as csvfile: 

    #csvwriter = csv.writer(csvfile)

    #csvwriter.writerows(body1)
    #csvwriter.writerows(data2_2008)


