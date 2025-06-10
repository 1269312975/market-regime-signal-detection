# Volatility models (placeholder)
def ewma_volatility(series, span=20):
    return series.ewm(span=span).std()