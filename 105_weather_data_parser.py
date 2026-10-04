"""105 - Weather Data Parser"""
from dataclasses import dataclass
from statistics import mean
import json

@dataclass
class WeatherRecord:
    city: str
    temperature: float
    humidity: float

class WeatherAnalyzer:
    def __init__(self, records):
        self.records = [
            WeatherRecord(
                item["city"],
                float(item["temperature"]),
                float(item["humidity"])
            )
            for item in records
        ]

    def average_temperature(self):
        return mean(r.temperature for r in self.records) if self.records else 0.0

    def average_humidity(self):
        return mean(r.humidity for r in self.records) if self.records else 0.0

    def hottest_city(self):
        return max(self.records, key=lambda r: r.temperature) if self.records else None

def main():
    data = [
        {"city": "Delhi", "temperature": 34, "humidity": 48},
        {"city": "Mumbai", "temperature": 30, "humidity": 72},
        {"city": "Bengaluru", "temperature": 26, "humidity": 65}
    ]

    print(json.dumps(data, indent=2))
    analyzer = WeatherAnalyzer(data)
    print("Average temperature:", analyzer.average_temperature())
    print("Average humidity:", analyzer.average_humidity())

    hottest = analyzer.hottest_city()
    print("Hottest city:", hottest.city if hottest else "N/A")

if __name__ == "__main__":
    main()
