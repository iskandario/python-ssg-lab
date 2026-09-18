# TeleBid Research

<div class="hero-panel">
  <div class="eyebrow">НИР-2 · Веб-технологии · 2026</div>
  <h1>Конкурентные торги, real-time доставка и восстановление состояния</h1>
  <p class="hero-lead">Исследование архитектурных решений для веб-платформ прямых и обратных аукционов: атомарная обработка ставок, Polling / SSE / WebSocket, snapshot / replay / hybrid recovery и надёжная доставка уведомлений в Telegram Mini App.</p>
  <div class="hero-actions">
    <a class="button primary" href="nir2-results.html">Результаты НИР-2</a>
    <a class="button ghost" href="methodology.html">Методика эксперимента</a>
  </div>
</div>

<div class="metric-grid">
  <div class="metric"><span>18</span><small>экспериментальных прогонов</small></div>
  <div class="metric"><span>306</span><small>виртуальных клиентов</small></div>
  <div class="metric"><span>1072</span><small>попытки торговых команд</small></div>
  <div class="metric"><span>7041</span><small>наблюдение доставки событий</small></div>
</div>

## Что исследуется

TeleBid используется не как экономическая модель, а как нагрузочный и событийный стенд. Аукцион удобен тем, что у него есть строгие инварианты: одна актуальная цена, один лидер, монотонная версия состояния и чёткий момент закрытия.

Исследование разделяет четыре слоя:

<div class="layer-grid">
  <div class="layer-card"><b>Command layer</b><span>атомарно принимает и проверяет ставки</span></div>
  <div class="layer-card"><b>Event layer</b><span>фиксирует подтверждённые изменения с версией</span></div>
  <div class="layer-card"><b>Sync layer</b><span>доставляет события и восстанавливает состояние</span></div>
  <div class="layer-card"><b>Notification layer</b><span>обеспечивает durable inbox и Telegram fallback</span></div>
</div>

## Главная идея

**Транспорт не равен синхронизации.** WebSocket может дать низкую задержку live-доставки, но после разрыва соединения корректность определяется не самим постоянным каналом, а журналом событий, версией состояния и протоколом recovery.

```{toctree}
:hidden:
:maxdepth: 2

nir2-results
methodology
architecture
reproducibility
deployment
licenses
```

<div class="control-string">SSG-LAB-CONTROL-2026</div>
