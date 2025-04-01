import matplotlib.pyplot as plt

def quick_histogram(x: pl.Series, bins=20):
    """Simple histogram"""
    data = series.to_numpy()
    plt.figure(figsize=(8, 5))
    plt.hist(data, bins=bins, color='skyblue', edgecolor='black')
    plt.title(f'Histogram of {series.columns}')
    plt.xlabel(series.columns)
    plt.ylabel('Frequency')
    plt.grid(alpha=0.3)
    plt.show()

def quick_scatter(x_series: pl.Series, y_series: pl.Series):
    """Simple scatter"""
    x_data = x_series.to_numpy()
    y_data = y_series.to_numpy()
    plt.figure(figsize=(8, 5))
    plt.scatter(x_data, y_data, alpha=0.7)
    plt.title(f'{y_series.columns} vs {x_series.columns}')
    plt.xlabel(x_series.columns)
    plt.ylabel(y_series.columns)
    plt.grid(alpha=0.3)
    plt.show()