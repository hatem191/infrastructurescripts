#Automated False Positive Analysis in Alerts

import pandas as pd

def filter_false_positives(alerts_file):
    df = pd.read_csv(alerts_file)
    false_positive_threshold = 0.8
    filtered_alerts = df[df['false_positive_rate'] < false_positive_threshold]
    filtered_alerts.to_csv('filtered_alerts.csv', index=False)
    print("Filtered alerts saved to 'filtered_alerts.csv'")

# Example usage
filter_false_positives('alerts.csv')
