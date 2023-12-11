import sys
sys.path.append("/home/samir/Desktop/ARIMA")
import pandas as pd
import xgboost as xgb
from g7.lib.inventory.optimization import optimize_inventory


# Load your dataset
# Ensure your dataset has columns: 'ds' for timestamps, 'y' for sales, and other features
def forecast_model(df, df_leadtime):
    df['ds'] = pd.to_datetime(df['ds'])

    # Feature engineering: Add lead time as a feature
    # Note: Replace 'your_leadtime_dataset.csv' with your actual lead time dataset

    df_leadtime['order_date'] = pd.to_datetime(df_leadtime['order_date'])
    df_leadtime['arrival_date'] = pd.to_datetime(df_leadtime['arrival_date'])
    df_leadtime['lead_time'] = (df_leadtime['arrival_date'] - df_leadtime['order_date']).dt.days
    df_leadtime.drop(['order_date'], axis=1, inplace=True)
    df = pd.merge(df, df_leadtime[['ds', 'lead_time']], on='ds', how='left')

    # Split data into training and testing sets
    train_size = int(len(df) * 0.8)
    train, test = df.iloc[:train_size], df.iloc[train_size:]

    # Train the forecasting model using XGBoost
    model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, max_depth=5)
    model.fit(train.drop(columns=['y']), train['y'])

    # Make future data frame for forecasting
    future = pd.DataFrame(index=test.index)
    future['promotion'] = test['promotion']  # Replace with actual promotion data
    future['lead_time'] = test['lead_time']  # Replace with actual lead time data

    # Forecast sales
    forecast = model.predict(future)

    # Add forecast values to the test set
    test['yhat'] = forecast

    # Run the optimization using the forecasted data
    optimized_orders = optimize_inventory(test)

    return optimized_orders
