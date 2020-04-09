### Тестовое задание на должность QA Инженер (Python)
В качестве тестового задания предлагаем тебе покрыть тестами наш сервис подписок, его исходный код доступен по ссылке: [https://gitlab.monq.ru/p.alekseev/flask-app-example](https://gitlab.monq.ru/p.alekseev/flask-app-example). Инструкция по локальному запуску сервиса доступна в репозитории. Авто-тесты должны покрывать как API так и UI.
Будет оцениваться как набор тест-кейсов, так и качество кода, выбор и использование инструментов.
В результате выполнения тестового задания отправьте нам ссылку на репозиторий(ии) с тестами.


### Требования к ПО
- Платформа: Mac OS, Linux
- Docker - [https://www.docker.com](https://www.docker.com)
- Python 3.8 - [www.python.org/getit/](https://www.python.org/getit/)
- Инструмент для работы с виртуальными окружениями virtualenv
```bash
pip install virtualenv
```

### Копирование репозитория и установка зависимостей
```bash
git clone https://github.com/arkuz/subscribe_tests
cd subscribe_tests
virtualenv env
env/bin/activate
pip3 install -r requirements.txt
```

### Устновка Selenoid

```bash
curl -s https://aerokube.com/cm/bash | bash \
&& ./cm selenoid start --vnc && ./cm selenoid-ui start
```
Панель управления будет доступна по ссылке http://localhost:8080/

При запуске тестов в контейнере Selenoid НЕ будет доступно тестовое приложение по адресу http://localhost:4000. Необходимо узнать IP адрес вашей физической машины и прописать его в `config.yaml` в `site_url` и `api_url` в тестах. Так же необходимо изменить IP адрес тестового сервиса как указано в README файле [https://gitlab.monq.ru/p.alekseev/flask-app-example](https://gitlab.monq.ru/p.alekseev/flask-app-example), а конкретно изменить файл `docker-compose.yml`. Добавить строку `BACKEND_HOST`.
```yaml
  app:
    environment:
      BACKEND_HOST: http://192.168.0.12:4000
```


Чтобы узнать свой IP можно воспользоваться командой `ifconfig` в терминале.

Искать строку похожую на:
```bash
inet 192.168.0.12 netmask 0xffffff00 broadcast 192.168.0.255
```
Ваш IP - 192.168.0.12


### Запуск тестов
 - Перед запуском тестов необходимо перейти в каталог проекта `subscribe_tests`
 - В файле `config.yaml`в `browser` можно вписать значения `Chrome` или `Firefox`


Аргументы запуска:
- -s - показывать принты в процессе выпонения
- -v - verbose режим, чтобы видеть, какие тесты были запущены

##### Запуск всех тестов
```bash
py.test -s -v tests
```

##### Запуск всех тестов в пакете
```bash
py.test -s -v tests/web
```

##### Запуск помеченных тестов (positive, negative и т.п.)
```bash
py.test -s -v -m positive tests/web
```

##### Запуск тестового модуля
```bash
py.test -s -v tests/web/test_subscribe.py
```

##### Запуск тестового класса
```bash
py.test -s -v tests/web/test_subscribe.py::TestsMain
```

##### Запуск конкретного теста
```bash
py.test -s -v tests/web/test_subscribe.py::TestsMain::test_check_subscribe_time
```

#### Результат выполнения
 - Видео запуска на локалном браузере - [run_tests_.mp4](https://github.com/arkuz/subscribe_tests/blob/master/run_tests_.mp4)
 - Видео запуска в Selenoid - [selenoid_run.mp4](https://github.com/arkuz/subscribe_tests/blob/master/selenoid_run.mp4)
