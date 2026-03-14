import json
import matplotlib.pyplot as plt
import numpy as np
import os
from collections import defaultdict

# Ensure results directory exists relative to this script
script_dir = os.path.dirname(os.path.abspath(__file__))
results_dir = os.path.join(script_dir, "results")
os.makedirs(results_dir, exist_ok=True)

# Load data
data_path = os.path.join(script_dir, 'hypothetical_scenario_data.json')
with open(data_path, 'r') as f:
    data = json.load(f)

# ---------------------------------------------------------
# PROBLEM 1: Agent Time Taken: Edited vs. Unedited
# ---------------------------------------------------------

# START PROBLEM 1 HERE
# TODO: Group data by inquiry_type and calculate the mean agent_time_taken_sec 
#       for unedited (agent_edit_distance_chars == 0) and edited (> 0) drafts.
# TODO: Create a grouped bar chart with two bars per inquiry type.
# TODO: Add title, axis labels, and a legend.


# END PROBLEM 1 HERE

plt.savefig(os.path.join(results_dir, "bar_grouped_time.png"))
plt.close()

# ---------------------------------------------------------
# PROBLEM 2: Time vs. Satisfaction by Inquiry Type
# ---------------------------------------------------------

# START PROBLEM 2 HERE
# TODO: Create a scatter plot of agent_time_taken_sec vs. customer_satisfaction_score.
# TODO: Color-code the scatter markers based on inquiry_type.
# TODO: Add title, axis labels, and a legend explaining the colors.


# END PROBLEM 2 HERE

plt.savefig(os.path.join(results_dir, "scatter_time_vs_csat.png"))
plt.close()

# ---------------------------------------------------------
# PROBLEM 3: Time Distribution by AI Confidence Score
# ---------------------------------------------------------

# START PROBLEM 3 HERE
# TODO: Split the dataset into high confidence (>= 0.8) and low confidence (< 0.8).
# TODO: Plot an overlaid histogram of agent_time_taken_sec for both groups.
#       (Hint: use alpha parameter to make colors transparent).
# TODO: Add title, axis labels, and a legend identifying the two distributions.


# END PROBLEM 3 HERE

plt.savefig(os.path.join(results_dir, "hist_overlaid_time.png"))
plt.close()

# ---------------------------------------------------------
# PROBLEM 4: Satisfaction Trend with Variance Bounds
# ---------------------------------------------------------

# START PROBLEM 4 HERE
# TODO: Calculate a rolling mean and rolling standard deviation for 
#       customer_satisfaction_score using a window size of 20.
#       (Hint: You can use pandas or numpy arrays).
# TODO: Plot the rolling mean as a solid line across the interaction index.
# TODO: Use plt.fill_between to create a shaded region spanning from 
#       (Mean - 1 Std Dev) to (Mean + 1 Std Dev).
# TODO: Add title, axis labels, and a legend for the mean line and variance bounds.


# END PROBLEM 4 HERE

plt.savefig(os.path.join(results_dir, "line_rolling_satisfaction.png"))
plt.close()

print(f"All plots generated and saved in {results_dir}")

