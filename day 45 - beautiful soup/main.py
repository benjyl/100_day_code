from bs4 import BeautifulSoup
import lxml
import requests
import numpy as np


response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text
soup=BeautifulSoup(yc_webpage, "html.parser")
# print(soup.title)

articles = soup.find_all(name="span", class_="titleline") # get anchortag of first article
titles = soup.select_one(".titleline a").getText()
# print(titles)
# gets first anchor tag of span tag, above method got both anchor tags
article_titles = [article.a.get_text(strip=True) for article in articles]
article_links = [article.a.get("href") for article in articles]
# get integer upvotes score
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

max_ind = np.argmax(article_upvotes)
print(article_titles[max_ind], article_links[max_ind], article_upvotes[max_ind])

# print(article_titles)
# print(article_links)
# print(article_upvotes)

# print(titles)

# with open("website.html", 'r', encoding="utf8") as file:
#     contents = file.read()
    
# soup = BeautifulSoup(contents, "html.parser")

# # print(soup.titles)
# # print(soup.titles.string)
# # print(soup.prettify()) # get all html data indented together
# # print(soup.a) # get first anchortag

# all_anchor_tags = soup.find_all(name="a") # get all anchortags
# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     # print(tag.getText()) # get names of all tags
#     print(tag.get("href")) # get all hrefs
    
# heading = soup.find(name="h1", id="name") #gets content assosciated with given id
# print(heading)
# # class is reserved keyword, cannot be used as keyword, can only be used for creating a class
# # therefore use class_
# section_heading = soup.find(name="h3", class_="heading") 
# print(section_heading.getText())

# # select gives all matching items, select_one gives first matching item
# # To select by id, selector = "#idname"
# # select by class, selector = ".classname"
# company_url = soup.select_one(selector="p a") # "p a" means an anchor tag inside a paragraph tag
# print(company_url)
