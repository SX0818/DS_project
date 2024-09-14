## Time Series Forecasting with Prophet

This section of the notebook demonstrates the use of the Prophet library for forecasting time series data. Prophet, developed by Facebook, is robust to missing data, shifts in the trend, and large outliers, making it well-suited for daily observations that have seasonal patterns.

### Data Preparation

The data used in this example consists of daily records of milk production. The dataset is first loaded, and the date column is converted to a datetime type to ensure compatibility with Prophet, which requires the date column to be named `ds` and the metric to forecast to be named `y`.

### Model Setup

A new Prophet model is instantiated and then fitted with the training data. This training data comprises 80% of the total dataset, allowing the remaining 20% to be used for model validation.

Useful article like: https://towardsdatascience.com/getting-started-predicting-time-series-data-with-facebook-prophet-c74ad3040525