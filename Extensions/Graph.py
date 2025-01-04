import plotly.express as px
import plotly.io as pio


class Graph:

    @staticmethod
    def generate_bar(data, x_label, y_label, title='Bar Chart'):

        # Create a bar chart using the specified x_label for the x-axis
        fig = px.bar(data_frame=data, x=x_label, y=y_label, title=title)

        # Update the layout to set the x-axis title to the capitalized x_label
        fig.update_layout(xaxis_title=x_label.capitalize(),
                          yaxis_title=y_label.capitalize())

        # Return the HTML representation of the figure
        return pio.to_html(fig, full_html=False)
