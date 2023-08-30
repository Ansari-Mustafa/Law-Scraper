# LawScraper - Extracting Municipal Laws from Municode

LawScraper is a powerful and versatile Python-based web scraping program designed to extract municipal laws and regulations from the Municode website (https://library.municode.com/). The program utilizes Selenium libraries to automatically navigate through the website's pages, gather relevant legal information, and organize it into a structured format for further analysis and use. The program employs automated navigation to traverse through the Municode website, simulating user interactions. It dynamically adapts to the website's structure, ensuring accurate data retrieval even as the website evolves.

## Key Features:

Dynamic Interaction: Leveraging the Selenium library, LawScraper-Selenium automates interactions with the Municode website by mimicking user actions. This approach allows the program to navigate dynamically through pages, handle JavaScript-rendered content, and capture data that traditional scraping methods might miss.

User-Defined Parameters: The program offers a user-friendly command-line interface where users can define search parameters, such as the target municipality, specific legal topics, or date ranges. This customization empowers users to focus the scraping process according to their requirements.

Automated Data Extraction: LawScraper employs Selenium's browser automation capabilities to extract relevant information from the Municode pages. It collects data including law titles, sections, descriptions, and associated legal codes.

Structured Data Output: Extracted data is organized into a structured format, often saved as .txt, .doc or .pdf files. This structured representation ensures easy storage, sharing, and integration with various data analysis tools.

Advanced Filtering: Users can apply custom filters to narrow down the scraped content, enabling extraction of laws that match specific criteria. This feature streamlines the process of obtaining precise legal information.

Flexibility and Extensibility: The modular architecture of the program allows for easy updates and expansions. As the Municode website evolves or scraping requirements change, LawScraper can be adapted to accommodate these modifications.

## Use Cases:

Legal Research: Legal professionals, researchers, and academics can benefit from LawScraper to gather comprehensive data for legal analysis and research endeavors.
Policy Insights: Government entities and policymakers can extract and analyze regulations from specific jurisdictions, aiding in informed policy-making.
Compliance Management: Businesses can monitor local regulations by regularly scraping and reviewing changes, ensuring continuous compliance.
Educational Purposes: Law schools can utilize LawScraper to provide students with real-world examples of legal documents and their practical implications.

## How To Use:

Please note, this guide might not 'exactly' be applicable for the current version.
1. The 'constants.py' file in the Functions folder contains detailed configurations for the program that can be edited accordingly.
2. After configuring the program for the specific USA State and county, you can enter your search term in the 'run.py' file as a string.
3. Functions for downloading both docs or pdfs are defined. (Use which ever in 'run.py')
4. Some extra/additional functions are saved in 'extras.txt' file
The 'SaveStates.py' file can be run to save a list of all the States and Cities on the Municode webpage. (No need to re-run)

## Note: 
While LawScraper offers a powerful means of extracting legal information from Municode, users should verify the accuracy and completeness of scraped data due to potential errors during the scraping process.
