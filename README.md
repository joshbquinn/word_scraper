# Word Scraper 

The program scrapes keywords, nouns and verbs from a URL and stores them in .txt files.

- Creates a list of words from a specified URL.
- Creates a unique directory (url name + datetime stamp) to store any .txt files.
- Creates generic lists of common words, nouns and verbs to cross check the URL list against. 
- Cleans up the URL list to remove unwanted elements (HTML, JavaScripts etc) and leave only the text. 
- Cross checks the URL list of words against the common words, noun and verb lists.
- Common words removed from URL list 
- Matched noun and verb lists created 
- Keyword, and noun and verb matches written to .txt files 
- Files stored in a unique directory each time the program is run.

# Instructions 

Pipeline script from SCM: to configure the job in Jenkins Pipeline add the following git repo with default master branch:  
https://github.com/joshbquinn/word_scraper.git

To run from command line:
- navigate to application directory
- enter command: py main.py "url_string" # URL string must be between double quotes ("")
- If a URL is not specified a default URL string will run. 

# Future changes

Application Structure:
- Modularise the files correctly
- Add classes
- Add inheritance 
- Ensure program is secured properly 
- Implement OO Design Principles 


Usability and functionality:
- More generic usability across various URLs
- More robust regex functions to clean up URL list of words


UI: 
- Simple frontend interface to add a URL to scrape from, display found keywords and option to download the .txt file.

# Future Pipeline extensions
- Browser testing 
- Archive test results 