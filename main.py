import requests
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
        author = post.find(class_="post-author").text[5:]
        title  = post.find('h2').text

        all_posts.append({ 'author': author, 'title': title})

print(all_posts)