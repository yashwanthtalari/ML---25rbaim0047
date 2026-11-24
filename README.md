# Student Marks Predictor
### Simple Linear Regression Based Prediction System

A lightweight, production-grade Machine Learning web application built using **Streamlit** and **Scikit-learn** that predicts examination marks based on daily study hours using a Simple Linear Regression model.

---

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Application
```bash
streamlit run app.py
```

The web dashboard will open in your default browser at `http://localhost:8501`.

---

## 📊 Dataset & Model Details

### Dataset
| Study Hours (X) | Examination Marks (Y) |
|:---:|:---:|
| 1 | 35 |
| 2 | 40 |
| 3 | 45 |
| 4 | 50 |
| 5 | 55 |
| 6 | 60 |
| 7 | 65 |
| 8 | 70 |
| 9 | 75 |
| 10 | 80 |

### Fitted Regression Equation
$$Y = mX + c$$
$$\text{Marks} = (5.00 \times \text{Study Hours}) + 30.00$$

- **Algorithm:** Ordinary Least Squares (Simple Linear Regression)
- **Slope ($m$ / Coefficient):** `+5.00` marks per additional study hour
- **Intercept ($c$):** `30.00` marks
- **Coefficient of Determination ($R^2$):** `1.000` (100% variance explained)

---

## 🎯 Features

1. **Interactive Controls:**
   - Study hours slider (0.0 to 16.0 hours, step 0.5)
   - Quick preset buttons (2.0 hrs, 5.0 hrs, 8.0 hrs, 10.0 hrs)
   - Real-time "Predict Marks" trigger button
2. **Prediction Cards:**
   - Dynamic predicted examination marks
   - Categorized performance rating (Distinction, First Class, Second Class, Pass, Needs Improvement)
   - Live $R^2$ score and regression coefficient ($m$)
3. **Data Visualization:**
   - Scatter plot of original training points
   - Clean continuous linear regression line
   - Highlighted user prediction marker with coordinate callout and dashed projection drop-lines
4. **Interactive Dataset Table:**
   - Formatted table of training data, fitted predictions ($\hat{Y}$), and residual errors ($e$)

