from bs4 import BeautifulSoup
import requests
import pandas as pd


# print(soup.prettify())
# more_pages = True
# page = 1
# data = []

# # print(page)
# url = f"https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/{page}"
# response = requests.get(url)

# response.encoding = "utf-8"
# top_salaries = response.text
# soup = BeautifulSoup(top_salaries, "html.parser")
# rows = soup.find_all(class_="data-table__row")
# column_names = []
# # next = soup.find(class_ = "pagination__next-btn")
# # print(rows[0])
# for row in rows:
#     row_data = []
#     for cell in row.find_all("td"):
#         cell = cell.text.split(":")
#         row_data.append(cell[1])
#         if cell[0] not in column_names:
#             column_names.append(cell[0])
        
#     # print(cell.text)
#     data.append(row_data)
    
# print("columns: ", column_names)
# print(data)


# df = pd.DataFrame(data, columns=column_names)
# print(df)
# print(len(df))
# row_data = [row.getText() for row in rows]
# print(row_data)
# print(df)
# active_pg = pg.find('li', 'active')
# # print(next_url)


more_pages = True
page = 1
data = []
column_names = []

while more_pages:
    print(page)
    url = f"https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/{page}"
    response = requests.get(url)

    response.encoding = "utf-8"
    top_salaries = response.text
    soup = BeautifulSoup(top_salaries, "html.parser")
    rows = soup.find_all(class_="data-table__row")
    
    # next = soup.find(class_ = "pagination__next-btn")
    # print(rows[0])
    for row in rows:
        row_data = []
        for cell in row.find_all("td"):
            cell = cell.text.split(":")
            row_data.append(cell[1])
            if cell[0] not in column_names:
                column_names.append(cell[0])
            
        # print(cell.text)
        data.append(row_data)
    
    if soup.select('a.pagination__next-btn.pagination__btn--off') == []:
        page +=1
    else:
        more_pages = False
    
df = pd.DataFrame(data, columns=column_names)
# print(len(df))
# row_data = [row.getText() for row in rows]
# print(row_data)
print(df)
# active_pg = pg.find('li', 'active')
# print(next_url)