# Data Science Example

This repository is an explorable example of how a data science project can be
organized and shared on GitHub. It includes sample data, a notebook, reusable
Python code, tests, project documentation, and a GitHub Actions workflow.

The analysis is intentionally simple. The main subject is the repository:
where different parts of a data science project live, how they connect, and
how GitHub can support the work.

## What to explore

- How sample data and its documentation are stored in `data/`
- How exploratory work is shown in `notebooks/`
- How reusable analysis code is separated into `src/`
- How tests in `tests/` check data and transformations
- How dependencies are listed in `requirements.txt`
- How GitHub Actions runs the tests automatically
- How the README helps someone else understand and use the project

The data is synthetic. It is included to make the repository structure
concrete, not to teach customer analytics or support real conclusions.

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

## Explore the repository

1. Browse the repository on GitHub and identify the role of each top-level
   folder.
2. Read `data/README.md` and inspect the sample CSV files.
3. Open `notebooks/01_exploration.ipynb` to see how an analysis can be
   documented alongside its output.
4. Compare the notebook with the reusable code in `src/`.
5. Open `tests/test_transformations.py` and `.github/workflows/ci.yml` to see
   how checks are written and run.
6. Use the repository history, branches, pull requests, and Actions checks to
   explore how GitHub supports collaboration around the project.

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

## Run the project locally

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

## Ideas for exploring GitHub for data science

- Create a branch and update the notebook or sample data documentation.
- Open a pull request and review the changed files.
- Add a test for a change and confirm that the Actions workflow runs it.
- Use an issue to describe a possible analysis or repository improvement.
- Compare notebook-only code with code that can be reused from `src/`.
- Inspect the commit history to see how project changes are recorded.

## Important limitations

- The CSV files contain synthetic data created only for this project.
- The analysis is intentionally simple and is not a complete data science or
  machine learning project.
- The results are examples for demonstrating repository organization, not
  evidence about real customers or markets.
