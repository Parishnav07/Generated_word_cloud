# Simple project on Genetated word cloud 
# pip install wikipedia
# pip install wordcloud

import wikipedia
import numpy as np
import sys
from wordcloud import WordCloud, STOPWORDS
from PIL import Image  # PIL -->python image library

title = str(input("Enter the topic :"))
keyword = wikipedia.search(title)
page = wikipedia.page(keyword)
content =page.content

stopwords = set(STOPWORDS)
wordcloud = WordCloud(background_color="grey",max_words=300,stopwords= stopwords)

wordcloud.generate(content)
wordcloud.to_file('output1.jpg') #
