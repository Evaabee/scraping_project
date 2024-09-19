# Ethical Considerations for Web Scraping and how we have taken those steps in this project

## Overview

Web scraping is a powerful tool for collecting and analyzing data, but it also comes with ethical responsibilities. This document outlines the ethical considerations that were carefully taken into account while developing this web scraper, including the **purpose of data collection**, **compliance with website terms**, **responsible data handling**, and **data usage** practices.

---

## Purpose of Data Collection

The purpose of this project is to collect **stage reviews** from **The Guardian's Stage section**. The data collected includes:

- **Show Name**: The name of the performance being reviewed.
- **Review Headline**: Title summarizing the performance review.
- **Article Link**: Direct URL to the full review on The Guardian’s website.
- **Star Rating**: Rating out of 5 stars, reflecting the review's assessment.
- **Review Date**: The publication date of the review, extracted from the article 

 The goal is to organize public performance reviews in a way that makes it easier for theater enthusiasts, critics, and researchers to analyze media coverage of stage performances. This project does not collect any personal information and does not aim to infringe on any intellectual property or disrupt the host website. This is a useful tool to see the ratings of all the latest stage shows at once. 

---

## Data Sources and robots.txt Compliance

### Data Source: The Guardian

The data is collected from **The Guardian's Stage section**. **The Guardian** was chosen because it is a well-respected source of professional theater reviews and ratings.

### Respect for Website Policies

We ensure compliance with **robots.txt** and the terms of service of The Guardian:

- **robots.txt Compliance**: Before scraping, we checkd the site's `robots.txt` file at `https://www.theguardian.com/robots.txt` to ensure that our scraping activity does not violate their guidelines. If the site prohibits scraping certain parts of the website or places limits, we respect those rules.
- **No Prohibited Data Collection**: The data collected does not violate any terms set by the website. We do not attempt to scrape pages that are explicitly restricted in the site's terms of service or `robots.txt`.

### Collection Practices

We adhere to best practices to ensure that our web scraping activity is ethical and does not interfere with the normal functioning of the website:

- **Rate Limiting**: We implement rate limiting to ensure that the scraping does not overload the website's servers. We make sure not to overwhelm the host website with frequent or excessive requests.
- **Non-Intrusive Scraping**: We only scrape publicly available data (review titles, article links, and star ratings). We avoid any content behind paywalls, login walls, or password-protected areas.
- **Respect for User Privacy**: No personal user information (PII) is collected during the scraping process.
- **Sleep Intervals**: To further reduce the load on the server, our scraper includes a `sleep(2)` function between requests. This introduces a 2-second delay to avoid making rapid, consecutive requests that could potentially disrupt the website's normal operations.


---

## Data Handling and Privacy

We follow ethical guidelines for handling and storing any scraped data, ensuring both the security of the data and compliance with privacy regulations:

### Data Collected

The data we collect includes:

- Review titles, article links, and star ratings (as publicly available on The Guardian's website).

### Privacy Considerations

We do not collect or store any Personally Identifiable Information (PII) such as names, emails, or login credentials. All data collected is publicly available and does not include user-generated content.
