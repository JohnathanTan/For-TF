import yfinance as yf
import numpy as np
import unittest
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as st
from scipy import optimize
import json

def apply_weights(weights, df):
    """
    Parameters
    ----------
    weights : dict
        Key = ticker, Value = weight in portfolio.
    df : pandas DataFrame
        Holds the return data of tickers. 
        The columns of this df must match the tickers in weight dict.

    Returns
    -------
    pandas Series
        Holds the portfolio return by summing the weighted returns of tickers.

    """
    case = unittest.TestCase()
    case.assertEqual(list(weights.keys()), list(df.columns)) # Assert that tickers are same
    
    df = df.copy()
    
    for ticker, weight in weights.items():
        df[ticker] *= weight
    
    series = df.sum(axis = 1)
    series.name = "Portfolio Returns (%)"
    
    return series


def plotter(x, cx, c, returns, xytext_dict={"VaR":(0.05, 0.25), "Median":(0.1, 0.9), "Mean":(0.7, 0.9)}, figsize=(10, 8), plot_title="Historical VaR on Daily Returns FY2016"):
    """
    This a mainly a plotting function to plot the distribution of daily returns.
    This plots a histogram and a PDF estimated by the Kernel Density Function.
    Additionally, this function calculates the mean and median values of the returns for added visualization.

    Parameters
    ----------
    x : float
        The VaR value.
    cx : float
        The CVaR Value.
    c : float
        The confidence level.
    returns : list-like
        A list of returns.
    xytext_dict : TYPE, optional
        Controls the text annotation position. The default is {"VaR":(0.05, 0.25), "Median":(0.1, 0.9), "Mean":(0.7, 0.9)}.
    figsize : tuple, optional
        Controls the figure size. The default is (10, 8).
    plot_title : TYPE, optional
        Controls the plot title. The default is "Historical VaR on Daily Returns FY2016".

    Returns
    -------
    fig : Figure instance of matplotlib.
        Final plot to be saved/viewed.

    """
    returns = returns.copy()
    c *= 100
    
    # Figure setup
    fig, ax = plt.subplots(figsize=figsize)
    
    # Plain Plot
    ax = sns.histplot(returns, stat='probability', kde=True, color='grey')
    ax.lines[0].set_color('red') # Set KDE Color
    
    ymin, ymax = ax.get_ylim() # y-values of Plot range
    xmin, xmax = ax.get_xlim() # y-values of Plot range
    data_x, data_y = ax.lines[0].get_data() # KDE Data
    
    # Annotate VaR & CVaR
    x_VaR = x
    y_VaR = np.interp(x_VaR, data_x, data_y) # y-value of KDE
    ax.axvline(x=x_VaR, ymax=y_VaR/ymax, linestyle='--', color='red')
    ax.annotate(text="VaR{}% = ".format(c)+str(round(x_VaR, 4))+" %\n" + "CVaR{}% = ".format(c)+str(round(cx, 4))+" %\n", 
                xy=(x_VaR, y_VaR),
                xytext=xytext_dict['VaR'],
                arrowprops=dict(arrowstyle="->", color='red', connectionstyle="arc3"),
                textcoords='axes fraction', color='red')
    
    # Annotate Median 
    x_median = portfolio_returns.quantile(1-0.5)
    y_median = np.interp(x_median, data_x, data_y) # y-value of KDE
    ax.axvline(x=x_median, linestyle=':', color='black')
    ax.annotate(text="Median = "+str(round(x_median, 4))+" %", 
                xy=(x_median, y_median),
                xytext=xytext_dict['Median'],
                arrowprops=dict(arrowstyle="->", color='black', connectionstyle="arc3"),
                textcoords='axes fraction', color='black')
    
    # Annotate Mean 
    x_mean = portfolio_returns.mean()
    y_mean = np.interp(x_mean, data_x, data_y) # y-value of KDE
    ax.axvline(x=x_mean, linestyle='-', color='blue')
    ax.annotate(text="Mean = "+str(round(x_mean, 4))+" %", 
                xy=(x_mean, y_mean),
                xytext=xytext_dict['Mean'],
                arrowprops=dict(arrowstyle="->", color='blue', connectionstyle="arc3"),
                textcoords='axes fraction', color='blue')
    
    ax.set_title(plot_title)
    
    return fig

