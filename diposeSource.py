import requests                  # 웹 페이지의 HTML을 가져오는 모듈
from bs4 import BeautifulSoup    # HTML을 파싱하는 모듈


class Diposer():
    def __init__(self, URL):
        self.URL = URL
        self.response = requests.get(self.URL)
        self.soup = BeautifulSoup(self.response.content, "html.parser")
        self.soup.br.replace_with('\n')

        self.en_tag = "h3"
        self.en_class = "Heading-gyg8vb-0 dbvomz"
        self.ko_tag = "div"
        self.ko_class = "Text-sc-1sog5i-0 hxbsdE"

    def parsing(self, t):
        s = str(t)
        s = s.replace("<br>", '\n')
        s = s.replace("<br/>", '\n')
        s = s.replace("<b>", ' ')
        s = s.replace("</b>", "")

        while True:
            if s[0] == '>':
                break
            s = s[1:]

        while True:
            if s[-1] == '<':
                break
            s = s[:-1]

        return s[1:-1]

    def getText(self, tag, cla):
        text = self.soup.findAll(tag, {"class" : cla})
        ret = []

        for t in text:
            ret.append(self.parsing(t))

        return ret

    def asText(self, write_title):
        english = self.getText(self.en_tag, self.en_class)
        korean = self.getText(self.ko_tag, self.ko_class)

        with open(write_title, 'w') as f:
            for e, k in zip(english, korean):
                f.write(e + " " + k + '\n')