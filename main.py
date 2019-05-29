import requests
import json
from bs4 import BeautifulSoup

res = requests.get("https://digitalinnovation.one/blog/")
res.encoding = "utf-8"
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.find(class_='pagination').find_all('a')


all_pages = []
all_posts = []

for link in links:
    lnk = requests.get(link.get('href'))
    all_pages.append(BeautifulSoup(lnk.text, 'html.parser'))

for page in all_pages:
    posts = soup.find_all(class_='post')
    for post in posts:
        info = post.find(class_='post-content')
        title = info.h2.a.text
        preview = info.p.text
        date = info.footer.time['datetime']
        img = post.find(class_='wp-post-image')['src']
        author = post.find(class_='post-author').text

        all_posts.append({
                'title': title,
                'preview': preview,
                'date': date,
                'author': author[5:],
                'img': img
        })


print(all_posts)
with open('posts.json', 'w') as json_file:
    json.dump(all_posts, json_file, indent=3, ensure_ascii=False)