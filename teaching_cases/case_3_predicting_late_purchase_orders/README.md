# Predicting Late Purchase Orders

This folder contains the notebooks for the teaching case on predicting late procurement deliveries.

## Notebooks

- `0_step_starting_point.ipynb`: starter notebook for students
- `1_step_late_procurement_deliveries_two_features.ipynb`: first model with two features
- `2_step_late_procurement_deliveries_all_features.ipynb`: model using all available features
- `3_step_late_procurement_deliveries_explainable_ai.ipynb`: model interpretation with SHAP

## Local Setup with the Project Virtual Environment

Run the following commands from the repository root.

### 1. Activate the virtual environment

On macOS or Linux:

```bash
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 2. Install JupyterLab and the notebook kernel

```bash
uv pip install jupyterlab ipykernel
```

### 3. Register the current environment as a Jupyter kernel

```bash
python -m ipykernel install --user --name course-business-analytics --display-name "Python (course_business_analytics_students)"
```

### 4. Start JupyterLab

```bash
jupyter lab
```

### 5. Select the correct kernel inside the notebook

In JupyterLab or VS Code, choose the kernel named `Python (course_business_analytics_students)`.

## Running in Google Colab

The notebooks use files hosted from GitHub, so they can also run in Colab.

If a notebook needs additional packages, install them in the first cell, for example:

```python
!pip install shap -q
```

For SHAP visualizations in Colab, call `shap.initjs()` right after `import shap`.

## Troubleshooting

If your environment does not appear in the kernel list, run the kernel registration command again:

```bash
python -m ipykernel install --user --name course-business-analytics --display-name "Python (course_business_analytics_students)"
```

If `jupyter lab` starts with the wrong Python, make sure the virtual environment is activated before launching it.

