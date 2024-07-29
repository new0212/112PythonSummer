import requests

URL = 'https://notify-api.line.me/api/notify'
H, P = {}, {}
H['Authorization'] = 'Bearer 68xcbXACa6nF44QmJd4jCiauAre26HwXurBuA4DqYTV'
P['message'] = '貼圖測試'
P['stickerPackageId'] = 6362
P['stickerId'] = 11087922
requests.post(URL, headers=H, params=P)