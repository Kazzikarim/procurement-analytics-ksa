Title: Procurement & Cost Control Analytics – KSA Oil & Gas (Simulated ERP Data)

I am building a Power BI dashboard that shows procurement delays, supplier performance, and cost leakage using ERP-style tables.

Audience: Procurement Manager / Cost Control Managers

Business problem:
Procurement leadership lacks consolidated visibility into purchasing cycle delays, supplier reliability, and cost leakage across departments, causing budget overruns and operational delays.

KPIs included:
PR to PO cycle time
    What it answers:
    Are approvals and sourcing slow?

    Calculation logic:
    PO_Date – PR_Date

    Decision impact:

    Identify bottlenecks by department

    Escalate approval delays
On-time delivery %
    What it answers:
    Are suppliers delivering late?

    Calculation logic:
    Actual_Delivery_Date – PO_Date

    Decision impact:

    Penalize poor suppliers

    Adjust lead times
Price variance % vs contract
    What it answers:
    Are we paying more than contracted prices?

    Calculation logic:
    (PO_Amount – Contract_Price) / Contract_Price

    Decision impact:

    Detect maverick buying

    Trigger contract renegotiation
Spend by category & department
    What it answers:
    Are departments overspending?

    Calculation logic:
    Actual Spend – Budget

    Decision impact:

    Budget freezes

    Reforecasting
Supplier concentration risk
    What it answers:
    Are we over-dependent on few suppliers?

    Calculation logic:
    Top 5 supplier spend / total spend

    Decision impact:

    Risk mitigation

    Diversification strategy

Tools: Power BI, Excel, SQL (optional)

Files:
/data: CSV tables
/powerbi: PBIX file
/screenshots: dashboard images
/sql: queries for KPI calculations