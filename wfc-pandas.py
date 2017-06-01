import requests
from bs4 import BeautifulSoup
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

#Function used to pass the list, using pandas make it into a Series object, which sorts them in descending order and plotting it into a bar chart
def goPandas(word_list):

    S = pd.Series(word_list).value_counts().sort_values(ascending = False).head(25)
    plt.figure(); plt.title('Top twenty-five words in the headlines of news.ycombinator.com'); plt.xlabel('Words'); plt.ylabel('Number of occurences'); S.plot(kind='bar'); plt.show()
    
def scramble(url):
    
    #Getting the source code of the html document as text and not as byte code
    html = requests.get(url).text
    bsObj = BeautifulSoup(html,'lxml')

    #Observing the source code of ycombinator news site, all the headlines belonged to the 'a' tag with class="storylink"
    for topics in bsObj.findAll('a',{'class':'storylink'}):
        headline = topics.get_text().lower().split()
        for eachWord in headline:
                word_list.append(eachWord)

if __name__ == '__main__':

    #List comprehension to fetch the first twenty web pages of new.ycombinator.com
    Top20 = ['https://news.ycombinator.com/news?p='+str(i) for i in range(1,21)]
    word_list = []
    for url in Top20:
        scramble(url)

    goPandas(word_list)

else:

    print('the file is borrowed!')






