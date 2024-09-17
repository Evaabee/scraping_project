# The Guardian Stage Reviews Scraper

## Overview

This project is a web scraper built using **Python** and **BeautifulSoup** to extract stage reviews from **The Guardian**. The scraper uncovers **stage performance reviews** from the "Stage" section, including the **title of the review, the article link**, and the **star rating** for each performance.

The purpose of this project is to provide an organized dataset of stage reviews, making it easier for theater enthusiasts, critics, and researchers to analyze media coverage and critical reception of various performances.

---

## Data Uncovered

This scraper pulls the following data from each article in The Guardian's Stage section:

1. **Review Title**: The title of the stage review, which summarizes the performance being reviewed.
2. **Article Link**: A direct URL to the full review on The Guardian’s website.
3. **Star Rating**: A rating out of 5 stars, which reflects the critical assessment of the performance. The rating is scraped directly from the review page.

### Example Data:

| Review Title                          | Article Link                          | Star Rating |
| ------------------------------------- | ------------------------------------- | ----------- |
| Ben Elton: Authentic Stupidity review | https://www.theguardian.com/stage/... | 4/5         |
| [More Review Titles]                  | [More Links]                          | 3/5         |

---

## Website Used

The website chosen for this project is **[The Guardian's Stage section](https://www.theguardian.com/stage)**. It was selected because The Guardian is a well-established media outlet that regularly publishes high-quality reviews of theater performances, often accompanied by detailed star ratings.

### Why This Website Was Chosen:

- **High-Quality Reviews**: The Guardian provides professional and critical stage reviews, making it a valuable source for those interested in performing arts.
- **Star Ratings**: Many reviews include a 5-star rating system, which provides useful insights for performance analysis.
- **Consistency**: The site structure allows for consistent scraping of data.

---

## How to Run the Scraper

To run this scraper on your local machine, follow the steps below:

### 1. **Clone the Repository**

### 2. **Install Dependencies**

The required Python packages are listed in requirements.txt

- Python 3.x
- BeautifulSoup
- Pandas
