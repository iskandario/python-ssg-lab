# Архитектура TeleBid

<div class="architecture-diagram">
  <div class="node client">Browser / React</div>
  <div class="node client">Telegram Mini App</div>
  <div class="arrow">HTTPS · SSE · WebSocket ↓</div>
  <div class="node api">NestJS API<br><small>commands · sync · gateway · notifications</small></div>
  <div class="split-row">
    <div class="node db">PostgreSQL<br><small>auctions · events · processed_commands</small></div>
    <div class="node bot">Telegram Bot<br><small>retry · fallback · deep links</small></div>
  </div>
  <div class="arrow">исследовательский контур ↓</div>
  <div class="split-row">
    <div class="node lab">Load generator</div>
    <div class="node lab">Toxiproxy</div>
    <div class="node lab">CSV / JSON dataset</div>
  </div>
</div>

## Транзакционная обработка

Ставка обрабатывается внутри PostgreSQL-транзакции. Строка аукциона блокируется на запись, проверяется `(auctionId, commandId)`, затем атомарно обновляются цена, лидер и `aggregateVersion`, а вместе с ними фиксируются событие и уведомления.

## Журнал событий

Каждое подтверждённое изменение получает `eventId` и монотонную `aggregateVersion`. Эта модель используется одинаково для Polling, SSE и WebSocket, благодаря чему транспорт не влияет на авторитетную семантику состояния.

## Recovery

- **snapshot** — полное актуальное состояние;
- **replay** — непрерывный диапазон событий после cursor;
- **hybrid** — выбирает меньший корректный payload.
