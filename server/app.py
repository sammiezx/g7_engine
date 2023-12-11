from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

# Sample inventory data (replace this with your actual data)
inventory_data = pd.DataFrame({
    'Item': ['Item A', 'Item B', 'Item C'],
    'Stock': [100, 50, 75],
    'Reorder Level': [20, 30, 25]
})

# Sample forecast data (replace this with your actual data)
forecast_data = pd.DataFrame({
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
    'Forecast': [110, 60, 80]
})

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/inventory')
def inventory():
    # Convert DataFrame to HTML table
    inventory_table = inventory_data.to_html(classes='table table-striped table-bordered table-hover')

    # Create bar chart using Plotly Express
    bar_chart = px.bar(inventory_data, x='Item', y='Stock', title='Stock Levels')

    # Create pie chart using Plotly Express
    pie_chart = px.pie(inventory_data, names='Item', values='Stock', title='Stock Distribution')

    # Convert charts to HTML
    bar_chart_html = bar_chart.to_html(full_html=False)
    pie_chart_html = pie_chart.to_html(full_html=False)

    return render_template('inventory.html', inventory_table=inventory_table, bar_chart=bar_chart_html, pie_chart=pie_chart_html)


@app.route('/forecast')
def forecast():
    # Convert DataFrame to HTML table
    forecast_table = forecast_data.to_html(classes='table table-striped table-bordered table-hover')

    # Create bar chart using Plotly Express
    bar_chart = px.bar(forecast_data, x='Date', y='Forecast', title='Sales Forecast')

    # Create pie chart using Plotly Express
    pie_chart = px.pie(forecast_data, names='Date', values='Forecast', title='Forecast Distribution')

    # Convert charts to HTML
    bar_chart_html = bar_chart.to_html(full_html=False)
    pie_chart_html = pie_chart.to_html(full_html=False)

    # Create a non-interactive Matplotlib plot
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(forecast_data['Date'], forecast_data['Forecast'], marker='o', linestyle='-', color='b')
    ax.set_title('Sales Forecast (Matplotlib)')
    ax.set_xlabel('Date')
    ax.set_ylabel('Forecast')
    ax.grid(True)

    # Save Matplotlib plot to a BytesIO buffer
    img_buffer = BytesIO()
    fig.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    img_data = base64.b64encode(img_buffer.read()).decode('utf-8')
    plt.close(fig)

    return render_template('forecast.html', forecast_table=forecast_table, bar_chart=bar_chart_html, pie_chart=pie_chart_html, matplotlib_plot=img_data)


if __name__ == '__main__':
    app.run(debug=True)
