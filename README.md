# Customer Segmentation Dashboard

An interactive Customer Segmentation Dashboard built using Python and Streamlit. The project uses RFM (Recency, Frequency, Monetary) analysis to categorize customers into different segments and generate business insights.

## 🚀 Live Demo

[View the Customer Segmentation Dashboard](YOUR_STREAMLIT_LINK_HERE)

## 📊 Features

- Customer segmentation using RFM analysis
- Filter customers by City
- Filter customers by Customer Segment
- Key performance indicators:
  - Total Customers
  - High-Value Customers
  - At-Risk Customers
  - Total Revenue
- Customer Segment Distribution visualization
- Revenue analysis by Customer Segment
- Detailed customer information table
- Download filtered customer data
- Recommended actions based on customer segments
- Business insights and customer analytics

## 🧠 Customer Segments

| Segment | Description |
|---|---|
| High-Value Customer | Recent, frequent, and high-spending customers |
| Loyal Customer | Customers who purchase frequently and show consistent engagement |
| At Risk | Customers who have not purchased recently and may be lost |
| New Customer | Customers with relatively recent and limited purchase history |
| Low-Value Customer | Customers with lower purchase frequency and spending |

## 📈 RFM Analysis

RFM analysis is a customer segmentation technique used to understand customer purchasing behavior.

- **Recency (R):** How recently the customer made a purchase.
- **Frequency (F):** How frequently the customer makes purchases.
- **Monetary (M):** How much money the customer spends.

## 🛠️ Technologies Used

- Python
- Pandas
- Streamlit
- Plotly

## 📂 Project Structure

```text
customer-segmentation/
│
├── data/
│   └── customer_data.csv
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore



## ▶️ How to Run Locally

1. Clone the repository

```bash
git clone https://github.com/shreyadolas/customer-segmentation.git
```

2. Navigate to the project folder

```bash
cd customer-segmentation
```

3. Install the required dependencies

```bash
pip install -r requirements.txt
```

4. Run the Streamlit application

```bash
streamlit run app.py
```

## 🔗 Live Application

The application is deployed using Streamlit.

[🚀 Open Customer Segmentation Dashboard](https://shreyadolas-customer-segmentation-app-llnbea.streamlit.app/)

## 👩‍💻 Author

**Shreya Dolas**
