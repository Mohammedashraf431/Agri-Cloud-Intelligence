import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Agri-Cloud AI Intelligence", layout="wide")
st.title("🌾 Agriculture Cloud Cost Intelligence Dashboard")
st.markdown("Developed by **AK** | BCA AI & Cloud Computing")

# 1. Load the Big Data
@st.cache_data
def load_data():
    return pd.read_excel('agriculture_cloud_big_data.xlsx')

df = load_data()

# 2. THE INTELLIGENCE LAYER: Anomaly Detection
# Find items that are 1.5x higher than the average cost
avg_cost = df['Cost_INR'].mean()
anomalies = df[df['Cost_INR'] > (avg_cost * 1.5)]

# 3. TOP METRICS
col1, col2, col3 = st.columns(3)
col1.metric("Total Spending", f"{df['Cost_INR'].sum():,.2f} INR")
col2.metric("Avg. Resource Cost", f"{avg_cost:.2f} INR")
col3.metric("🚨 Anomalies Detected", len(anomalies))

st.divider()

# 4. THE RECOMMENDATION SYSTEM (Your past work!)
st.subheader("🤖 AI Optimization Recommendations")
if not anomalies.empty:
    highest_item = anomalies.sort_values(by='Cost_INR', ascending=False).iloc[0]
    
    st.warning(f"**High Cost Detected:** {highest_item['Resource']} reached {highest_item['Cost_INR']} INR on {highest_item['Date']}.")
    
    # Custom Recommendations based on your logic
    recs = {
        'Drone Crop Survey': "Switch to 'Spot Instances' on Azure/AWS to save 60% on compute-heavy imaging.",
        'Irrigation AI Control': "Schedule sensor pings to 'Off-Peak' hours to reduce API call costs.",
        'Harvesting Automation': "Move to a Reserved Instance pricing model for 24/7 harvesting operations.",
        'Soil Sensors (IoT)': "Implement Data Compression to reduce Cloud Storage egress fees."
    }
    
    current_rec = recs.get(highest_item['Resource'], "Review resource scaling limits to prevent budget leaks.")
    st.success(f"**Recommendation:** {current_rec}")
else:
    st.success("✅ All systems operating within budget. No action required.")

# 5. VISUAL ANALYTICS
st.subheader("📊 Statistical Cost Distribution")
fig, ax = plt.subplots(figsize=(10, 4))
sns.boxplot(x='Cost_INR', y='Resource', data=df, palette='viridis', ax=ax)
plt.axvline(avg_cost, color='red', linestyle='--', label='Mean Cost')
st.pyplot(fig)

# 6. SHOW THE ANOMALIES TABLE
st.subheader("🔍 Detailed Anomaly Log")
st.table(anomalies.sort_values(by='Cost_INR', ascending=False).head(10))