# random_film2022
Цей код на Python виконує парсинг веб-сайту з фільмами. Давайте розберемо його почергово:

1.Імпорт необхідних модулів:
requests: для здійснення HTTP-запитів до веб-сайту.
BeautifulSoup з модуля bs4: для парсингу HTML-коду веб-сторінки.

2.Ініціалізація змінних:
page = 1: вказує на початкову сторінку для парсингу.
ls = {}: це словник, в якому будуть зберігатися назви фільмів та посилання на них.

3.Основний цикл парсингу:
В циклі while True виконуються наступні кроки до тих пір, поки не буде виконано умову break.
Виконується HTTP-запит до веб-сторінки за допомогою requests.get(). URL сторінки формується з базової адреси та номера сторінки.
HTML-код сторінки зберігається в змінній html.
Вибираються елементи сторінки, що містять інформацію про фільми, за допомогою CSS-селектора ul.results > .results-item-wrap.
Якщо кількість знайдених елементів не дорівнює нулю і номер сторінки менший або дорівнює 3, виконуються наступні дії:
Виводиться розділювач, що показує номер поточної сторінки.
Для кожного елементу виводяться назва фільму та посилання на нього.
Записується назва фільму та посилання на нього в словник ls.
Збільшується значення змінної page на одиницю.

4.Виведення результатів:
Після завершення циклу виводиться розділювач.
Змінна x отримує випадковий ключ (назву фільму) зі словника ls.
Виводиться назва фільму та посилання на нього, отримані зі словника ls за допомогою методу .get().
Виводиться розділювач.

Отже, цей код парсить веб-сторінку з фільмами за допомогою requests і BeautifulSoup. Він проходить крізь кілька сторінок, збирає назви фільмів та посилання на них і випадковим чином вибирає один фільм для виведення.