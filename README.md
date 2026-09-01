# Land & Water Protection Efforts — Interactive Map

An interactive map of current local land and water protective efforts connected to
our geographies. Each point marks an effort and opens a card describing who is on
the ground, what they are up against, and the support they've asked for.

Built with [Folium](https://python-visualization.github.io/folium/) (Leaflet.js) and
rendered to a single self-contained HTML file — no server, no build step, no account
needed to view it.

## Contents

| Path | What it is |
|------|------------|
| `scripts/build_map.py` | The map generator. Effort data lives at the top of this file. |
| `docs/index.html` | Generated map. Open in any browser. Rebuilt by the script. |
| `.gitignore` | Blocks raw survey exports and other sensitive files from ever being committed. |

## Running it

Requires Python 3.9 or newer.

```bash
pip install folium
```

```bash
python3 scripts/build_map.py
```

The script writes `docs/index.html`. Open that file in a browser to view the map.

## Editing the data

Each effort is a dictionary in the `efforts` list near the top of
`scripts/build_map.py`:

```python
{
    "name": "Bayou City Waterkeepers",
    "location": "Houston",
    "lat": 29.7604, "lon": -95.3698,
    "on_ground": "Bayou City Waterkeepers; National Wildlife Federation; Clean Water Action",
    "fighting": "WOTUS rollback / Trump Administration (Clean Water Act protections)",
    "support": "Legal, public awareness, meeting space",
}
```

Add or edit an entry, re-run the script, and the map regenerates. `lat`/`lon` are
decimal degrees — negative longitude for the Western Hemisphere.

## A note on the basemap

The background map tiles come from Esri's World Light Gray Canvas, which is served
without an API key. An earlier version used CARTO's Positron basemap; CARTO has since
moved that basemap behind an API key and now stamps `API KEY REQUIRED` across tiles
requested without one. If you ever see that watermark reappear, the tile provider —
not this repository — is what changed.

## Data & privacy

The effort information here was gathered from survey responses. A few ground rules
keep respondents protected:

- **No individual people are named in this repository.** Efforts are credited to the
  organization, tribe, nation, or collective doing the work — not to named private
  individuals. Publishing a person's name next to the government agency or company
  they are organizing against creates real risk for that person.
- **Raw survey exports are never committed.** `.gitignore` blocks `private/`,
  `data/raw/`, and common survey export filenames. Keep original responses, contact
  details, and anything with emails or phone numbers outside this repository.
- **Only publicly-facing information belongs here** — the effort, its general
  location, the organization on the ground, and the support requested.
- **Locations are approximate.** Coordinates point at a city or landmark, not at
  anyone's home, meeting site, or camp.

If you are adding data, check it against this list before committing. Once something
is pushed it lives in git history even if a later commit removes it.

## Acknowledgements

Thanks to every organizer, tribe, nation, and collective represented here, and to
everyone who took the time to respond to the survey.
