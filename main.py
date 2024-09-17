import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.theguardian.com/stage' 

#send a request to fetch the Stage section page content
response = requests.get(url)

#check if  request was successful
if response.status_code == 200:
    print("Successfully fetched the Stage page.")
else:
    print("Failed to fetch the Stage page. Status code:", response.status_code)

#parse the Stage section html content
soup = BeautifulSoup(response.content, 'html.parser')


review_titles = []
review_links = []
star_ratings = []

#find  article links in the Stage section
articles = soup.find_all('a', attrs={'aria-label': True})

#;oop through each article link 
for article in articles:
    review_title = article['aria-label']
    review_link = 'https://www.theguardian.com' + article['href']

    if '/stage/2024' in review_link:
        review_titles.append(review_title)
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
                star_ratings.append('No Rating')  
        else:
            star_ratings.append('No Rating')  


data = {
    'Review Title': review_titles,
    'Article Link': review_links,
    'Star Rating': star_ratings
}

df = pd.DataFrame(data)

csv_file_name = 'guardian_stage_reviews_with_stars.csv'
df.to_csv(csv_file_name, index=False)


print(f"Data saved to {csv_file_name}")
print(df.head(10)) 
