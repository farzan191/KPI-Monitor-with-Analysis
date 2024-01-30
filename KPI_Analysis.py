import time
import random
from datetime import datetime, timedelta

class KPI:
    def __init__(self, name, threshold):
        self.name = name
        self.values = []
        self.threshold = threshold

    def update_value(self):
        # Simulate data changes (replace with actual data source)
        new_value = random.randint(0, 100)
        self.values.append(new_value)
        return new_value

    def calculate_average(self, window_size):
        if len(self.values) < window_size:
            return None  # Not enough data for analysis yet
        else:
            window_values = self.values[-window_size:]
            return sum(window_values) / window_size

def monitor_kpi(kpi, interval_seconds, analysis_window):
    while True:
        new_value = kpi.update_value()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Calculate average over the specified time window
        average_value = kpi.calculate_average(analysis_window)

        if average_value is not None and average_value > kpi.threshold:
            alert_message = (
                f"ALERT: {kpi.name} average exceeded threshold at {timestamp} - "
                f"Average Value: {average_value}, Current Value: {new_value}"
            )
            print(alert_message)
            # You can send an alert (email, notification, etc.) here

        time.sleep(interval_seconds)

if __name__ == "__main__":
    # Define a sample KPI with a threshold
    sample_kpi = KPI("Revenue", 80)

    # Set the monitoring interval (in seconds) and analysis window (in data points)
    monitoring_interval = 5
    analysis_window = 10

    # Start monitoring the KPI
    monitor_kpi(sample_kpi, monitoring_interval, analysis_window)
