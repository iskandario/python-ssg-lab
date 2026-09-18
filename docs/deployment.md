# CI/CD и публикация

Этот сайт собирается **Sphinx**, а Markdown разбирается расширением **MyST Parser**. За визуальный слой отвечает тема **Furo** и собственный CSS.

## Почему не MkDocs

Sphinx даёт более мощную структуру документации, расширяемость, встроенный поисковый индекс, кросс-ссылки и развитую экосистему для технических и исследовательских публикаций. MyST позволяет при этом продолжать писать материалы в Markdown.

## Локальный запуск

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
sphinx-autobuild docs site
```

Для строгой сборки, аналогичной CI:

```bash
sphinx-build -W --keep-going -b html docs site
```

## GitHub Pages

Workflow `.github/workflows/pages.yml` устанавливает Python-зависимости, выполняет строгую Sphinx-сборку, проверяет контрольную строку и публикует каталог `site/` через официальный Pages artifact.
