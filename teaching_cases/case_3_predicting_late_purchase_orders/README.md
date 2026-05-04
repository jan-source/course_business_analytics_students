# Predicting Late Purchase Orders

This folder contains the notebooks for the teaching case on predicting late procurement deliveries.

## Notebooks for this Case

- [Starter Notebook](teaching_cases/case_3_predicting_late_purchase_orders/0_step_starting_point.ipynb)
([Open in Colab](https://colab.research.google.com/github/jan-source/course_business_analytics_students/blob/main/teaching_cases/case_3_predicting_late_purchase_orders/0_step_starting_point.ipynb))

- [First Model with 2 Features](teaching_cases/case_3_predicting_late_purchase_orders/1_step_late_procurement_deliveries_two_features.ipynb)
([Open in Colab](https://colab.research.google.com/github/jan-source/course_business_analytics_students/blob/main/teaching_cases/case_3_predicting_late_purchase_orders/1_step_late_procurement_deliveries_two_features.ipynb))

- [Model using several Features](teaching_cases/case_3_predicting_late_purchase_orders/2_step_late_procurement_deliveries_all_features.ipynb)
([Open in Colab](https://colab.research.google.com/github/jan-source/course_business_analytics_students/blob/main/teaching_cases/case_3_predicting_late_purchase_orders/2_step_late_procurement_deliveries_all_features.ipynb))

- [Model interpretation with SHAP](teaching_cases/case_3_predicting_late_purchase_orders/3_step_late_procurement_deliveries_explainable_ai.ipynb)
([Open in Colab](https://colab.research.google.com/github/jan-source/course_business_analytics_students/blob/main/teaching_cases/case_3_predicting_late_purchase_orders/3_step_late_procurement_deliveries_explainable_ai.ipynb))

- [Notebook Course Day 5 Starting Point](teaching_cases/case_3_predicting_late_purchase_orders/4_starting_point_5_course_day.ipynb)
([Open in Colab](https://colab.research.google.com/github/jan-source/course_business_analytics_students/blob/main/teaching_cases/case_3_predicting_late_purchase_orders/4_starting_point_5_course_day.ipynb))

- [Notebook Course Day 5 Final](teaching_cases/case_3_predicting_late_purchase_orders/5_complete_notebook_5_course_day.ipynb)
([Open in Colab](https://colab.research.google.com/github/jan-source/course_business_analytics_students/blob/main/teaching_cases/case_3_predicting_late_purchase_orders/5_complete_notebook_5_course_day.ipynb))

- [Notebook Course Day 6 Explainable AI](teaching_cases/case_3_predicting_late_purchase_orders/6_complete_notebook_6_course_day_explainable_ai.ipynb)
([Open in Colab](https://colab.research.google.com/github/jan-source/course_business_analytics_students/blob/main/teaching_cases/case_3_predicting_late_purchase_orders/6_complete_notebook_6_course_day_explainable_ai.ipynb))


## Local Setup with the Project Virtual Environment <span style="color:red">(can be skipped if Anaconda was used for installing Python)</style>

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

