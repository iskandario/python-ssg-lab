# TeleBid Research — Sphinx SSG

Исследовательский сайт по НИР-2 и лабораторной работе по Python SSG.

## Что опубликовано

- результаты НИР-2 TeleBid с графиками и формальными метриками;
- T1: сравнительная матрица MkDocs Material / Sphinx+MyST / Pelican / Quarto;
- методика эксперимента, архитектура и воспроизводимость;
- CI/CD на GitHub Actions и публикация GitHub Pages;
- формулы в критичных страницах — нативный MathML без внешнего CDN.

## Стек

- Python 3.12
- Sphinx 8.2.3
- MyST Parser 4.0.1
- Furo 2024.8.6
- GitHub Actions
- GitHub Pages

## Локальная сборка

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
sphinx-build -W --keep-going -b html docs site
python3 -m http.server 8000 -d site
```

Сайт: https://iskandario.github.io/python-ssg-lab/
