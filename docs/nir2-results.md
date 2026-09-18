# Результаты НИР-2

<div class="page-intro">
Пилотная серия проверяла пять гипотез: корректность конкурентных торгов, live-задержку транспортов, сходимость после reconnect, корректность hybrid recovery и надёжность двухканальной доставки уведомлений.
</div>

## Итог пилотной серии

<div class="result-kpi-grid">
  <div class="result-kpi success"><strong>18 / 18</strong><span>торгов завершились с корректной ценой и лидером</span></div>
  <div class="result-kpi success"><strong>64 / 64</strong><span>повторные команды распознаны без второго эффекта</span></div>
  <div class="result-kpi success"><strong>306 / 306</strong><span>клиентов сошлись с серверной версией после reconnect</span></div>
  <div class="result-kpi success"><strong>1125 / 1125</strong><span>Telegram-уведомлений доставлены после искусственного отказа первой попытки</span></div>
  <div class="result-kpi success"><strong>387 / 387</strong><span>ожидаемых уведомлений получил Mini App</span></div>
  <div class="result-kpi success"><strong>18 / 18</strong><span>hybrid-проверок выбрали минимальный JSON payload</span></div>
</div>

## H1 · Корректность конкурентных торгов

Во всех 18 trial фактическая цена и лидер совпали с ожидаемым лучшим предложением. Авторитетные версии журнала были непрерывны, а все 64 повторные команды вернули сохранённый результат с признаком идемпотентного replay. Повторных доменных эффектов не зафиксировано.

<div class="stat-row">
  <div><b>49,31 мс</b><span>среднее время обработки исходной команды</span></div>
  <div><b>40 мс</b><span>медиана</span></div>
  <div><b>114 мс</b><span>p95</span></div>
  <div><b>438 мс</b><span>максимум</span></div>
</div>

**Вывод:** транзакционная обработка, `SELECT FOR UPDATE` и составной ключ идемпотентности `(auctionId, commandId)` обеспечили корректность в исследованном диапазоне.

## H2 · Live latency: Polling vs SSE vs WebSocket

В стабильном профиле SSE и WebSocket показали заметно меньшую p95-задержку live-доставки, чем HTTP polling.

<div class="chart-card">
  <div class="chart-title">Медиана trial-p95 live-доставки</div>
  <div class="chart-group"><span class="chart-label">Прямой аукцион</span><div class="bar polling" style="--w: 88%"><b>Polling</b><em>266 мс</em></div><div class="bar sse" style="--w: 16%"><b>SSE</b><em>48 мс</em></div><div class="bar ws" style="--w: 14%"><b>WebSocket</b><em>42 мс</em></div></div>
  <div class="chart-group"><span class="chart-label">Обратный аукцион</span><div class="bar polling" style="--w: 89%"><b>Polling</b><em>267 мс</em></div><div class="bar sse" style="--w: 11%"><b>SSE</b><em>34 мс</em></div><div class="bar ws" style="--w: 12%"><b>WebSocket</b><em>35 мс</em></div></div>
</div>

По трём повторам нельзя объявлять SSE или WebSocket универсальным победителем: преимущество между ними мало и меняет направление между видами торгов.

## H3 · Восстановление после разрыва

После reconnect все 306 клиентов завершили серию на актуальной серверной версии. `staleClients = 0`, `missingEvents = 0`. Гипотеза поддержана во всех 12 trial с разрывом.

| Профиль | Polling | SSE | WebSocket |
|---|---:|---:|---:|
| mobile-reconnect, прямой | 446 мс | 2415 мс | 954 мс |
| mobile-reconnect, обратный | 360 мс | 2409 мс | 960 мс |
| final-burst-unstable, прямой | 1427 мс | 2121 мс | 1766 мс |
| final-burst-unstable, обратный | 1328 мс | 2116 мс | 1678 мс |

<div class="insight-card warning"><b>Неожиданный результат:</b> при принудительном fault polling в текущей конфигурации восстанавливался быстрее push-вариантов. Это не противоречит live-тесту: live latency и reconnect — разные свойства системы.</div>

## H4 · Hybrid recovery

Во всех 18 контрольных проверках snapshot, replay и hybrid пришли к одной финальной версии, а replay содержал непрерывный диапазон событий.

<div class="comparison-grid">
  <div><small>Snapshot</small><strong>657–676 байт</strong></div>
  <div><small>Replay</small><strong>2250–5675 байт</strong></div>
  <div class="accent"><small>Hybrid</small><strong>18 / 18 → snapshot</strong></div>
</div>

Hybrid корректно выбрал меньший сериализованный JSON payload. При этом однообразный выбор — ограничение пилота: состояние аукциона было небольшим, поэтому из результата нельзя делать вывод, что snapshot всегда лучше replay.

## H5 · Mini App и Telegram-уведомления

Система сохранила 1125 уведомлений. Исследовательский адаптер намеренно отклонял первую попытку каждого сообщения. После retry все 1125 записей получили статус `DELIVERED`.

- trial-p95 доставки ботом: **115–469 мс**;
- Mini App получил **387 из 387** ожидаемых уведомлений;
- **115** пришли через live WebSocket;
- **272** восстановлены через replay после cursor;
- потерь, повторного показа и нарушений причинного порядка не обнаружено.

## Что в итоге доказал пилот

Пилот поддержал H1–H5 **в тестируемом диапазоне**, но не является универсальным доказательством превосходства одного транспорта. Главный архитектурный вывод: корректность торгов обеспечивается серверной семантикой, идемпотентностью и версионированным журналом; транспорт определяет прежде всего характеристики live-доставки, а сходимость после разрыва — протокол recovery.
