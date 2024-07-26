### NEWS-SUMMARIZER

**Overview:**
The NEWS-SUMMARIZER project is a Python-based application that extracts and summarizes news articles from a given URL. It uses several natural language processing (NLP) libraries to achieve this functionality.

**Features:**
- **News Article Extraction:** Fetches and processes articles from URLs.
- **Summarization:** Summarizes the content of the articles.
- **Sentiment Analysis:** Analyzes the sentiment of the article text.

**Libraries Used:**
- **Tkinter:** For creating the graphical user interface (GUI).
- **NLTK:** For natural language processing tasks.
- **TextBlob:** For sentiment analysis.
- **Newspaper3k:** For extracting and processing news articles.

**Usage:**
- **GUI Elements:** Input for URL, display for title, author, publication date, summary, and sentiment.
- **Actions:** Users input the URL of a news article, and the application displays the summarized content along with sentiment analysis.

**Setup Instructions:**
1. **Install Dependencies:** Install the required libraries using pip.
2. **Run Application:** Execute the Python script to launch the GUI.
3. **Input URL:** Enter the URL of the news article to get the summary and sentiment analysis.

This project simplifies the process of extracting and analyzing news articles, making it easier for users to get concise information and understand the sentiment behind the news.

### Output 


![image](https://github.com/user-attachments/assets/d3968e6e-9fd1-4f7d-ab9d-5dbaa221af80)








Description:
Title Section: A label "Title" followed by a text box to display the article's title.
Author Section: A label "Author" followed by a text box to display the authors of the article.
Publication Date Section: A label "Publishing Date" followed by a text box to display the publication date.
Summary Section: A label "Summary" followed by a large text box to display the summarized content of the article.
Sentiment Section: A label "Sentiment" followed by a text box to display the sentiment analysis result.
URL Section: A label "URL" followed by a text box for the user to input the article URL.
Summarize Button: A button labeled "Summarize" to trigger the summarization process.
