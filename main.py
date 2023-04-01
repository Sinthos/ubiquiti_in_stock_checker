import requests
from bs4 import BeautifulSoup


def check_availability(url):
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, "html.parser")

    texts = ["In Stock", "Sold Out"]
    found_text = None

    for text in texts:
        result = soup.find(string=text)
        if result:
            found_text = text
            break

    if found_text:
        print(f"Der erste gefundene Text ist: {found_text}")
    else:
        print("Keiner der Texte 'In Stock' oder 'Sold Out' wurde gefunden.")


if __name__ == '__main__':
    url = input("Bitte geben Sie die URL der Website ein: ")
    check_availability(url)
