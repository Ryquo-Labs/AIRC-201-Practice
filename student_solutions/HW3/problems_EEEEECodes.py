import json
import matplotlib.pyplot as plt
import numpy as np
import os
from collections import defaultdict
import pandas as pd

# Ensure results directory exists relative to this script
script_dir = os.path.dirname(os.path.abspath(__file__))
results_dir = os.path.join(script_dir, "results")
os.makedirs(results_dir, exist_ok=True)

# Load data
data_path = os.path.join(script_dir, 'hypothetical_scenario_data.json')
with open(data_path, 'r') as f:
    data = json.load(f)

def safe_get(entry, key):
    if not isinstance(entry, dict):
        return None

    if key in entry:
        val = entry[key]
    else:
        val = entry.get("metrics", {}).get(key)

    if val is None:
        return None
    try:
        return float(val)
    except Exception:
        return None

# ---------------------------------------------------------
# PROBLEM 1: Agent Time Taken: Edited vs. Unedited
# ---------------------------------------------------------

# START PROBLEM 1 HERE
unedited_times = defaultdict(list)
edited_times = defaultdict(list)

for entry in data:
    if not isinstance(entry, dict):
        continue
    itype = entry.get("inquiry_type")
    t = safe_get(entry, "agent_time_taken_sec")
    edit = safe_get(entry, "agent_edit_distance_chars")
    if itype is None or t is None or edit is None:
        continue
    if edit == 0:
        unedited_times[itype].append(t)
    else:
        edited_times[itype].append(t)

# Prepare sorted inquiry types
all_types = sorted(set(list(unedited_times.keys()) + list(edited_times.keys())))
unedited_means = [np.mean(unedited_times[t]) if len(unedited_times[t])>0 else 0 for t in all_types]
edited_means = [np.mean(edited_times[t]) if len(edited_times[t])>0 else 0 for t in all_types]

x = np.arange(len(all_types))
width = 0.35
fig, ax = plt.subplots(figsize=(10,6))
ax.bar(x - width/2, unedited_means, width, label='Unedited (edit_distance=0)')
ax.bar(x + width/2, edited_means, width, label='Edited (edit_distance>0)')
ax.set_xticks(x)
ax.set_xticklabels(all_types, rotation=45, ha='right')
ax.set_ylabel('Mean Agent Time (sec)')
ax.set_title('Mean Agent Time by Inquiry Type: Edited vs Unedited')
ax.legend()
plt.tight_layout()
fig.savefig(os.path.join(results_dir, "bar_grouped_time.png"))
plt.close(fig)
# END PROBLEM 1 HERE

# ---------------------------------------------------------
# PROBLEM 2: Time vs. Satisfaction by Inquiry Type
# ---------------------------------------------------------

# START PROBLEM 2 HERE
# Collect points and map colors
points = defaultdict(lambda: {"t": [], "csat": []})
for entry in data:
    if not isinstance(entry, dict):
        continue
    itype = entry.get("inquiry_type")
    t = safe_get(entry, "agent_time_taken_sec")
    csat = safe_get(entry, "customer_satisfaction_score")
    if itype is None or t is None or csat is None:
        continue
    points[itype]["t"].append(t)
    points[itype]["csat"].append(csat)

colors = plt.get_cmap('tab10')
fig, ax = plt.subplots(figsize=(8,6))
for i, (itype, vals) in enumerate(sorted(points.items())):
    ax.scatter(vals["t"], vals["csat"], label=itype, color=colors(i % 10), alpha=0.7, edgecolors='w', s=60)
ax.set_xlabel('Agent Time Taken (sec)')
ax.set_ylabel('Customer Satisfaction Score')
ax.set_title('Agent Time vs Customer Satisfaction by Inquiry Type')
ax.legend(title='Inquiry Type', bbox_to_anchor=(1.05,1), loc='upper left')
plt.tight_layout()
fig.savefig(os.path.join(results_dir, "scatter_time_vs_csat.png"))
plt.close(fig)
# END PROBLEM 2 HERE

# ---------------------------------------------------------
# PROBLEM 3: Time Distribution by AI Confidence Score
# ---------------------------------------------------------

# START PROBLEM 3 HERE
high_times = []
low_times = []
for entry in data:
    if not isinstance(entry, dict):
        continue
    t = safe_get(entry, "agent_time_taken_sec")
    conf = safe_get(entry, "ai_confidence_score")
    if t is None or conf is None:
        continue
    if conf >= 0.8:
        high_times.append(t)
    else:
        low_times.append(t)

fig, ax = plt.subplots(figsize=(8,6))
bins = 30
ax.hist(low_times, bins=bins, alpha=0.6, label='Low Confidence (<0.8)', color='orange', density=False)
ax.hist(high_times, bins=bins, alpha=0.6, label='High Confidence (>=0.8)', color='teal', density=False)
ax.set_xlabel('Agent Time Taken (sec)')
ax.set_ylabel('Count')
ax.set_title('Agent Time Distribution by AI Confidence Score')
ax.legend()
plt.tight_layout()
fig.savefig(os.path.join(results_dir, "hist_overlaid_time.png"))
plt.close(fig)
# END PROBLEM 3 HERE

# ---------------------------------------------------------
# PROBLEM 4: Satisfaction Trend with Variance Bounds
# ---------------------------------------------------------

# START PROBLEM 4 HERE
csat_list = []
for entry in data:
    if not isinstance(entry, dict):
        continue
    csat = safe_get(entry, "customer_satisfaction_score")
    # preserve sequence; use NaN for missing so rolling handles properly
    csat_list.append(np.nan if csat is None else csat)

csat_series = pd.Series(csat_list)
window = 20
rolling_mean = csat_series.rolling(window=window, min_periods=1).mean()
rolling_std = csat_series.rolling(window=window, min_periods=1).std().fillna(0)

fig, ax = plt.subplots(figsize=(10,6))
x_idx = np.arange(len(csat_series))
ax.plot(x_idx, rolling_mean, label=f'Rolling Mean (window={window})', color='blue')
ax.fill_between(x_idx, rolling_mean - rolling_std, rolling_mean + rolling_std, color='blue', alpha=0.2, label='±1 Std Dev')
ax.set_xlabel('Interaction Index')
ax.set_ylabel('Customer Satisfaction Score')
ax.set_title('Rolling Satisfaction Trend with ±1 Std Dev')
ax.legend()
plt.tight_layout()
fig.savefig(os.path.join(results_dir, "line_rolling_satisfaction.png"))
plt.close(fig)
# END PROBLEM 4 HERE

print(f"All plots generated and saved in {results_dir}")

