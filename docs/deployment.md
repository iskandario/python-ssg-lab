# CI/CD и развёртывание

## Локальная подготовка

```bash
python3 --version
python3 -m pip --version
python3 -m pip install virtualenv
python3 -m virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
mkdocs build --strict
```

`--strict` превращает предупреждения MkDocs в ошибку и поэтому используется также в CI.

## GitHub Pages

Основной workflow находится в `.github/workflows/pages.yml`. Он:

1. получает исходный код;
2. устанавливает Python и зависимости;
3. выполняет `mkdocs build --strict`;
4. проверяет наличие контрольной строки;
5. загружает каталог `site/` как Pages artifact;
6. развёртывает artifact официальным `actions/deploy-pages`.

В настройках репозитория необходимо выбрать **Settings → Pages → Source → GitHub Actions**.

## Два подхода к GitHub Pages

`peaceiris/actions-gh-pages` публикует готовую сборку отдельным commit/push в ветку `gh-pages`. В результате сгенерированные файлы физически находятся в специальной ветке.

Официальная схема `actions/upload-pages-artifact` + `actions/deploy-pages` не требует отдельной ветки с результатами сборки: CI передаёт artifact непосредственно сервису Pages. В этой работе используется второй подход.

## Helios / собственный отечественный сервер

Файл `.github/workflows/helios.yml` собирает сайт тем же способом, после чего копирует каталог `site/` на сервер по SSH с помощью `rsync`. Секреты репозитория:

- `HELIOS_HOST` — адрес сервера;
- `HELIOS_USER` — имя пользователя;
- `HELIOS_SSH_KEY` — приватный SSH-ключ;
- `HELIOS_PATH` — каталог публикации.

Workflow запускается вручную (`workflow_dispatch`), чтобы публикация на учебный сервер не происходила без необходимости.

## Базовый URL

Для GitHub Pages проект размещается в подкаталоге `/python-ssg-lab/`, поэтому в `mkdocs.yml` задан `site_url` с полным путём. Внутренние ссылки в Markdown используются относительные, а `use_directory_urls: true` позволяет получать человекочитаемые URL.

Для Helios при публикации в другом подкаталоге рекомендуется менять `site_url` на фактический адрес либо собирать отдельную конфигурацию. Критично не использовать жёстко заданные пути вида `/assets/...`.
