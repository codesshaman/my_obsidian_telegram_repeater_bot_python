### Архитектура бота:

```
app................| Корневая папка приложения
-controllers.......| Компонент, обрабатывающий команды пользователя
--routes...........| Определение всех роутов приложения
---handlers........| Обработчики команд для бота
----creation.py....| Обработчики команд на создание заметок
----handlers.py....| Обработчики основных команд
----scanning.py....| Обработчики команд сканирования директории
-model.............| Компонент, управляющий обработкой данных
--core.............| Ядро приложения, запускающее бота
---bot.py..........| Единственный запущенный экземпляр бота
--file_module......| Модуль для работы с файловой системой
---create.py.......| Класс создания файлов заметок
---index.py........| Класс индексации имеющихся заметок
---scann.py........| Класс сканирования директории заметок
--send_module......| Модуль отправки данных
---send.py.........| Класс отправки данных пользователю
--config_parser.py.| Парсер конфигурации
```

### Архитектура контейнеров:

```
docker-compose......................| Конфигурацтя docker-compose.yml
-app:...............................| Приложение, содержащее код бота
--volumes:..........................| Примонтированные боту разделы
---./app:/app.......................| Непосредственно код приложения
---./zettelkasten:/var/zettelkasten.| Папка-символьная ссылка на заметки
-syncthing:.........................| Приложение syncthing для синхронизации
--volumes:..........................| Разделы для работы syncthing
---./syncthing:/var/syncthing.......| Здесь храняться заметки в /zettelkasten
```