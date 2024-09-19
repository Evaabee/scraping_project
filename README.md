# The Guardian Stage Reviews Scraper

## Overview

This project is a web scraper built using **Python** and **BeautifulSoup** to extract stage reviews from **The Guardian**. The scraper uncovers **stage performance reviews** from the "Stage" section, including the **title of the review,date and the article link**, and also the **star rating** for each performance.

The purpose of this project is to provide an organized dataset of stage reviews, making it easier for theater enthusiasts, critics, and researchers to analyze media coverage and critical reception of various performances.

---

## Data Uncovered

This scraper pulls the following data from each article in The Guardian's Stage section:

- **Show Name**: The name of the performance being reviewed.
- **Review Headline**: Title summarizing the performance review.
- **Article Link**: Direct URL to the full review on The Guardian’s website.
- **Star Rating**: Rating out of 5 stars, reflecting the review's assessment.
- **Review Date**: The publication date of the review, extracted from the article URL.



### Example Data:

| Show Name                              | Review Headline                           | Article Link                                 | Star Rating | Review Date  |
|----------------------------------------|-------------------------------------------|----------------------------------------------|-------------|--------------|
| Ben Elton: Authentic Stupidity         | Authentic Stupidity review                | [Link](https://www.theguardian.com/stage/...) | 4/5         | 2024/sep/18  |
| [More Show Names]                      | [More Headlines]                          | [More Links]                                | No Rating   | No Date      |

---

## Website Used

The website chosen for this project is **[The Guardian's Stage section](https://www.theguardian.com/stage/stage+tone/reviews)**. It was selected because The Guardian is a well-established media outlet that regularly publishes high-quality reviews of theater performances, often accompanied by detailed star ratings.

### Why This Website Was Chosen:

- **High-Quality Reviews**: The Guardian provides professional and critical stage reviews, making it a valuable source for those interested in performing arts.
- **Star Ratings**: Many reviews include a 5-star rating system, which provides useful insights for performance analysis.
- **Consistency**: The site structure allows for consistent scraping of data.

---

## How to Run the Scraper

To run this scraper on your local machine, follow the steps below:

### 1. **Clone the Repository**
   git clone https://github.com/Evaabee/scraping_project.git

### 2. **Install Dependencies**
    cd guardian-stage-reviews-scraper
    pip install -r requirements.txt

The required Python packages are listed in requirements.txt

- Python 3.x
- requests
- BeautifulSoup4
- Pandas

### 3. **Run the Scrapper**
    python main.py

You will be prompted to enter the number of latest pages to scrape. The script will fetch the reviews, star ratings, and publication dates, and save the data to a CSV file named guardian_stage_reviews_with_stars.csv.