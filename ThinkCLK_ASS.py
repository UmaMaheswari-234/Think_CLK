import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Load the dataset
data = pd.read_csv(r"metadata.csv")

# Inspect columns
print("Columns in the dataset:", data.columns)

# Clean column names
data.columns = data.columns.str.strip()

# Add 'cycle_count' if it's missing
if 'cycle_count' not in data.columns:
    data['cycle_count'] = range(1, len(data) + 1)

# Extract relevant data
relevant_data = data[['cycle_count', 'Re', 'Rct']]  # Match column names
relevant_data = relevant_data.dropna(subset=['Re', 'Rct'])

# Preview cleaned data
print(relevant_data.head())

# Create plots using Plotly
# Create subplots
fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
                    subplot_titles=("Electrolyte Resistance (Re) Over Cycle Count", 
                                    "Charge Transfer Resistance (Rct) Over Cycle Count"))

# Add line plot for Re
fig.add_trace(go.Scatter(x=relevant_data['cycle_count'], 
                         y=relevant_data['Re'], 
                         mode='lines+markers', 
                         name='Re (Ohms)',
                         line=dict(color='blue')),
              row=1, col=1)

# Add line plot for Rct
fig.add_trace(go.Scatter(x=relevant_data['cycle_count'], 
                         y=relevant_data['Rct'], 
                         mode='lines+markers', 
                         name='Rct (Ohms)',
                         line=dict(color='red')),
              row=2, col=1)

# Update layout
fig.update_layout(title="Battery Impedance Parameters Over Charge/Discharge Cycles",
                  xaxis_title="Cycle Count",
                  height=700,
                  showlegend=True)

# Show the plot
fig.show()

# Optional - Save the plot as an HTML file
fig.write_html("battery_impedance_analysis.html")
