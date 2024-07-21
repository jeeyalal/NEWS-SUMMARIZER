# use nlp also
import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article


# function for btn summarize
def summarize():
    url = utext.get("1.0", "end").strip()
    article = Article(url)
    article.download()
    article.parse()

    nltk.download("punkt")
    article.nlp()

    title.config(state="normal")
    author.config(state="normal")
    publication.config(state="normal")
    summary.config(state="normal")
    sentiment.config(state="normal")

    title.delete("1.0", "end")
    title.insert("1.0", article.title)
    author.delete("1.0", "end")
    author.insert("1.0", article.authors)
    publication.delete("1.0", "end")
    publication.insert("1.0", article.publish_date)
    summary.delete("1.0", "end")
    summary.insert("1.0", article.summary)

    # sentiment analysis

    analysis = TextBlob(article.text)
    sentiment.delete("1.0", "end")
    sentiment.insert(
        "1.0",
        f'Polarity: {analysis.polarity},sentiment : {"positive " if analysis.polarity>0 else "negative" if analysis.polarity <0 else "neutral"}',
    )

    title.config(state="disabled")
    author.config(state="disabled")
    publication.config(state="disabled")
    summary.config(state="disabled")
    sentiment.config(state="disabled")


# GUI
root = tk.Tk()
root.title("NEWS summarizer")
root.geometry("1200x600")

# title

tlable = tk.Label(root, text="Title")
tlable.pack()

title = tk.Text(root, height=1, width=140)
title.config(state="disabled", bg="#dddddd")
title.pack()

# author table
alable = tk.Label(root, text="Author")
alable.pack()

author = tk.Text(root, height=1, width=140)
author.config(state="disabled", bg="#dddddd")
author.pack()

# publicatopn date table
plable = tk.Label(root, text="Publishing date")
plable.pack()

publication = tk.Text(root, height=1, width=140)
publication.config(state="disabled", bg="#dddddd")
publication.pack()

# summary box
slable = tk.Label(root, text="Summary")
slable.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state="disabled", bg="#dddddd")
summary.pack()

# sentiment box
slabel = tk.Label(root, text="Sentiment")
slable.pack()

sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state="disabled", bg="#dddddd")
sentiment.pack()

# url box
ulabel = tk.Label(root, text="URL")
ulabel.pack()

utext = tk.Text(root, height=1, width=140)
utext.pack()

btn = tk.Button(root, text="summarize", command=summarize)
btn.pack()


root.mainloop()
