# AGENTS.md — Helpdesk (Django 3.1)

## Environment

`python-dotenv` is loaded at the top of `core/settings.py`. Create a `.env` file in the project root for any overrides. `*.env` is gitignored.

## Database

SQLite (`db.sqlite3`), gitignored. After cloning, run `makemigrations` then `migrate`.
See `memory/helpdesk/gotcha-datetime.md` before touching date-related models.

## Structure

| Directory | Purpose |
|-----------|---------|
| `core/` | Django project config: settings, root URL conf, ASGI/WSGI |
| `account/` | Custom user model (`MyUser`), `Account` profile, `Rol` (Regular/Agent) |
| `helpdesk/` | Tickets, Comments, Attachments, Vacation, Logs |

**URLs**: `/` → helpdesk, `/account/` → account, `/admin/` → admin.
**Auth**: `LOGIN_URL = 'account:login'`, `LOGIN_REDIRECT_URL = 'helpdesk:dashboard'`.

## Key dependencies

- Django 3.1.6, `django-widget-tweaks`, `Pillow`, `python-dotenv`

## Media

Uploaded files go to `media/account_images/` and `media/attachments/`. Served via Django during dev. The `media/` dir is not gitignored (keep or empty as needed).

## Conventions

- `AUTH_USER_MODEL = account.MyUser` (extends `AbstractUser`).
- `Rol` model uses `OneToOneField` to `MyUser` — each user gets exactly one role (is_regular or is_agent)
- Locale: `es-us`. Code mixes Spanish and English in comments and verbose names.
- Ticket statuses: `Pending`, `Ongoing`, `Closed`
- Vacation statuses: `pending`, `approved`, `declined`
- Ticket URLs use date-based paths: `/ticket/<year>/<month>/<day>/<code>/`

<!--
## Gotchas

See `memory/helpdesk/datetime-gotcha.md` before modifying date-related models or settings.
-->