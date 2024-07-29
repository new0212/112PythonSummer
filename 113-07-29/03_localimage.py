import requests

URL = 'https://notify-api.line.me/api/notify'
H, P, F = {}, {},{}
H['Authorization'] = 'Bearer 68xcbXACa6nF44QmJd4jCiauAre26HwXurBuA4DqYTV'
P['message'] = '本機圖片'
F['imageFile'] = open('shin.jpg', 'rb')
requests.post(URL, headers=H, params=P, files=F)