# 📘 Supplier Risk Scoring System  
### *KPI Normalization • Weighted Risk Scoring • Streamlit Dashboard*

A fully transparent and replicable system for evaluating supplier performance and risk.  
This project aggregates PO-level KPIs, normalizes them using global Min–Max scaling, computes a weighted composite risk score, and visualizes everything using an interactive **Streamlit dashboard**.

---

## 🚀 Features

- ✔ Aggregates PO-level data into supplier KPIs  
- ✔ Normalizes KPIs globally using Min–Max  
- ✔ Computes composite weighted supplier risk score  
- ✔ Manual weight inputs (not sliders)  
- ✔ Supplier engagement level included  
- ✔ Sorted bar chart and risk distribution pie chart  
- ✔ Exports clean Excel output  
- ✔ Fully reproducible by hand (all formulas provided)

---

## 📁 Repository Structure

riskscoringsystem.ipynb → Main notebook
Supplier_KPI_Normalized_Final.xlsx → Output KPI file
app.py → Streamlit dashboard
README.md → Project documentation


---

## 📊 KPIs Used

| KPI | Description |
|-----|-------------|
| `LDR` | Late Delivery Rate |
| `NRR` | Not Received Rate |
| `AD` | Weighted Average Delay (days) |
| `Avg_Lead_Time` | Average supplier lead time |
| `Total_Line_Value` | Financial exposure with the supplier |
| `VSL_Risk` | Risk level derived from SL ID (10 or 20) |
| `Supplier_Engagement_Level` | Frequency-based supplier grouping |

---

## 🔢 KPI Normalization (Global Min–Max Scaling)

All KPIs are scaled to 0–1 using:

\[
\text{Normalized} = \frac{x - x_{\min}}{x_{\max} - x_{\min}}
\]

Normalized columns created:

- `LDR_norm`
- `NRR_norm`
- `AD_norm`
- `LTR_norm`
- `FE_norm`
- `VSL_Risk_norm`

The final Excel file also includes all **global min/max values** used, so anyone can replicate calculations manually.

---

## 🧮 Composite Risk Score

Users can define custom weights (must sum to 1):

Risk Score =
(LDR_norm * w_LDR) +
(NRR_norm * w_NRR) +
(AD_norm * w_AD) +
(LTR_norm * w_LTR) +
(FE_norm * w_FE) +
(VSL_Risk_norm * w_VSL)


These weights are entered directly in the Streamlit dashboard.

---

## 🚦 Risk Category Labels

| Score Range | Category |
|-------------|----------|
| **0.00 – 0.33** | 🟢 Low Risk |
| **0.34 – 0.66** | 🟡 Moderate Risk |
| **0.67 – 1.00** | 🔴 High Risk |

The dashboard calculates and displays these labels automatically.

---

## 🖥️ Streamlit Dashboard (`app.py`)

Run the dashboard with:

python -m streamlit run app.py
- Install dependencies: pip install pandas numpy streamlit openpyxl

# Dashboard capabilities

# Reads Supplier_KPI_Normalized_Final.xlsx
- Lets users enter weights manually
- Recalculates composite risk score instantly

# Displays:
- Supplier table (Supplier, Engagement Level, Risk Score, Category)
- Works with no need to upload files — the XLSX is read directly.

- 