def portfolio_optimizer(weights):
    """
    This is the optimizer function used for scipy.optimize.minimize
    As the optimizer function is a minimizer, this function will return -1 * portfolio_sharpe.
    To minimize the negative of sharpe is to maximize sharpe.

    Parameters
    ----------
    weights : list
        A list of weights in sequence of the keys of weights_dict.

    Returns
    -------
    float
        The negative of portfolio_sharpe. That is, -1 * portfolio_sharpe.

    """
    covar_matrix = daily_returns_single_month.cov()
    weight_series = pd.Series(weights, index=weights_dict.keys())
    
    case = unittest.TestCase()
    case.assertEqual(list(weights_dict.keys()), list(daily_returns_single_month.columns))
    
    portfolio_daily_returns = weight_series.dot(daily_returns_single_month.T)
    
    portfolio_variance = weight_series.dot(covar_matrix).dot(weight_series)
    portfolio_std = np.sqrt(portfolio_variance)
    portfolio_mean = portfolio_daily_returns.mean()
    portfolio_sharpe = (portfolio_mean-daily_rf_rate)/portfolio_std
    
    return -portfolio_sharpe
    
def weights_constraint(weights):
    """
    This is a contraint function used for scipy.optimize.minimize together with the portfolio_optimizer function.
    This constraint ensures that the absolute sum of weights == 1.

    Parameters
    ----------
    weights : list
        A list of weights in sequence of the keys of weights_dict.

    Returns
    -------
    int
        Absolute sum of weights - 1. This is for the 'equality' mode in scipy.optimize.minimize

    """
    return sum(map(abs, weights)) - 1

sns.set_style("dark")

# Download Dataset from yahoo finance
df = yf.download("AAPL IBM GOOG BP XOM COST GS", start="2016-01-01", end="2016-12-31")

# Retrieve only Adj Close prices & Drop first date which is < 2016-01-01
df = df.iloc[1:, :7]
# Drop multi-index column level
df.columns = df.columns.droplevel()

# Check for outlier data that falls outside the range [Q1 - 2*IQR, Q3 + 2*IQR]
quantiles = df.quantile([.25, .75], axis=0)
quantiles.loc['IQR', :] = quantiles.loc[0.75, :] - quantiles.loc[0.25, :]
quantiles.loc['Lower Bound', :] = quantiles.loc[0.25, :] - 2*quantiles.loc['IQR', :]
quantiles.loc['Upper Bound', :] = quantiles.loc[0.75, :] + 2*quantiles.loc['IQR', :]

# Quick description of data
for ticker in df.columns:
    print(df[ticker].describe())

# IQR Filter
for ticker in df.columns:
    ticker_lb = quantiles.loc['Lower Bound', ticker]
    ticker_ub = quantiles.loc['Upper Bound', ticker]
    for index, price in df.loc[:, ticker].items():
        if (price < ticker_lb) or (price > ticker_ub):
            print(ticker, index, price)
            
# Only GS's price got triggered, but it is not anomalous data. 
# Simply a sharp appreciation in price due to Trump's presidential election.

# Calculate Daily Returns
daily_returns = df.pct_change().dropna()*100

weights_dict = {
        "AAPL": 0.15,
        "BP":   0.15,
        "COST": 0.15,
        "GOOG": 0.20,
        "GS":   0.05,
        "IBM":  0.20,
        "XOM":  0.10,
    }

# Apply portfolio weights
portfolio_returns = apply_weights(weights_dict, daily_returns)

################################ Part a.
c = 0.95
VaR = portfolio_returns.quantile(1-c)
CVaR = portfolio_returns[portfolio_returns <= VaR].mean()
figure_VaR_historical = plotter(x=VaR, cx=CVaR, c=c, returns=portfolio_returns)
figure_VaR_historical.savefig("VaR Historical Method.jpg", dpi=300)

################################ Part b.
# Assume that Portfolio returns have a standard normal distribution
VaR_z = st.norm.ppf(1 - c) # At 95% Confidence, left tail standard normal z-score = -1.645
CVaR_z = -st.norm.pdf(VaR_z) / (1 - c)

covar_matrix = daily_returns.cov()

# Assert that the elements in the weight vector and covar matrix are identically arranged
case = unittest.TestCase()
case.assertEqual(list(weights_dict.keys()), list(covar_matrix.columns))

# Convert values of the weight dictionary to series for dot multiplication
weight_series = pd.Series(weights_dict.values(), index=weights_dict.keys())

portfolio_variance = weight_series.dot(covar_matrix).dot(weight_series)
portfolio_std = np.sqrt(portfolio_variance)
portfolio_mean = portfolio_returns.mean()

# Compute VaR and CVaR
VCV_VaR = (portfolio_mean + VaR_z*portfolio_std)
VCV_CVaR = (portfolio_mean + CVaR_z*portfolio_std)

figure_VaR_parametric = plotter(x=VCV_VaR, cx=VCV_CVaR, c=c, returns=portfolio_returns, plot_title="Parametric VaR (Std.Norm Assumption) on Daily Returns FY2016")
figure_VaR_parametric.savefig("VaR Parametric Method.jpg", dpi=300)

