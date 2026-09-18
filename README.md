# Python SSG Lab

Лабораторная работа по генераторам статических сайтов на Python и CI/CD.

## Локальный запуск

```bash
python3 -m pip install virtualenv
python3 -m virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Строгая сборка:

```bash
mkdocs build --strict
```

## GitHub Pages

1. Создать публичный репозиторий `python-ssg-lab` в аккаунте `iskandario`.
2. Загрузить содержимое этого проекта в ветку `main`.
3. Открыть Settings → Pages → Source → GitHub Actions.
4. Workflow `.github/workflows/pages.yml` соберёт и опубликует сайт.

Ожидаемый URL: `https://iskandario.github.io/python-ssg-lab/`.

## Helios

Добавить Actions Secrets: `HELIOS_HOST`, `HELIOS_USER`, `HELIOS_SSH_KEY`, `HELIOS_PATH`, затем вручную запустить workflow `Deploy MkDocs to Helios`.
