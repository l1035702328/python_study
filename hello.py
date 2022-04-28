# coding = utf =8

import requests





if __name__ == '__main__':
    html = requests.get("https://www.youtube.com/watch?v=JGwWNGJdvx8")
    # print(html.text)
    print(html.content)