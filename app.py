import streamlit as st
import pandas as pd



st.set_page_config(
    page_title="Customer Segmentation Dashboard",
    page_icon="📊",
    layout="wide"
)


# Load the customer transaction data
df = pd.read_csv("data/customer_transactions.csv")


# Convert Purchase_Date to datetime
df["Purchase_Date"] = pd.to_datetime(df["Purchase_Date"])



# Create a reference date
reference_date = df["Purchase_Date"].max() + pd.Timedelta(days=1)

# Calculate RFM metrics for each customer
rfm = df.groupby("Customer_ID").agg(
    Recency=("Purchase_Date", lambda x: (reference_date - x.max()).days),
    Frequency=("Customer_ID", "count"),
    Monetary=("Amount", "sum")
).reset_index()


# Create RFM scores from 1 to 5

rfm["R_Score"] = pd.qcut(
    rfm["Recency"],
    5,
    labels=[5, 4, 3, 2, 1]
)

rfm["F_Score"] = pd.qcut(
    rfm["Frequency"].rank(method="first"),
    5,
    labels=[1, 2, 3, 4, 5]
)

rfm["M_Score"] = pd.qcut(
    rfm["Monetary"].rank(method="first"),
    5,
    labels=[1, 2, 3, 4, 5]
)


# Create customer segments

def segment_customer(row):
    r = int(row["R_Score"])
    f = int(row["F_Score"])
    m = int(row["M_Score"])

    if r >= 4 and f >= 4 and m >= 4:
        return "High-Value Customer"

    elif r >= 4 and f >= 4:
        return "Loyal Customer"

    elif r <= 2 and f >= 3:
        return "At Risk"

    elif r >= 4 and f <= 2:
        return "New Customer"

    else:
        return "Low-Value Customer"


rfm["Segment"] = rfm.apply(segment_customer, axis=1)



# Count customers in each segment

segment_counts = rfm["Segment"].value_counts()



st.title("Customer Segmentation Dashboard")
st.write("Customer segmentation analysis based on RFM.")


city = st.selectbox(
    "Select City",
    ["All Cities"] + sorted(df["City"].unique().tolist())
)

if city != "All Cities":
    filtered_df = df[df["City"] == city]
    city_customers = filtered_df["Customer_ID"].unique()
    filtered_rfm = rfm[rfm["Customer_ID"].isin(city_customers)]
else:
    filtered_df = df
    filtered_rfm = rfm

segment = st.selectbox(
    "Select Segment",
    ["All Segments"] + sorted(filtered_rfm["Segment"].unique().tolist())
)

if segment != "All Segments":
    filtered_rfm = filtered_rfm[filtered_rfm["Segment"] == segment]


segment_counts = filtered_rfm["Segment"].value_counts()

segment_revenue = filtered_rfm.groupby("Segment")["Monetary"].sum()



col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Customers", len(filtered_rfm))
col2.metric("High-Value Customers", (filtered_rfm["Segment"] == "High-Value Customer").sum())
col3.metric("At-Risk Customers", (filtered_rfm["Segment"] == "At Risk").sum())
col4.metric("Total Revenue", f"₹{filtered_df[filtered_df['Customer_ID'].isin(filtered_rfm['Customer_ID'])]['Amount'].sum():,.0f}")


st.subheader("Customer Segments")

st.write(segment_counts)


st.subheader("Customer Segment Distribution")

st.bar_chart(segment_counts)

st.subheader("Revenue by Customer Segment")

st.bar_chart(segment_revenue)

st.divider()

st.subheader("Customer Details")

customer_details = filtered_rfm[
    ["Customer_ID", "Recency", "Frequency", "Monetary",
     "R_Score", "F_Score", "M_Score", "Segment"]
]

customer_details = customer_details.sort_values(
    "Monetary",
    ascending=False
)

st.dataframe(customer_details, width="stretch")

csv = customer_details.to_csv(index=False)

st.download_button(
    "Download Customer Details",
    csv,
    "customer_details.csv",
    "text/csv"
)

st.divider()

st.subheader("Recommended Action")

if segment == "At Risk":
    st.warning("Focus on retention campaigns, personalized offers, and re-engagement.")
elif segment == "High-Value Customer":
    st.success("Reward these customers with VIP offers and loyalty benefits.")
elif segment == "Loyal Customer":
    st.info("Maintain engagement with loyalty rewards and exclusive offers.")
elif segment == "New Customer":
    st.info("Encourage repeat purchases with welcome offers and product recommendations.")
elif segment == "Low-Value Customer":
    st.write("Use targeted promotions to increase purchase frequency and spending.")
else:
    st.write("Select a customer segment to see recommended actions.")


st.divider()

st.subheader("Business Insights")

total_customers = len(filtered_rfm)

total_revenue = filtered_df[
    filtered_df["Customer_ID"].isin(filtered_rfm["Customer_ID"])
]["Amount"].sum()

if total_customers > 0:
    avg_revenue = total_revenue / total_customers

    st.write(f"• Total customers: {total_customers}")
    st.write(f"• Total revenue: ₹{total_revenue:,.2f}")
    st.write(f"• Average revenue per customer: ₹{avg_revenue:,.2f}")

    at_risk_count = (filtered_rfm["Segment"] == "At Risk").sum()
    at_risk_percentage = (at_risk_count / total_customers) * 100

    st.write(
        f"• At-Risk customers: {at_risk_percentage:.1f}% "
        f"of selected customers."
    )


st.divider()

st.subheader("About RFM Analysis")

st.write("""
RFM analysis is a customer segmentation technique used to understand
customer purchasing behavior.

• Recency (R): How recently the customer made a purchase.
Lower recency means the customer purchased more recently.

• Frequency (F): How frequently the customer made purchases.
Higher frequency indicates stronger customer engagement.

• Monetary (M): How much money the customer spent.
Higher monetary value indicates higher customer value.
""")

st.subheader("Customer Segments")

st.write("""
• High-Value Customer → Recent, frequent, and high-spending customers.

• Loyal Customer → Customers who purchase frequently and show consistent engagement.

• At Risk → Customers who have not purchased recently and may be lost.

• New Customer → Customers with relatively recent and limited purchase history.

• Low-Value Customer → Customers with lower purchase frequency and spending.
""")