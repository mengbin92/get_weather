from bs4 import BeautifulSoup
from urllib.request import urlopen


def get_weather(url):

    #url = 'http://www.weather.com.cn/weather/101210402.shtml'

    html = urlopen(url).read().decode('utf-8')
    # print(html)

    soup = BeautifulSoup(html, features='lxml')

    today = soup.find('li', attrs={'class': 'sky skyid lv1 on'})
    # print(today)

    day = today.find('h1').get_text()
    # print(day.get_text())

    weather = today.find('p', {'class': 'wea'}).get_text()
    # print(weather.get_text())

    temp = today.find('p', {'class': 'tem'}).get_text()[1:-1]
    # print(temp.get_text())

    windy = today.find('p', {'class': 'win'}).find('em').find_all('span')
    windy = windy[0]['title']+'转'+windy[1]['title']
    # print(windy)

    windy_power = today.find('p', {'class': 'win'}).find_all('i')[0].get_text()
    # print('风力：',windy_power.get_text())
    return day, weather, temp, windy, windy_power
