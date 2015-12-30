# Teste.py

import datetime
import numpy as np
import pandas.io.data as web
from scipy.stats import norm

def var_cov_var(P, c, mu, sigma):
    """
    Variance-Covariance calculation of daily Value-at-Risk
    using confidence level c, with mean of returns mu
    and standard deviation of returns sigma, on a portfolio
    of value P.
    """
    alpha = norm.ppf(1-c, mu, sigma)
    return P - P*(alpha + 1)    

if __name__ == "__main__":
    start = datetime.datetime(2010, 1, 1)
    end = datetime.datetime(2014, 1, 1)

    stock = web.DataReader("PBR", 'yahoo', start, end)
    stock["rets"] = stock["Adj Close"].pct_change()

    P = 1e6   # 1,000,000 USD
    c = 0.95  # 99% confidence interval
    mu = np.mean(stock["rets"])
    sigma = np.std(stock["rets"])

    var = var_cov_var(P, c, mu, sigma)
    s = 'Value-at-Risk: $%0.2f' % var
    print (s)