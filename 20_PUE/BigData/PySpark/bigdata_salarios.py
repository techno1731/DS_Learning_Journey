#!/usr/bin/env python3

import pandas as pd
from pandas_profiling import ProfileReport
import numpy as np
import matplotlib.pyplot as plt
import csv

df = pd.read_csv(r'Data/Salaries.csv')

profile = ProfileReport(df, title="Pandas Profiling Report")

profile.to_file("your_report.html")
