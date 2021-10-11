## File Types 

* Q1. SQL file
* Q2. Python file 
* Q3. Python file
* Q4. Python file 
* Q5. Bash script (requires Git)
* Q6. TXT file

## Outputs

Q5. [script output](https://github.com/JohnathanTan/For-TF/blob/main/q5%20output.PNG)

## Dependencies 

Python files are written with the version 3.8.10

Libraries used for Q4
```
import yfinance as yf
import numpy as np
import unittest
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as st
from scipy import optimize
import json
import os
```

The yfinance module had an update ~July 2021. You would need to update it or else it will show a JSONDecodeError when pulling ticker price data.
```
pip uninstall yfinance
pip install yfinance --upgrade --no-cache-dir
```

## Assumptions

Q4. 
In the parametric CVaR/VaR calculation, I assume a standard normal distribution of daily returns.
In the optimization solution, I assume that the weights of each asset can take on any value in the domain [-1, 1] but ensured that their absolute sum is equals to 1.

Q5. 
I assume that all python files that the script is looping through are without syntax errors.

## Additional Notes

Q4.
Optimal weights are saved in a optimal_weights.json file.
Plots will be saved as jpg files.

Q5. 
I was not sure if there was a requirement for a particular type of script. I decided to do it via a shell script without using any other downloaded libraries. Within the shell script there are only git & bash commands. 

To be frank, I have little experience with shell scripting so there might be some inefficient logic within the script (I might be using the wrong terminologies too). But, I am sure that I got the right outputs for the task at hand.

I have included some dummy data to check against my script. The dummy folder is titled the same way as the question "my-python-project". To test it against another folder, you would need to change the "project_dir" variable at line 2 of the script.

I run the file on my Windows desktop with the command "sh q5.sh" from the base directory of the repo.
