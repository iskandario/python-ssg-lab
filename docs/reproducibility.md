# Воспроизводимость

Исследовательский стенд запускается отдельно от продуктового контура и формирует машиночитаемый датасет.

## Артефакты запуска

- `events.csv` — доставка события виртуальному клиенту;
- `commands.csv` — исходные и повторные HTTP-команды;
- `notifications.csv` — получение и безопасный показ уведомления Mini App;
- `clients.csv` — итоговые клиентские метрики;
- `trials.csv` — метрики транспорта в trial;
- `aggregates.csv` — описательная статистика;
- `summary.json` — вердикты гипотез;
- `manifest.json` — версия кода, seed и параметры среды.

## Воспроизведение

```bash
npm install
npm run research
```

Короткий smoke-run:

```bash
npm run research:up
npm run research:wait
npm run research:quick
```

Исходный экспериментальный проект: `iskandario/telebid-auction-lab`.
