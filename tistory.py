class Tistory:
    def __init__(self):
        self.table_strat = "<tbody>"
        self.table_end = "<tr><td style=\"width: 50%;\"><br></td><td style=\"width: 50%;\"><br></td></tr></tbody>"

        self.tr_style = "<tr style=\"height: 20px;\" data-mce-style=\"height: 20px;\">"
        self.td_style_en = "<td style=\"width: 50%; height: 20px;\" data-mce-selected=\"1\" data-mce-first-selected=\"1\">"
        self.td_style_ko = "<td style=\"width: 50%; height: 20px;\">"

        self.space = "&nbsp;"

    def changeSpace(self, s):
        s = s.replace(" ", self.space)

        return s

    def makeEng(self, s):
        return self.td_style_en + self.changeSpace(s) + "</td>"

    def makeKor(self, s):
        return self.td_style_ko + self.changeSpace(s) + "</td>"

    def makeTableScript(self, en, ko):
        script = self.table_strat

        for e, k in zip(en, ko):
            script = script + self.tr_style + self.makeEng(e) + self.makeKor(k) + "</tr>"

        script = script + self.table_end

        return script