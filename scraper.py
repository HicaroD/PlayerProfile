from bs4 import BeautifulSoup
import requests

class LiquipediaScraper:
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname
        self.soup = self.get_soup()

    def get_soup(self) -> BeautifulSoup:
        page = self.fetch_liquipedia_profile_page()
        return BeautifulSoup(page, 'lxml')

    def fetch_liquipedia_profile_page(self) -> str:
        page = requests.get(f"https://liquipedia.net/counterstrike/{self.nickname}")
        return page.text

    def get_player_description(self) -> str:
        player_description = self.soup.find("meta", {"name":"description"})
        return player_description['content'] if player_description else "Unknown player"

def main():
    nickname = input()
    scraper = LiquipediaScraper(nickname)
    print(scraper.get_player_description())

if __name__ == "__main__":
    main()
