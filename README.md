# Data Science Example

This repository is a small practice project for learning how a data science
workflow fits together. You will work with synthetic customer and order data,
explore it in a notebook, turn repeated analysis into Python functions, and
run tests to check that the results still make sense.

The project is intentionally small, so you can focus on the workflow instead
of spending time cleaning a large or unfamiliar dataset.

## What you will practice

- Loading related CSV files with pandas
- Joining customer and order data
- Exploring data in a Jupyter notebook
- Creating customer-level summary features
- Grouping customers into simple revenue bands
- Writing reusable Python code outside the notebook
- Using tests to check data and transformation results

The data is made up for practice. It is not a real customer dataset and should
not be used for business decisions or model training.

## Repository structure

```text
.
├── README.md
├── data/
│   ├── README.md              # Notes about the sample data
│   └── sample/                # Synthetic customer and order CSV files
├── notebooks/
│   └── 01_exploration.ipynb   # Guided first look at the data
├── src/
│   ├── data_loader.py         # Loads and joins the CSV files
│   ├── feature_engineering.py # Builds customer summary features
│   └── modeling.py            # Produces a small scorecard
├── tests/
│   └── test_transformations.py
├── requirements.txt
├── pytest.ini
└── .github/workflows/ci.yml   # Runs the tests on GitHub
```

## Start here

1. Read `data/README.md` to understand the columns and limitations of the
   sample data.
2. Open `notebooks/01_exploration.ipynb` and run the cells. Look at the
   customer and order tables, then inspect the merged data.
3. Read `src/data_loader.py` to see how the tables are loaded and joined.
4. Read `src/feature_engineering.py` to see how order-level rows become one
   summary row per customer.
5. Run the tests and then try changing the analysis yourself.

## Set up the project

Create a virtual environment so the project packages stay separate from your
other Python projects:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

## Run the examples

```bash
python src/data_loader.py
python src/feature_engineering.py
python src/modeling.py
pytest -q
```

To open the notebook:

```bash
jupyter notebook
```

Then open `notebooks/01_exploration.ipynb` in the browser window.

## Ideas for practice

- Add a chart showing revenue by region or product category.
- Compare repeat and non-repeat purchases.
- Change the revenue-band thresholds and explain the effect.
- Add a new customer metric, such as days since signup.
- Write a test for the new metric.
- Replace the notebook's data-loading code with
  `src.data_loader.load_demo_data`.

## Important limitations

- The CSV files contain synthetic data created only for this project.
- The analysis is intentionally simple and is not a complete machine learning
  project.
- The results are examples for learning, not evidence about real customers or
  markets.
