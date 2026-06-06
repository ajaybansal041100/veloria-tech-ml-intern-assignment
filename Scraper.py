import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://www.howstat.com/cricket/Statistics/Matches/MatchList_ODI.asp"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Referer": "http://www.howstat.com/"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

tables = soup.find_all("table")

# Table 0 contains the ODI match list
rows = tables[0].find_all("tr")

matches = []

for row in rows:
    cols = row.find_all("td")

    if len(cols) >= 6:

        date = cols[0].get_text(strip=True)
        series = cols[1].get_text(strip=True)
        match = cols[2].get_text(strip=True)
        venue = cols[3].get_text(strip=True)
        result = cols[4].get_text(strip=True)

        matches.append({
            "Date": date,
            "Series": series,
            "Match": match,
            "Venue": venue,
            "Winner": result
        })

df = pd.DataFrame(matches)

# Remove empty rows
df = df[df["Date"] != ""]

# Keep only latest 20 matches
df = df.head(20)

df.to_csv("match_data.csv", index=False)

print(df.head())
print("\nSaved match_data.csv")