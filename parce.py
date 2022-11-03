import requests
from bs4 import BeautifulSoup

BASE_URL = "https://home-club.com.ua/ua/sku-90507603"


def parse_page():

    page = requests.get(BASE_URL).content
    soup = BeautifulSoup(page, "html.parser")

    information = soup.select_one("div.additional-details")

    article = information.select_one("span.label").text
    article_number = information.select_one("#sku-148136").text

    delivery = information.select_one("div:nth-child(2) > a").text
    delivery_number = soup.select_one("div.additional-details > div:nth-child(2) > span").text

    forecast = information.select_one("div:nth-child(3) > a").text
    forecast_number = soup.select_one("div.additional-details > div:nth-child(3) > span").text

    city = information.select_one("div:nth-child(5) > a").text
    city_status = information.select_one("div:nth-child(5) > span").text

    return f"{article} {article_number}" \
           f"\n{delivery}{delivery_number}" \
           f"\n{forecast}{forecast_number}" \
           f"\n{city}{city_status}"


with open("text.txt", "w") as file:
    file.write(parse_page())
