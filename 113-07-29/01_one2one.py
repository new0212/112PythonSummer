import requests

URL = 'https://notify-api.line.me/api/notify'
H, P = {}, {}
H['Authorization'] = 'Bearer 68xcbXACa6nF44QmJd4jCiauAre26HwXurBuA4DqYTV'
P['message'] = '今天天氣很好'
requests.post(URL, headers=H, params=P)