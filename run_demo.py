#!/usr/bin/env python3
"""
Lightweight demo that downloads hourly temperature from Open-Meteo, writes CSV/parquet,
and produces a small PNG for quick visualization.
"""
import argparse
import os
import requests
import pandas as pd
import matplotlib.pyplot as plt

API_URL = "https://api.open-meteo.com/v1/forecast"

def fetch_hourly_temperature(lat, lon, start_date, end_date):
    params = {
        "latitude": lat,
        "longitude": lon,
        "start_date": start_date,
        "end_date": end_date,
        "hourly": "temperature_2m",
        "timezone": "UTC",
    }
    r = requests.get(API_URL, params=params, timeout=30)
    r.raise_for_status()
    payload = r.json()
    hourly = payload.get("hourly", {})
    times = hourly.get("time", [])
    temps = hourly.get("temperature_2m", [])
    df = pd.DataFrame({"time": times, "temperature_2m": temps})
    df["time"] = pd.to_datetime(df["time"])  # localize/convert downstream as needed
    return df

def save_outputs(df, out_dir="examples/output"):
    os.makedirs(out_dir, exist_ok=True)
    csv_path = os.path.join(out_dir, "weather.csv")
    parquet_path = os.path.join(out_dir, "weather.parquet")
    img_path = os.path.join(out_dir, "temperature.png")

    df.to_csv(csv_path, index=False)
    try:
        df.to_parquet(parquet_path, index=False)
    except Exception:
        # pyarrow optional — skip if not available
        pass
    df.set_index("time")["temperature_2m"].plot(title="Temperature (2m)")
    plt.ylabel("°C")
    plt.tight_layout()
    plt.savefig(img_path)
    print("Saved:", csv_path, parquet_path, img_path)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--lat", type=float, required=True)
    parser.add_argument("--lon", type=float, required=True)
    parser.add_argument("--start", type=str, required=True)
    parser.add_argument("--end", type=str, required=True)
    args = parser.parse_args()

    df = fetch_hourly_temperature(args.lat, args.lon, args.start, args.end)
    save_outputs(df)

if __name__ == "__main__":
    main()
