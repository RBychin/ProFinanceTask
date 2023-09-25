# Тестовое задание от ПРО Финанс

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/RBychin/ProFinanceTestTask/tests)


### - Описание проекта:
- Тестовая задача от ПроФинанс
- Проект имеет три ендпоинта:
- 1. добавление задачи
- 2. просмотр результата выполнения задачи
- 3. получения статуса списка задач
- Перед пушем на Git проект проходит тесты:
- - Flake8
- - Pytest

Спецификация API находится по адресу: http://rbychin.ddns.net/docs


### - Стек разработки бекенда:
- Работа сайта организована на API запросах от фронтенда к бекенду.

  - Python 3.10
  - FastApi 0.103.1
  - Uvicorn
  - pytest
  - PyCharm 2023 1.2 (CE)
  - Docker
  - Docker-compose
  - Nginx
  - Git
  - Git Actions
  - Git Workflows
  - Ubuntu 22.04 etc Ubuntu-server 22.04


### - Первичный запуск:

- Скачайте папки `infra` из корневой директории проекта.
- Разместите эту папку на своем сервере.

- перейдите в директорию `infra`: `cd infra`.
- запустите docker-compose файл `docker compose up -d`

- Ваш сервер запущен и готов к работе по адресу вашего сервера на порту 80.


Для создания суперпользователя выполните команду:
- `docker-compose exec backend python manage.py createsuperuser`

Для доступа в админ панель используйте url такого вида `http://your_host/admin/`.
