.
├── data/                   # Processed & synthetic datasets
│   ├── herd_daily_clean.csv
│   └── device_daily_clean.csv
├── notebooks/              # Jupyter analysis
│   ├── 1_Data_Preprocessing.ipynb
│   ├── 2_EDA.ipynb
│   ├── 3_Time_Series.ipynb
│   └── 4_ML_Modeling.ipynb
├── src/                    # Python modules
│   ├── preprocessing.py   # Data merging/cleaning
│   ├── models.py          # SARIMA/ML implementations
│   └── visualize.py       # Plotting functions
├── results/               # Outputs
│   ├── forecasts/
│   ├── residual_analysis/
│   └── model_performance/
├── requirements.txt       # Dependency list
└── README.md