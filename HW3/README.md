# HW3 - Data Visualization with Matplotlib

This assignment focuses on **Matplotlib**, a core library for data visualization in Python. You will create various plots to analyze interaction data from our AI research scenario.

## AI Research Scenario: AI-Assisted Customer Support Response Generation

### Scenario Overview
In modern customer service operations, human agents are often assisted by Large Language Models (LLMs) that pre-draft responses based on the customer's inquiry. This scenario models a human-in-the-loop setup where a customer sends a message, an AI assesses it and formulates a response, and a human agent reviews, edits, and sends the final response.

This research scenario explores the dynamics of **Human-AI Collaboration**. 

### Research Tasks & Questions
This dataset enables researchers to explore several NLP and human-computer interaction (HCI) queries:
1. **Reliance on AI:** Does a higher AI confidence score correlate with a shorter human editing time and lower edit distance?
2. **Quality vs. Speed:** Do faster response times (lower `agent_time_taken_sec`) lead to lower or higher `customer_satisfaction_score`?
3. **Draft Intervention:** By calculating the exact edit distance (or semantic similarity) between the `ai_suggestion` and `agent_final_response`, researchers can evaluate how much the human actually changes the text across different inquiry types (e.g., technical support vs. shipping delays).

### Procedure
1. A customer submits an inquiry (`customer_inquiry`) categorized into specific types (shipping, damage, etc.).
2. The AI generates an initial draft (`ai_suggestion`) and attaches a confidence score (`ai_confidence_score`) indicating how certain it is that the response completely answers the question.
3. The human agent views the draft, edits it if necessary (`agent_edit_distance_chars`), and sends the `agent_final_response`. The time taken to review/edit is recorded (`agent_time_taken_sec`).
4. The customer receives the response and rates their interaction out of 5 (`customer_satisfaction_score`).

### Data Format (JSON Schema)
The dataset is provided as a JSON array of objects in `hypothetical_scenario_data.json`. Each object has the following structure:

```json
{
    "interaction_id": "interaction_1000",
    "inquiry_type": "shipping", 
    "customer_inquiry": "Where is my package? It was supposed to arrive ...",
    "ai_suggestion": "I apologize for the delay...",
    "agent_final_response": "I apologize for the delay... We value your business!",
    "metrics": {
        "ai_confidence_score": 0.85,           // Float (0.0 - 1.0): AI's internal confidence in its draft.
        "agent_time_taken_sec": 34,            // Integer: Seconds the human agent took to review/edit.
        "agent_edit_distance_chars": 24,       // Integer: Character difference between AI draft and Agent final. 
        "customer_satisfaction_score": 4.5     // Float (1.0 - 5.0): Customer survey rating.
    }
}
```

---

## Instructions

For this homework, you will test your matplotlib knowledge by answering dataset specific questions.
Complete the problems in the following file:
1. `HW3/problems.py`

Write your plotting code between the `# START PROBLEM X HERE` and `# END PROBLEM X HERE` comments. The script will automatically save your plots to the `HW3/results/` folder. Ensure every plot has a title, x and y axis labels, and a legend where appropriate.

Examples of these plots are shown in the `HW3/examples/` folder.

### 1. Agent Time Taken: Edited vs. Unedited (Grouped Bar Chart)
Analyze whether human agents take significantly longer when they edit an AI draft compared to when they accept it as-is. Create a grouped bar chart displaying the mean `agent_time_taken_sec`, grouped by `inquiry_type`.
- **X-axis**: Inquiry Type (with tick labels for each category).
- **Y-axis**: Average Time Taken (Seconds).
- **Data Series**: For each inquiry type, plot two bars side-by-side: 
  - "Unedited" (where `agent_edit_distance_chars == 0`)
  - "Edited" (where `agent_edit_distance_chars > 0`)
- **Required Details**: Legend, Title, Axis Labels.
- **Output**: Saved as `bar_grouped_time.png`

### 2. Time vs. Satisfaction by Inquiry Type (Colored Scatter Plot)
Investigate the relationship between processing time and customer satisfaction, keeping in mind the context of the inquiry. 
- **X-axis**: Agent Time Taken (Seconds).
- **Y-axis**: Customer Satisfaction Score.
- **Data Series**: Plot a scatter point for each interaction. Color-code the points base on their `inquiry_type`.
- **Required Details**: Legend showing the colors for each inquiry type, Title, Axis Labels.
- **Output**: Saved as `scatter_time_vs_csat.png`

### 3. Time Distribution: High vs. Low AI Confidence (Overlaid Histograms)
Do agents spend notably different amounts of time reviewing drafts depending on the AI's internal confidence? Split the data into two subsets: High Confidence (`ai_confidence_score >= 0.80`) and Low Confidence (`ai_confidence_score < 0.80`).
- **X-axis**: Agent Time Taken (Seconds).
- **Y-axis**: Frequency / Count.
- **Data Series**: Plot two histograms on the exact same axes. Use transparency (`alpha=0.6`) so overlap can be seen.
- **Required Details**: Legend ("High Confidence", "Low Confidence"), Title, Axis Labels.
- **Output**: Saved as `hist_overlaid_time.png`

### 4. Satisfaction Trend with Variance Bounds (Line Plot with Shaded Region)
In reinforcement learning and AI system monitoring, it's common to visualize performance trends over time using rolling averages and shaded variance bounds. Treat the sequence of the dataset (index 0 to N) as chronological time. 
- **Data Prep**: Calculate a rolling mean and rolling standard deviation of the `customer_satisfaction_score` using a window size of 20 interactions. *(Hint: You may use pandas or numpy for this calculation).*
- **X-axis**: Interaction Index (Chronological time).
- **Y-axis**: Customer Satisfaction Score.
- **Data Series 1**: A solid line representing the rolling mean.
- **Data Series 2**: A shaded region (`plt.fill_between`) spanning from (Mean - 1 StdDev) to (Mean + 1 StdDev).
- **Required Details**: Legend ("Rolling Mean", "$\pm 1$ Std Dev"), Title, Axis Labels.
- **Output**: Saved as `line_rolling_satisfaction.png`

