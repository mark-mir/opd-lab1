import requests
from bs4 import BeautifulSoup

URL = "https://omgtu.ru/general_information/the-structure/the-department-of-university.php"


def main():
    # Загружаем страницу
    response = requests.get(URL)
    if response.status_code != 200:
        print(f"Ошибка: {response.status_code}")
        return

    # Парсим HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Ищем список кафедр
    departments = []
    for li in soup.select("#pagecontent ul li"):
        a_tag = li.find("a")
        if a_tag and a_tag.text.strip():
            departments.append(a_tag.text.strip())

    # Записываем в файл
    with open("departments.txt", "w", encoding="utf-8") as file:
        for department in departments:
            file.write(department + "\n")

    print(f"Сохранено {len(departments)} кафедр в departments.txt")


if __name__ == "__main__":
    main()
