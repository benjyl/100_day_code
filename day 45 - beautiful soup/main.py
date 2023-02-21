from bs4 import BeautifulSoup
import lxml

with open("website.html", 'r', encoding="utf8") as file:
    contents = file.read()
    
soup = BeautifulSoup(contents, "html.parser")

# print(soup.title)
# print(soup.title.string)
# print(soup.prettify()) # get all html data indented together
# print(soup.a) # get first anchortag

all_anchor_tags = soup.find_all(name="a") # get all anchortags
print(all_anchor_tags)

for tag in all_anchor_tags:
    # print(tag.getText()) # get names of all tags
    print(tag.get("href")) # get all hrefs
    
heading = soup.find(name="h1", id="name") #gets content assosciated with given id
print(heading)
# class is reserved keyword, cannot be used as keyword, can only be used for creating a class
# therefore use class_
section_heading = soup.find(name="h3", class_="heading") 
print(section_heading.getText())

# select gives all matching items, select_one gives first matching item
# To select by id, selector = "#idname"
# select by class, selector = ".classname"
company_url = soup.select_one(selector="p a") # "p a" means an anchor tag inside a paragraph tag
print(company_url)