Procurement Analytics & Cost Control Dashboard (KSA)

    Project Overview

        This project simulates an enterprise procurement analytics dashboard for a Saudi Arabia–based oil & gas–related organization.
        The goal is to provide decision-ready insights for Procurement, Cost Control, and Operations leadership by analyzing spend, budget utilization, cycle times, and supplier performance.
        The dashboard is built using Power BI with Python-generated ERP-style transactional data, reflecting realistic procurement workflows (PR → PO → Delivery).

    Business Problem

        Procurement leadership needs visibility into:
        Whether spending is aligned with budget
        How efficient the procurement process is (cycle times)
        Which departments and suppliers drive cost and delays
        Where cost leakage and supplier risks exist
        This dashboard answers those questions at executive, operational, and supplier levels.

    Target Users

        Procurement Managers
        Cost Control & Finance Teams
        Operations & Plant Management
        BI / Data Analytics Teams

    Key KPIs

        Total Spend
        Total Budget
        Budget Utilization %
        Avg PR → PO Cycle Time (Days)
        Avg PO → Delivery Lead Time (Days)
        On-time Delivery %
        Late Delivery %
        Price Variance Amount & %
        Top 5 Supplier Spend %
        All KPIs are calculated as DAX measures using a star-schema data model.

Dashboard Pages
    1-Executive Overview

        High-level view for leadership:
            Budget utilization and spend control
            Monthly spend vs budget trend
            Spend distribution by department
            Key insights summary

        Key Insight Example:
            Overall budget utilization reached ~104%, driven primarily by Plant and Operations activities in Q4.

    2-Procurement Efficiency

        Operational performance view:
            PR → PO and PO → Delivery cycle time trends
            Department-level efficiency comparison
            Late delivery analysis
            Detailed matrix for drill-down

    3-Supplier & Cost Control

        Risk and cost leakage view:
            Price variance % by category
            Top suppliers by spend
            Supplier performance scorecard
            Interactive tooltip for supplier KPIs

Data Model

    Fact tables: Purchase Requisitions, Purchase Orders, Deliveries, Budget
    Dimension tables: Date, Month, Department, Supplier 
    Separate handling of daily transactional dates and monthly budget periods

    Advanced DAX using:
        TREATAS
        USERELATIONSHIP
        Context-aware measures
        This ensures correct monthly analysis despite mixed date grains.

Tools & Technologies

    Power BI Desktop
    Python (data generation & simulation)
    DAX
    GitHub
    CSV datasets

Files:
    /data
    └─ CSV files (generated transactional data)
    /powerbi
    └─ procurement_analytics_ksa.pbix
    /screenshots
    └─ Executive Overview
    └─ Procurement Efficiency
    └─ Supplier & Cost Control
    /docs
    └─ PDF export of dashboard