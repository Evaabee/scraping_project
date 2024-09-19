import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time

base_url = 'https://www.theguardian.com/stage/stage+tone/reviews?page=' 

num_pages = int(input("Enter the number of latest pages to scrape: "))

review_dates = []
review_shows = []
review_headlines = []
review_links = []
star_ratings = []

for page in range(1, num_pages + 1):
    url = base_url + str(page)
    #send a request to fetch the Stage section page content
    response = requests.get(url)

    #check if request was successful
    if response.status_code == 200:
        print("Successfully fetched page number ", page)
    else:
        print("Failed to fetch page number ", page, ". Status code:", response.status_code)

    #parse the Stage section html content
    soup = BeautifulSoup(response.content, 'html.parser')




    #find  article links in the Stage section
    articles = soup.find_all('a', attrs={'aria-hidden': True})

    #loop through each article link 
    for article in articles:
        review_title = article.get_text().strip()
        review_link = article['href']
        match = re.match(r"^(.*) review\s*[-–]\s*(.*)$", review_title)
        if match:
            show = match.group(1).strip()
            headline = match.group(2).strip()


        # Extract the date from the URL (assuming the URL contains the date in YYYY/MM/DD format)
        date_match = re.search(r'/(\d{4}/\w{3}/\d{2})/', review_link)
        review_date = date_match.group(1) if date_match else None
        review_dates.append(review_date)
        review_shows.append(show)
        review_headlines.append(headline)
        review_links.append(review_link)

        #visit each article page to scrape the star rating
        article_response = requests.get(review_link)
        
        if article_response.status_code == 200:
            article_soup = BeautifulSoup(article_response.content, 'html.parser')

            star_rating_container = article_soup.find('div', class_='dcr-tdnqeh')

            if star_rating_container:
                solid_star_d = "m19.151 21.336-2.418-7.386L23 9.348l-.312-.989h-7.75L12.547 1h-1.092L9.087 8.36H1.312L1 9.347l6.267 4.602-2.366 7.386.806.624L12 17.357l6.293 4.603z"
                empty_star_d = "m14.381 13.196 3.863-2.837h-4.758l-1.479-4.547-1.462 4.547H5.756l3.855 2.831-1.438 4.488L12 14.88l3.856 2.82zm4.77 8.14-.858.624L12 17.357 5.707 21.96l-.806-.624 2.366-7.386L1 9.348l.312-.989h7.775L11.454 1h1.092l2.393 7.36h7.749l.312.988-6.267 4.602z"

                solid_stars = 0
                empty_stars = 0

                svg_paths = star_rating_container.find_all('path')

                #count solid/empty stars
                for path in svg_paths:
                    if path['d'] == solid_star_d:
                        solid_stars += 1
                    elif path['d'] == empty_star_d:
                        empty_stars += 1

                total_stars = solid_stars + empty_stars
                star_ratings.append(f'{solid_stars}/{total_stars}')
            else:
                review_dates.remove(review_date)
                review_shows.remove(show)
                review_headlines.remove(headline)
                review_links.remove(review_link)
        else:
            review_dates.remove(review_date)
            review_shows.remove(show)
            review_headlines.remove(headline)
            review_links.remove(review_link)
    # sleep for 2 seconds between each page
    time.sleep(2)

data = {
    'Review Date' : review_dates,
    'Show': review_shows,
    'Headline' : review_headlines,
    'Article Link': review_links,
    'Star Rating': star_ratings
}

df = pd.DataFrame(data)

csv_file_name = 'guardian_stage_reviews_with_stars.csv'
df.to_csv(csv_file_name, index=False)


print(f"Data saved to {csv_file_name}")
print(df.head(10)) 
