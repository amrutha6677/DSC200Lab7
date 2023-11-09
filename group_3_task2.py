import requests
import csv
from bs4 import BeautifulSoup


def scrape_wikipedia_friends_episodes():
    url = "https://en.wikipedia.org/wiki/List_of_Friends_episodes"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return

    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract and save data from the Wikipedia page
    with open("group_3_task2.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file)

        # Write the header row with the desired columns
        writer.writerow(
            ["Episode number", "Directed by", "Written by", "Original air date", "Prod. code",
             "U.S. viewers (millions)"])

        # Extract data and write to the CSV
        for row in soup.select("table.wikitable tbody tr")[2:]:  # Skip the first two header rows
            columns = row.find_all("td")
            if len(columns) >= 8:  # Make sure you have enough columns
                episode_number = columns[0].get_text(strip=True)
                title = columns[2].get_text(strip=True)
                directed_by = columns[3].get_text(strip=True)
                written_by = columns[4].get_text(strip=True)
                original_air_date = columns[5].get_text(strip=True)
                prod_code = columns[6].get_text(strip=True)
                us_viewers_millions = columns[7].get_text(strip=True)

                writer.writerow(
                    [episode_number, title, directed_by, written_by, original_air_date, prod_code,
                     us_viewers_millions])

    print("Data scraped and saved to 'group_3_task2.csv'")


if __name__ == "__main__":
    scrape_wikipedia_friends_episodes()