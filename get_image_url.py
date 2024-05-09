import requests

def avatar_img_url(id):
    print(id, "aa")
    url = f"https://thumbnails.roblox.com/v1/users/avatar?userIds={id}&size=720x720&format=Png&isCircular=false"
    response = requests.get(url=url)
    return response.json()["data"][0]["imageUrl"]
    