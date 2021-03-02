import diposeSource
import tistory


def main():
    site_name = "https://mycake.me/sentences/70d9da470da0?utm_source=share&lang=ko&pid=Player&c=21528&lang=ko"
    disposer = diposeSource.Diposer(site_name)
    english, korean = disposer.getText()

    tis = tistory.Tistory()
    script = tis.makeTableScript(english, korean)

    with open("result.txt", 'w') as f:
        f.write(script)
    

if __name__ == "__main__":
    main()