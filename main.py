import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of The Guardian's Stage section
url = 'https://www.theguardian.com/stage'

# Send a request to fetch the Stage section page content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Successfully fetched the Stage page.")
else:
    print("Failed to fetch the Stage page. Status code:", response.status_code)

# Parse the Stage section HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Initialize lists to store data
review_titles = []
review_links = []
star_ratings = []

# Find the article links in the Stage section (use correct tag and class)
articles = soup.find_all('a', attrs={'aria-label': True})

# Loop through each article link
for article in articles:
    # Extract the review title and link
    review_title = article['aria-label']
    review_link = 'https://www.theguardian.com' + article['href']

    # Append title and link to the lists
    review_titles.append(review_title)
    review_links.append(review_link)

    # Visit each article page to scrape the star rating
    article_response = requests.get(review_link)
    
    if article_response.status_code == 200:
        article_soup = BeautifulSoup(article_response.content, 'html.parser')

        # Find the star rating container inside the article page (adjust based on the actual class)
        star_rating_container = article_soup.find('div', class_='dcr-tdnqeh')

        if star_rating_container:
            # The 'd' attribute values that distinguish solid and empty stars
            solid_star_d = "m19.151 21.336-2.418-7.386L23 9.348l-.312-.989h-7.75L12.547 1h-1.092L9.087 8.36H1.312L1 9.347l6.267 4.602-2.366 7.386.806.624L12 17.357l6.293 4.603z"
            empty_star_d = "m14.381 13.196 3.863-2.837h-4.758l-1.479-4.547-1.462 4.547H5.756l3.855 2.831-1.438 4.488L12 14.88l3.856 2.82zm4.77 8.14-.858.624L12 17.357 5.707 21.96l-.806-.624 2.366-7.386L1 9.348l.312-.989h7.775L11.454 1h1.092l2.393 7.36h7.749l.312.988-6.267 4.602z"
            
            # Initialize counters for solid and empty stars
            solid_stars = 0
            empty_stars = 0

            # Find all <path> elements in the star rating container
            svg_paths = star_rating_container.find_all('path')

            # Loop through and count solid/empty stars
            for path in svg_paths:
                if path['d'] == solid_star_d:
                    solid_stars += 1
                elif path['d'] == empty_star_d:
                    empty_stars += 1

            # Total stars is the sum of solid and empty stars
            total_stars = solid_stars + empty_stars
            star_ratings.append(f'{solid_stars}/{total_stars}')
        else:
            star_ratings.append('No Rating')  # If no star rating is found
    else:
        star_ratings.append('No Rating')  # If the article page request fails

# Create a DataFrame to store the scraped data
data = {
    'Review Title': review_titles,
    'Article Link': review_links,
    'Star Rating': star_ratings
}

df = pd.DataFrame(data)

# Save the data to a CSV file with headers and formatted star ratings
csv_file_name = 'guardian_stage_reviews_with_stars.csv'
df.to_csv(csv_file_name, index=False)

# Display a preview of the DataFrame in the console
print(f"Data saved to {csv_file_name}")
print(df.head(10))  # Show the first 10 rows for review