################################ Part c.
rf_rate = 0.0184  # Avg 10Y Yield in 2016 from https://www.macrotrends.net/2016/10-year-treasury-bond-rate-yield-chart
daily_rf_rate = rf_rate / np.sqrt(365)

optimal_weights = {}

for current_month in range(1, 13):
    
    # Calculate return for the Current Month
    monthly_returns = df[df.index.month == current_month]
    monthly_returns = (monthly_returns.iloc[-1] / monthly_returns.iloc[0] - 1)*100
    
    daily_returns_single_month = daily_returns[daily_returns.index.month == current_month]

    # Run optimizer
    # Constraints: absolute sum of weights == 1, individual weights are in the domain of [-1, 1]
    optimizer_results = optimize.minimize(fun=portfolio_optimizer, 
                                          x0=[0.2,0.2,0.2,0.1,0.1,0.1,0.1], 
                                          bounds=((-1, 1),(-1, 1),(-1, 1),(-1, 1),(-1, 1),(-1, 1),(-1, 1)), 
                                          constraints={'type': "eq", 'fun': weights_constraint})    
    
    # Create dictionary to save optimal results and statistics
    optimal_weights[current_month] = {'weights': [], 'sharpe': [], 'volatility':[], 'return':[]}
    
    if optimizer_results['success']:
        # If optimizer converges, save results
        covar_matrix = daily_returns_single_month.cov()
        weight_series = pd.Series(optimizer_results['x'].tolist(), index=weights_dict.keys())
        portfolio_daily_returns = weight_series.dot(daily_returns_single_month.T)
        
        portfolio_variance = weight_series.dot(covar_matrix).dot(weight_series)
        portfolio_std = np.sqrt(portfolio_variance)
        portfolio_mean = portfolio_daily_returns.mean()
        portfolio_sharpe = (portfolio_mean-daily_rf_rate)/portfolio_std
        
        # Save
        optimal_weights[current_month]['weights']       = optimizer_results['x'].tolist()
        optimal_weights[current_month]['sharpe']        = -optimizer_results['fun']
        optimal_weights[current_month]['volatility']    = portfolio_std
        optimal_weights[current_month]['return']        = weight_series.dot(monthly_returns)
    else:
        # Catch non-convergence
        print("Optimizer did not converge for Month {}. Check optimizer_results.".format(current_month))


# Save optimal weights to json
with open("optimal_weights.json", "w") as outfile:
    json.dump(optimal_weights, outfile)


# Plotting Setup
for_barplot = pd.DataFrame(data={
            "Month": [],
            "Ticker": [],
            "Weights": []
            
    })

for month, items in optimal_weights.items():
    for ticker, weight in zip(weights_dict.keys(), items['weights']):
        for_barplot.loc[len(for_barplot)] = [int(month), ticker, weight]

for_lineplot = pd.DataFrame(data={
            "Month": [],
            "Sharpe": [],
            "Volatility": [],
            "Return": [],
            
    })

for month, items in optimal_weights.items():
    for_lineplot.loc[len(for_lineplot)] = [int(month)-1, items["sharpe"], items["volatility"], items["return"]]


# Start plotting
fig, ax1 = plt.subplots(figsize=(10, 8))


ax2 = ax1.twinx()

for i in range(1, 13):
    ax1.axvline(x=i-.5, linestyle='-', color='white')

sns.barplot(x="Month", y="Weights", hue="Ticker", data=for_barplot, ax=ax1)

sns.lineplot(x="Month", y="Sharpe", label="Sharpe", color='black', marker='o', data=for_lineplot, ax=ax1)
sns.lineplot(x="Month", y="Volatility", label="Volatility", color='crimson', marker='o', data=for_lineplot, ax=ax2)
sns.lineplot(x="Month", y="Return", label="Return", marker='o', color='green', data=for_lineplot, ax=ax2)

ax1.set_xlabel('Month')
ax1.set_ylabel('Weights & Sharpe')
ax2.set_ylabel('Volatility & Return, %')

ax1.set_title("Optimal Portfolio Allocation by Month in FY2016")

fig.savefig("Optimal Portfolio Allocation")

################################ Print out answers
print("####################### ANSWERS #######################\n")
print("Part a.")
print("With the historical simulation method,\nthe VaR of the base portfolio is {}%\nthe CVaR of the base portfolio is {}%\n".format(-round(VaR, 4), -round(CVaR, 4)))
print("Part b.")
print("With the parametric method,\nthe VaR of the base portfolio is {}%\nthe CVaR of the base portfolio is {}%\n".format(-round(VCV_VaR, 4), -round(VCV_CVaR, 4)))
print("Part c.")
print("The optimial portfolio weights are:")
print(for_barplot.to_markdown(index=False))
print("\n####################### ANSWERS #######################")
