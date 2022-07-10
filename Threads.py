import requests
from threading import Thread


def download(url):
    a = url.split("/")
    file = a[len(a)-1]
    p = requests.get(url)
    with open(file, "wb") as recieve:
        recieve.write(p.content)
    print(file + ' is downloaded')


def downloads(urls):
    threads = []
    for j in range(len(urls)):
        print(urls[j])
        threads.append(Thread(target=download, kwargs=dict(url=urls[j])))
    for i in threads:
        i.start()
    for i in threads:
        i.join()
    print("Ok")


if __name__ == '__main__':

    p1 = "https://click-or-die.ru/app/uploads/2020/09/original-1.jpg"
    p2 = "https://assets.turbologo.ru/blog/ru/2019/03/18170122/agriculture-bright-clouds-440731.jpg"
    p3 = "https://upload.wikimedia.org/wikipedia/ru/2/2f/Beck-_Mongolian_Chop_Squad.jpg"
    files = [p1, p2, p3]

    downloads(files)