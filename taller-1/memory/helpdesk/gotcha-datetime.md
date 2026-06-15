# Gotcha: USE_TZ = False

`USE_TZ = False` is intentional. Do not change it to True without migrating
existing data. Affected areas:

- Ticket date-based URLs: `/ticket/<year>/<month>/<day>/<code>/`
  Stored dates are naive (no tz). Enabling USE_TZ shifts interpretation to UTC,
  breaking URL resolution for existing tickets.

- Vacation date filters (`approved`, `pending` queries)
  Date comparisons become inconsistent between naive DB values and tz-aware queries.

**Rule**: if deployment ever requires USE_TZ = True, run a data migration to
convert all DateTimeField values before changing the setting.