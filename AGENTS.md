# LibroLibre — AGENTS.md

## Stack (immutable)

| Layer | Technology | Notes |
|-------|-----------|-------|
| Backend | Python + Django | — |
| Frontend | HTML5 + CSS3 | No React/Vue/Angular |
| Database | PostgreSQL | **Never use SQLite** — not even in dev |
| Hosting | Render | Must be Render-compatible from day 1 |
| Maps | Leaflet + OpenStreetMap | — |
| Images | Pillow | Cover image required for every book |

## Database

- PostgreSQL must be created on Render **first**, before any models are written.
- Workflow: create Render PG → get `DATABASE_URL` → configure Django → create models → makemigrations → migrate → develop.
- Migrations must never target SQLite.

## Modules & entities

- **User** — registration via Django auth (username + institutional email, password validation)
- **Book** — title, author, description, type (loan/donation), cover image, availability status
- **Solicitud (Request)** — states: Pendiente → Aceptada/Rechazada/Cancelada → Completada
- **Mensaje (Message)** — private chat enabled only after a request is accepted
- **PuntoEncuentro (MeetingPoint)** — lat, lng, address, delivery date/time; one active per request; visible only to participants

Convention: define all model relationships before building views or forms.

## Environment variables

`SECRET_KEY`, `DEBUG`, `DATABASE_URL`, `ALLOWED_HOSTS`, `STATIC_URL`, `STATIC_ROOT`, `MEDIA_URL`, `MEDIA_ROOT`.

## Image handling

- Formats: JPG, JPEG, PNG, WEBP only.
- If image upload fails, abort the entire book creation (no partial records).
- Use Render-compatible paths — never absolute local paths.

## Pre-deployment checks

Before each deploy, verify: user registration, login, password reset, book publishing, image upload & display, requests, messaging, map, meeting point, PostgreSQL connection, migrations applied.

## Key constraints

- All private views require authentication.
- Users can only modify their own books.
- Chat & meeting point visible only to participants.
- Only one active meeting point per request.
