import itchat
import weather_tools

# itchat.auto_login(True)

#itchat.send('hello filehelper', toUserName='filehelper')

# friends = itchat.get_friends(update=True)
# for friend in friends:
#     if friend['NickName'] == 'Gypsy':
#         itchat.send('What are you 弄啥嘞！', toUserName=friend['UserName'])
#         print('send msg done')
# itchat.logout()


def send_weather(url):
    # 获取天气信息
    day, weather, temp, windy, windy_power = weather_tools.get_weather(url)
    # 拼接消息
    msg = '今日天气：\n时间：{}\n天气：{}\n气温：{}\n风向：{}\n风力：{}'
    msg = msg.format(day, weather, temp, windy, windy_power)

    # 登录微信
    itchat.auto_login(True)

    # 发送消息
    itchat.send(msg, toUserName='filehelper')

    # 退出登录
    itchat.logout()


if __name__ == "__main__":
    url = 'http://www.weather.com.cn/weather/101210402.shtml'

    send_weather(url)
