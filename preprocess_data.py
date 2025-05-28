import pandas as pd
import numpy as np
from io import StringIO
from sklearn.linear_model import LinearRegression
import json

# file paths
file_paths = {
    "SS_HS": "C:\\Users\\PrincipalWang\\OneDrive\\桌面\\final project\\blood-pressure-in-salt-sensitive-dahl-rats-1.0.0\\SS_HS.txt",
    "SS_LS": "C:\\Users\\PrincipalWang\\OneDrive\\桌面\\final project\\blood-pressure-in-salt-sensitive-dahl-rats-1.0.0\\SS_LS.txt",
    "SSBN13_HS": "C:\\Users\\PrincipalWang\\OneDrive\\桌面\\final project\\blood-pressure-in-salt-sensitive-dahl-rats-1.0.0\\SSBN13_HS.txt",
    "SSBN13_LS": "C:\\Users\\PrincipalWang\\OneDrive\\桌面\\final project\\blood-pressure-in-salt-sensitive-dahl-rats-1.0.0\\SSBN13_LS.txt"
}

# preprocess SS_HS
with open(file_paths["SS_HS"], "r") as f:
    lines = [line for line in f if not line.strip().startswith("//")] # Remove comment lines
ss_hs = pd.read_csv(StringIO("".join(lines)), sep="\t", header=None).dropna(how="any") # Read data and drop empty rows
ss_hs = ss_hs.iloc[::20, :].reset_index(drop=True) # Downsample to 5Hz

ss_hs_js = {}
for i in ss_hs.columns:
    X = np.arange(len(ss_hs)).reshape(-1, 1) # Time indices
    y = ss_hs[i].values.reshape(-1, 1) # Blood pressure values for one rat
    slope = LinearRegression().fit(X, y).coef_[0][0] # Fit linear regression and get slope
    ss_hs_js[f"rat_{i}"] = {
        "values": ss_hs[i].round(3).tolist(),
        "slope": round(slope, 2)
    }

# preprocess SS_LS
with open(file_paths["SS_LS"], "r") as f:
    lines = [line for line in f if not line.strip().startswith("//")] # Remove comment lines
ss_ls = pd.read_csv(StringIO("".join(lines)), sep="\t", header=None).dropna(how="any") # Read data and drop empty rows
ss_ls = ss_ls.iloc[::20, :].reset_index(drop=True) # Downsample to 5Hz

ss_ls_js = {}
for i in ss_ls.columns:
    X = np.arange(len(ss_ls)).reshape(-1, 1) # Time indices
    y = ss_ls[i].values.reshape(-1, 1) # Blood pressure values for one rat
    slope = LinearRegression().fit(X, y).coef_[0][0] # Fit linear regression and get slope
    ss_ls_js[f"rat_{i}"] = {
        "values": ss_ls[i].round(3).tolist(),
        "slope": round(slope, 2)
    }

# preprocess SSBN13_HS
with open(file_paths["SSBN13_HS"], "r") as f:
    lines = [line for line in f if not line.strip().startswith("//")] # Remove comment lines
ssbn13_hs = pd.read_csv(StringIO("".join(lines)), sep="\t", header=None).dropna(how="any") # Read data and drop empty rows
ssbn13_hs = ssbn13_hs.iloc[::20, :].reset_index(drop=True) # Downsample to 5Hz

ssbn13_hs_js = {}
for i in ssbn13_hs.columns:
    X = np.arange(len(ssbn13_hs)).reshape(-1, 1) # Time indices
    y = ssbn13_hs[i].values.reshape(-1, 1) # Blood pressure values for one rat
    slope = LinearRegression().fit(X, y).coef_[0][0] # Fit linear regression and get slope
    ssbn13_hs_js[f"rat_{i}"] = {
        "values": ssbn13_hs[i].round(3).tolist(),
        "slope": round(slope, 2)
    }

# preprocess SSBN13_LS
with open(file_paths["SSBN13_LS"], "r") as f:
    lines = [line for line in f if not line.strip().startswith("//")] # Remove comment lines
ssbn13_ls = pd.read_csv(StringIO("".join(lines)), sep="\t", header=None).dropna(how="any") # Read data and drop empty rows
ssbn13_ls = ssbn13_ls.iloc[::20, :].reset_index(drop=True) # Downsample to 5Hz

ssbn13_ls_js = {}
for i in ssbn13_ls.columns:
    X = np.arange(len(ssbn13_ls)).reshape(-1, 1) # Time indices
    y = ssbn13_ls[i].values.reshape(-1, 1) # Blood pressure values for one rat
    slope = LinearRegression().fit(X, y).coef_[0][0] # Fit linear regression and get slope
    ssbn13_ls_js[f"rat_{i}"] = {
        "values": ssbn13_ls[i].round(3).tolist(),
        "slope": round(slope, 2)
    }

# combine and save as JSON
time = list(range(len(ss_hs))) 

final_json = {
    "SS_HS": ss_hs_js,
    "SS_LS": ss_ls_js,
    "SSBN13_HS": ssbn13_hs_js,
    "SSBN13_LS": ssbn13_ls_js,
    "time": time
}

with open("final_rat_data.json", "w") as f:
    json.dump(final_json, f, indent=2)