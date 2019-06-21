import itchat
import weather_tools


def send_weather(url, NickName=None, RemarkName=None):
    # 获取天气信息
    day, weather, temp, windy, windy_power = weather_tools.get_weather(url)
    # 拼接消息
    msg = '今日天气：\n时间：{}\n天气：{}\n气温：{}\n风向：{}\n风力：{}'
    msg = msg.format(day, weather, temp, windy, windy_power)

    if '雨' in msg:
        msg = msg + '\n今天有雨，记得带伞哦'

    # 登录微信
    itchat.auto_login(True)

    if NickName or RemarkName:
        friends = itchat.get_friends(update=True)
        for friend in friends:
            if NickName:
                if friend['NickName'] == NickName:
                    username = friend['UserName']
            else:
                if friend['RemarkName'] == RemarkName:
                    username = friend['UserName']
    else:
        username = 'filehelper'

    # 发送消息
    itchat.send(msg, toUserName=username)

    # 退出登录
    itchat.logout()


if __name__ == "__main__":
    url = 'http://www.weather.com.cn/weather/101010200.shtml'

    send_weather(url)
