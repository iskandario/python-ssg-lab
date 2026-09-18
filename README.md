# TeleBid Research — Sphinx SSG

Статический исследовательский сайт по НИР-2 «Исследование архитектурных решений обработки конкурентных торгов и синхронизации состояния в веб-платформах прямых и обратных аукционов».

## Стек сайта

- Python 3.12
- Sphinx
- MyST Parser (Markdown)
- Furo theme
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

GitHub Pages: https://iskandario.github.io/python-ssg-lab/
