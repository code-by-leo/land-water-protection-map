from pathlib import Path

import folium

efforts = [
    {
        "name": "Save East River Park",
        "location": "New York",
        "lat": 40.7196, "lon": -73.9748,
        "on_ground": "East River Park Action; community members with support from some electeds",
        "fighting": "Lower Manhattan Coastal Resiliency Plan (City of New York); developers & the city",
        "support": "Public awareness, community building, and funds to preserve park land and natural habitat",
    },
    {
        "name": "No mega jail in Chinatown",
        "location": "New York",
        "lat": 40.7163, "lon": -73.9999,
        "on_ground": "Youth Against Displacement",
        "fighting": "City of New York; big real estate",
        "support": "Showing up to protests to make the issue public and known",
    },
    {
        "name": "Carrizo Comecrudo Tribe vs SpaceX",
        "location": "Texas",
        "lat": 25.9975, "lon": -97.1558,
        "on_ground": "Carrizo Comecrudo Tribe of Texas; South Texas Environmental Justice Network",
        "fighting": "SpaceX / Elon Musk; TCEQ; City Council of Brownsville",
        "support": "Legal, public awareness, meeting space",
    },
    {
        "name": "Bayou City Waterkeepers",
        "location": "Houston",
        "lat": 29.7604, "lon": -95.3698,
        "on_ground": "Bayou City Waterkeepers; National Wildlife Federation; Clean Water Action",
        "fighting": "WOTUS rollback / Trump Administration (Clean Water Act protections)",
        "support": "Legal, public awareness, meeting space",
    },
    {
        "name": "Land Memory Bank & Seed Exchange",
        "location": "Louisiana",
        "lat": 30.4515, "lon": -91.1871,
        "on_ground": "Land Memory Bank & Seed Exchange",
        "fighting": "Habitat loss and threats to Coastal Indigenous & local cultures (United Houma Nation, Louisiana French, African American communities); loss of community knowledge & food sovereignty",
        "support": "Regranting support and storytelling/amplification (e.g., NPN National Conference, e-news), with compensation",
    },
    {
        "name": "Bvlbancha Collective",
        "location": "Louisiana",
        "lat": 29.9511, "lon": -90.0715,
        "on_ground": "Bvlbancha Collective",
        "fighting": "Erasure of Gulf South Indigenous peoples — fighting for cultural revitalization, community resilience, and sovereignty for United Houma Nation, Tunica-Biloxi Tribe, and others",
        "support": "Regranting support and storytelling/amplification, with compensation",
    },
    {
        "name": "Bristol Bay / Pebble Mine Opposition",
        "location": "Alaska",
        "lat": 58.7184, "lon": -156.6612,
        "on_ground": "Bristol Bay residents and Alaska Native groups",
        "fighting": "Pebble Mine; the State of Alaska's current administration; other pro-mine forces",
        "support": "Money; support in telling the story and vision of a world that doesn't eviscerate living systems for short-term profit",
    },
    {
        "name": "Just Transition / Native Movement",
        "location": "Alaska",
        "lat": 61.2181, "lon": -149.9003,
        "on_ground": "Coalition of organizations including Native Movement",
        "fighting": "An ethos of extraction manifesting in corporations, policies, and government actions",
        "support": "Money; support in telling the story and vision of a regenerative economy",
    },
    {
        "name": "Onondaga Land Back",
        "location": "New York",
        "lat": 43.0481, "lon": -76.1474,
        "on_ground": "Onondaga Nation (legal counsel); St. Regis Mohawk Tribe (Black Ash)",
        "fighting": "New York State / US government",
        "support": "Pressure on politicians; more publicity for the cause",
    },
    {
        "name": "Canoe Family Water & Climate Actions",
        "location": "Oregon",
        "lat": 45.5152, "lon": -122.6784,
        "on_ground": "Canoe Family",
        "fighting": "Oregon government",
        "support": "Not specified by respondent",
    },
    {
        "name": "Willamette Falls Return",
        "location": "Oregon",
        "lat": 45.3526, "lon": -122.6178,
        "on_ground": "Canoe Family (undamning of rivers / Willamette Falls)",
        "fighting": "Oregon government",
        "support": "Not specified by respondent",
    },
    {
        "name": "Lake Munson / Lake Jackson Protection",
        "location": "Florida",
        "lat": 30.4383, "lon": -84.2807,
        "on_ground": "Current group unknown; Seminole communities requesting inclusion",
        "fighting": "Plans to alter Lake Munson and Lake Jackson (water draw-down)",
        "support": "Not specified by respondent",
    },
]

PALETTE = ["#a21d11", "#8b0e0e", "#c83214"]
CREAM = "#f4eddf"
SAND = "#eee2bc"

us_bounds = [[18.0, -172.0], [72.0, -66.0]]

m = folium.Map(
    location=[44.0, -110.0],
    zoom_start=4,
    # Esri World Light Gray Canvas: same clean look as CartoDB positron,
    # but served without an API key (CARTO now watermarks unauthenticated tiles).
    tiles=(
        "https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/"
        "World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}"
    ),
    attr="Tiles &copy; Esri — Esri, DeLorme, NAVTEQ",
    control_scale=True,
    min_zoom=3,
    max_bounds=True,
)
m.fit_bounds(us_bounds)
m.options["maxBounds"] = us_bounds

# Subtle sand-colored title banner (minimal use of #eee2bc)
title_html = f"""
<div style="position: fixed; top: 10px; left: 50%; transform: translateX(-50%);
            background-color: {SAND}; padding: 8px 18px; border-radius: 6px;
            font-family: Helvetica, Arial, sans-serif; font-size: 15px;
            font-weight: 600; color: #2b2b2b; z-index: 9999;
            box-shadow: 0 2px 6px rgba(0,0,0,0.15);">
  Current local land/water protective efforts connected to our geographies
</div>
"""
m.get_root().html.add_child(folium.Element(title_html))

for i, e in enumerate(efforts):
    color = PALETTE[i % len(PALETTE)]
    popup_html = f"""
    <div style="font-family: Helvetica, Arial, sans-serif; min-width: 260px; max-width: 320px;">
      <div style="font-weight: 700; font-size: 14px; color: {color};">{e['name']}</div>
      <div style="font-size: 12px; color: #555; margin: 4px 0 8px 0;">{e['location']}</div>
      <div style="font-size: 12px; color: #2b2b2b; margin-top: 6px;">
        <div style="margin-bottom: 6px;"><span style="font-weight:600;">Who is on the ground:</span> {e['on_ground']}</div>
        <div style="margin-bottom: 6px;"><span style="font-weight:600;">Who/what is being fought:</span> {e['fighting']}</div>
        <div><span style="font-weight:600;">Support requested:</span> {e['support']}</div>
      </div>
    </div>
    """
    folium.CircleMarker(
        location=[e["lat"], e["lon"]],
        radius=9,
        color=color,
        weight=2,
        fill=True,
        fill_color=color,
        fill_opacity=0.85,
        popup=folium.Popup(popup_html, max_width=300),
    ).add_to(m)

OUT = Path(__file__).resolve().parent.parent / "docs" / "index.html"
OUT.parent.mkdir(parents=True, exist_ok=True)
m.save(str(OUT))
print(f"wrote {OUT}")
