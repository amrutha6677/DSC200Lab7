DSC 200 – Data Wrangling
Lab 7: Web Scraping

Goals:
• Determine websites that are “scrapable”
• Use pandas, beautifulsoup4, and requests Python libraries to scrape and store data from
a website

Instructions:
1. Choose two websites, review their terms of reference, and determine whether the
websites allow bots and scripts to scrape its contents. For each website reproduce (copy
and paste) the portion of the site’s terms of use and robots.txt file detailing their web
scraping policy. Store this information in an MS Word document. Remember to include
the URL to the terms of reference. Your submission for this task should be a written
two-page written report detailing the following for each of the websites: an introduction
to the website (i.e. what the website is about, the business domain, why you choose
that website, etc.), a summary of the salient points about web scraping as published in
their stated policies, etc. The appendices to this short report must include the contents
of the robots.txt files for each of the websites. Provide one appendix for each of the
websites. Make sure the report is properly structured for ease of reading. 20 marks

2. Choose one of the websites listed in task 1 and write a simple function that returns one
of the pages that the website allows to be web scraped. Save the contents of the
webpage in a properly formatted file (CSV). Name the output file using the following
format: group_[your group number]_task2.csv. 20 marks

3. Given the following URLs, write a separate function for each of the data sources. Each
function should pandas, beautifulsoup4, and request libraries to scrape the contents of
each page and store the results in a separate CSV file. For each URL, the script should
print the number of rows and columns to the screen. Also name the downloaded files
using a format the includes your group name and an indication of the source of the
data.
a. https://vincentarelbundock.github.io/Rdatasets/datasets.html.This page
contains a list of headers that can be used to create the dataset. Randomly select
a linked CSV file and download the file.
b. https://realpython.github.io/fake-jobs/. Use the following as headers for the file:
job_title, company_name, city, state, posting_date.
40 marks
Make sure to include a main function that calls each of the functions referenced above. If you
are interested in a challenge, you may choose to create a Python class the accepts the URL of
the data source and output file name as constructor parameters, and a function that retrieves
the contents of the webpage and saves it to a CSV file. You may want to use this class for each
of tasks 2 and 3. (This may require creating 3 instances of the class you create and call each
instance to retrieve the contents of the URL.)

Submission:
You are required to submit two files via the Canvas assignment from which this assignment is
linked:
1. A word document containing the response to question 1. The file should be names:
group_[your_group_number]_Lab7_part1.docx
2. A python script containing the code that answers questions 2 and 3. Name the file using
the following format: group_[your_group_number]_Lab7_parts2n3.py
