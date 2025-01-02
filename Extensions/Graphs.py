from dash import Dash, dcc, html
import plotly.express as px


class Graph:
    def __init__(self, server):
        """Initialize the GraphGenerator with Dash app setup."""
        self.app = Dash(__name__, server=server,
                        url_base_pathname='/dash/')  # Initialize Dash app inside the class
        self.app.layout = html.Div("Això és una pàgina Dash!")

    def generate_graph(self, data, x_label, y_label, title=''):
        """Generate a bar graph using Plotly Express and return the Dash app's index page."""
        # Generate the bar chart figure
        fig = px.bar(data, x=x_label, y=y_label, title=title)

        # Set up the Dash layout with the graph
        self.app.layout = html.Div([
            dcc.Graph(figure=fig)
        ])

        # Return the rendered Dash app layout (i.e., the index page)
        return self.app.index()
