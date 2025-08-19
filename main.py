import requests
import json
from datetime import datetime, timedelta

def fetch_mf_stats(scheme_code):
    url = f"https://api.mfapi.in/mf/{scheme_code}"
    resp = requests.get(url)
    data = resp.json()

    scheme_name = data.get("meta", {}).get("scheme_name", "Unknown")
    nav_data = data.get("data", [])

    parsed = []
    for entry in nav_data:
        try:
            date = datetime.strptime(entry["date"], "%d-%m-%Y")
            nav = float(entry["nav"])
            parsed.append((date, nav))
        except:
            continue

    parsed.sort(reverse=True)

    current_nav = parsed[0][1] if parsed else None
    today = parsed[0][0] if parsed else datetime.today()

    one_week_ago = today - timedelta(days=7)
    two_weeks_ago = today - timedelta(days=14)
    three_weeks_ago = today - timedelta(days=21)
    one_month_ago = today - timedelta(days=30)
    one_year_ago = today - timedelta(days=365)

    last_week = [nav for d, nav in parsed if d >= one_week_ago]
    last_2weeks = [nav for d, nav in parsed if d >= two_weeks_ago]
    last_3weeks = [nav for d, nav in parsed if d >= three_weeks_ago]
    last_month = [nav for d, nav in parsed if d >= one_month_ago]
    last_year = [nav for d, nav in parsed if d >= one_year_ago]

    max_nav_52 = max(last_year) if last_year else None
    min_nav_52 = min(last_year) if last_year else None

    def calc_return(arr):
        return ((arr[-1] - arr[0]) / arr[0] * 100) if len(arr) >= 2 else None

    one_week_return = calc_return(last_week)
    two_week_return = calc_return(last_2weeks)
    three_week_return = calc_return(last_3weeks)
    one_month_return = calc_return(last_month)

    return {
        "scheme_name": scheme_name,
        "scheme_code": scheme_code,
        "current_nav": round(current_nav, 4) if current_nav else None,
        "max_nav_52weeks": round(max_nav_52, 4) if max_nav_52 else None,
        "min_nav_52weeks": round(min_nav_52, 4) if min_nav_52 else None,
        "1_week_return_percent": round(one_week_return, 2) if one_week_return else None,
        "2_week_return_percent": round(two_week_return, 2) if two_week_return else None,
        "3_week_return_percent": round(three_week_return, 2) if three_week_return else None,
        "1_month_return_percent": round(one_month_return, 2) if one_month_return else None
    }


if __name__ == "__main__":
    schemes = []
    while True:
        code = input("Enter MF scheme code (or STOP to finish): ").strip()
        if code.upper() == "STOP":
            break
        if code.isdigit():
            schemes.append(int(code))

    results = [fetch_mf_stats(code) for code in schemes]

    # Sorting parameter
    sort_param = input("Enter sorting parameter (1w, 2w, 3w, 1m): ").strip().lower()
    key_map = {
        "1w": "1_week_return_percent",
        "2w": "2_week_return_percent",
        "3w": "3_week_return_percent",
        "1m": "1_month_return_percent"
    }
    if sort_param in key_map:
        results = sorted(results, key=lambda x: (x[key_map[sort_param]] is None, x[key_map[sort_param]]))

    # File name input
    file_name = input("Enter file name to save results (e.g., results.json): ").strip()
    if not file_name.endswith(".json"):
        file_name += ".json"

    with open(file_name, "w") as f:
        json.dump(results, f, indent=3)

    print(f"✅ Results written to {file_name} (sorted by {sort_param})")
