<h1>Text2Image Telegram Bot</h1>
    
<h2>Описание проекта</h2>

<p>Этот проект представляет собой Telegram-бота для генерации изображений на основе текстовых запросов с использованием API FusionBrain AI.</p>
    
<h2>Структура проекта</h2>
    
<h3>Файл: <code>ClassImgGenerate.py</code></h3>
    
<h4>Описание</h4>

<p>Этот модуль содержит класс <code>Text2ImageAPI</code>, предоставляющий интерфейс для взаимодействия с API генерации изображений FusionBrain AI.</p>
    
<h4>Класс: <code>Text2ImageAPI</code></h4>
    
<h5>Атрибуты</h5>
<ul>
    <li><code>URL</code> (str): Базовый URL API.</li>
    <li><code>AUTH_HEADERS</code> (dict): Словарь с заголовками аутентификации.</li>
</ul>
    
<h5>Методы</h5>
<ul>
    <li>
        <code>__init__(self, url, api_key, secret_key)</code>: Конструктор класса. Инициализирует новый экземпляр <code>Text2ImageAPI</code>.
    </li>
    <li>
        <code>get_model(self)</code>: Возвращает ID доступной модели генерации изображений.
    </li>
    <li>
        <code>generate(self, prompt, model, style, images=1, width=1024, height=1024)</code>: Генерирует изображение по заданному запросу и параметрам.
    </li>
    <li>
        <code>check_generation(self, request_id, attempts=10, delay=10)</code>: Проверяет статус запроса на генерацию изображения.
    </li>
</ul>
    
<h3>Файл: <code>Global_Variables.py</code></h3>
    
<h4>Описание</h4>

<p>Модуль содержит глобальные переменные, используемые в приложении.</p>

<pre><code>URL = ""<br>BOT_TOKEN = ""<br>API_KEY = ""<br>SECRET_KEY = ""</code></pre>
    
<h3>Файл: <code>main.py</code></h3>
    
<h4>Описание</h4>

<p>Основной модуль приложения, отвечающий за взаимодействие с Telegram ботом и генерацию изображений.</p>
    
<h5>Функции</h5>
<ul>
    <li>
        <code>generate_image_bot(prompt, style="No style")</code>: Генерирует изображение по заданному запросу и стилю.
    </li>
    <li>
        <code>get_message(message)</code>: Обработчик команды <code>/gen</code>. Генерирует изображение по запросу пользователя в Telegram.
    </li>
    <li>
        <code>get_style(message)</code>: Обработчик команды <code>/sty</code>. Выводит список доступных стилей для генерации изображений.
    </li>
</ul>
    
<h3>Запуск приложения</h3>

<p>Для запуска приложения необходимо выполнить файл <code>main.py</code>.</p>
    
<h3>Примечания</h3>

<p>Для работы приложения необходимо установить библиотеки <code>telebot</code>, <code>requests</code> и <code>datetime</code>. Перед запуском приложения необходимо указать в файле <code>Global_Variables.py</code> актуальные значения переменных <code>URL</code>, <code>BOT_TOKEN</code>, <code>API_KEY</code> и <code>SECRET_KEY</code>.</p>
    
<h2>Авторы проекта</h2>
<ul>
    <li>Эльадр</li>
    <li>Данил</li>
    <li>Мусса</li>
</ul>
