# 🚖 YourCabs - Cab Cancellation Prediction

This project predicts whether a cab booking will be canceled based on various features such as booking time, source and destination areas, travel type, and more. It includes detailed exploratory data analysis (EDA), feature engineering, and multiple machine learning models to improve prediction accuracy.

---

## 📌 Problem Statement

Cab service providers like **YourCabs** face operational issues due to last-minute cancellations. Predicting such cancellations in advance helps reduce costs and improve user experience.

---

## 📊 Exploratory Data Analysis (EDA)

- **Data Shape:** 43,431 rows × 18 columns
- **Missing Value Analysis:** Significant nulls in `to_area_id`, `to_city_id`, and `package_id`
- **Datetime Parsing:** Extracted dates and time-based features (day, month, session, weekday/weekend)
- **Categorical Encoding:** Travel type, online/mobile booking, etc.
- **Geospatial Analysis:** Calculated distance using Haversine formula from lat-long coordinates
- **Imbalance Check:** Class imbalance observed in target variable `Car_Cancellation`
- **Outlier and Distribution Checks:** Visualizations using seaborn and matplotlib

---

## 🧠 Feature Engineering

- `time_diff`: Time difference between booking and trip start (in minutes)
- `from_date_session` and `booking_created_session`: Categorized time into sessions like Morning, Evening, etc.
- `distance`: Haversine distance between source and destination
- Encoded `travel_type_id` as `point_to_point` and `hourly`
- Labeled `from_area_id` into cancellation risk buckets (Low, Medium, High)

---

## ⚙️ Models Used

| Model                 | Accuracy | Precision | Recall | F1 Score |
|----------------------|----------|-----------|--------|----------|
| Logistic Regression  | 92.84%   | 0.00      | 0.00   | 0.00     |
| Decision Tree        | 91.3%    | (Your result here) | ... | ... |
| Random Forest        | 92.85%   | 0.00      | 0.00   | 0.00     |

> ❗ Note: Metrics indicate class imbalance. Most models struggle to predict class `1` (cancellation). Next steps include SMOTE or using `class_weight='balanced'`.

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/yourcab-cancellation-predictor.git
cd yourcab-cancellation-predictor
pip install -r requirements.txt

