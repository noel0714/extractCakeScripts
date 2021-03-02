import diposeSource


def main():
    site_name = "https://mycake.me/sentences/70d9da470da0?utm_source=share&lang=ko&pid=Player&c=21528&lang=ko"
    disposer = diposeSource.Diposer(site_name)
    disposer.asText("result.txt")


if __name__ == "__main__":
    main()