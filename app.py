import dash
from dash import dcc, html
import plotly.express as px

# Sample data for demonstration purposes
schedule_data = {
    'Foundation': {'Planned_Days': 5, 'Actual_Days': 6},
    'Framing': {'Planned_Days': 10, 'Actual_Days': 8},
    'Roofing': {'Planned_Days': 3, 'Actual_Days': 2},
}

# Create a Dash app instance
app = dash.Dash(__name__)

# Layout of the app
app.layout = html.Div([
    html.H1("Task Progress Monitoring Dashboard"),
    
    # Dropdown for selecting tasks
    dcc.Dropdown(
        id='task-dropdown',
        options=[{'label': task, 'value': task} for task in schedule_data.keys()],
        value='Foundation'  # Default value
    ),
    
    # Graph to display task progress
    dcc.Graph(id='task-progress'),
])

# Callback to update the graph based on the selected task
@app.callback(
    dash.dependencies.Output('task-progress', 'figure'),
    [dash.dependencies.Input('task-dropdown', 'value')]
)
def update_progress(task):
    planned = schedule_data[task]['Planned_Days']
    actual = schedule_data[task]['Actual_Days']
    return {
        'data': [
            {'x': [task], 'y': [planned], 'type': 'bar', 'name': 'Planned'},
            {'x': [task], 'y': [actual], 'type': 'bar', 'name': 'Actual'},
        ],
        'layout': {
            'title': f'Task Progress for {task}',
            'barmode': 'group',
            'xaxis': {'title': 'Task'},
            'yaxis': {'title': 'Days'},
        },
    }

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8050))
    app.run(debug=True, host="0.0.0.0", port=port)


