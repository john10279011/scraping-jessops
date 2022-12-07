from bs4 import BeautifulSoup
from requests_html import HTMLSession
import pandas as pd


data = []


def getcontent(soup):
    items = soup.find_all("div", class_="f-grid prod-row")
    for item in items:
        name = item.find("h4").text
        price = item.find("p", class_="price larger").text
        url = str("https://www.jessops.com/") + str(item.find("h4").find("a")["href"])
        itm = {"name": name, "price": price, "product link": url}
        print(itm)
        data.append(itm)
    return


for i in range(1, 1150, 21):
    sesh = HTMLSession()
    page = sesh.get(
        f"https://www.jessops.com/accessories?fh_start_index={i}&fh_view_size=21"
    )
    soup = BeautifulSoup(page.content, "html.parser")
    print(i)
    getcontent(soup)


items = pd.DataFrame(data)
items.to_csv("jessops.csv", index=False)
print(items)
