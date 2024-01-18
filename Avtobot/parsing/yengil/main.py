from bs4 import BeautifulSoup
import requests, json, time
from pprint import pprint
headers = {
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "referer":"https://avtoelon.uz/avto/chevrolet/?price-currency=1"
}

def get_page(url):
    site = requests.get(url=url, headers=headers)
    return site if site.status_code == 200 else False

def get_phone(id):
    # headers["x-requested-with"] = "XMLHttpRequest"
    # headers["referer"] = f"https://avtoelon.uz/uz/a/show/{id}"
    # site = requests.get(url=f"https://avtoelon.uz/uz/a/ajaxPhones/?id={id}", headers=headers)
    return id

def get_detail(url):
    avtodetails_page = get_page(url)
    htmldom = BeautifulSoup(avtodetails_page.text, "lxml")
    try:
        description_datas = htmldom.find("div", class_="description-body").find_all("dd",class_="clearfix")
    except:
        description_datas = "Topilmadi!"
    try:
        datas = ", ".join([data.text.strip() for data in description_datas])
    except:
        datas = "topilmadi"
    try:
        add = ", ".join([span.text.strip() for span in htmldom.find("ul", class_="params-block__list").find_all("span")])
    except:
        add = "topilmadi"
    try:
        phone = url.split("/")[-1]['data']['model']['phone']
    except:
        phone = "topilmadi"
    try:
        images = htmldom.find(class_="main-photo").find("img")['src']
    except:
        images = "topilmadi"
    try:
        description = htmldom.find(class_="description-text").text.strip()
    except:
        description = "topilmadi"




    avto = {
        "title": htmldom.find("h1", class_="a-title__text").text.strip(),
        "details": datas,
        "more": add,
        "images": images,
        "description": description,
        "phone": f"https://avtoelon.uz/uz/a/ajaxPhones/?id={phone}"
    }
    return avto

def get_items(htmldom):
    items = htmldom.select("div#results > script")
    results = []
    for scr in items:
        scr = scr.text.strip().replace("listing.items.push(", "").replace(");", "")
        scr = json.loads(scr)
        detail = get_detail(scr['url'])
        scr['detail'] = detail
        results.append(scr)
    return results
def yengil_parser():
    print("Yengil Avtomobillar Parseri ishga tushdi!")
    for num_page in range(1, 2):
        html = get_page(f"https://avtoelon.uz/uz/avto/chevrolet/?page={num_page}")
        htmldom = BeautifulSoup(html.text, "lxml")
    

        items = get_items(htmldom)
        with open(f"page_Avto.json", "w", encoding="UTF8") as file:
            json.dump(items, file, indent=4)
            print(f"Fayl {num_page}saqlandi!")


