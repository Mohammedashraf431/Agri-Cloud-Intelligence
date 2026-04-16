# 🌾 Cloud Cost Intelligence Platform for Agriculture
**Specialization:** AI & Cloud Computing  
**Developer:** AK  
**Tech Stack:** Python 3.12, Pandas, Matplotlib, Openpyxl

## 📌 Project Overview
This platform is designed to help agricultural stakeholders (farmers and researchers) monitor, predict, and optimize their cloud expenditures. It transforms raw usage data from IoT sensors and drone surveys into actionable business intelligence.

## 🚀 Key Features
- **Data Persistence:** Automated Excel-based storage for offline access.
- **Anomaly Detection:** Identifies "High Cost" resources using mean-threshold logic.
- **AI Forecasting:** Uses current burn rates to predict 30-day budget outlooks.
- **Multi-Cloud Comparison:** Visualizes potential savings by comparing different cloud providers.

## 📊 Visual Intelligence
The system automatically generates two key reports:
1. `cost_analysis_chart.png`: Distribution of current resource costs.
2. `cloud_comparison.png`: Comparison between current and optimized cloud strategies.

## ⚙️ How to Run
1. Activate the environment: `.\venv\Scripts\activate`
2. Open `agriculture_analysis.ipynb` in VS Code.
3. Run all cells to generate the latest reports and Excel database.