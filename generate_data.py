import random
from datetime import date, timedelta
import pandas as pd

random.seed(42)

START = date(2025, 1, 1)
END = date(2025, 12, 31)
DAYS = (END - START).days + 1

departments = ["Procurement", "Maintenance", "Operations", "Plant", "HR", "Finance"]
categories = ["MRO", "Safety", "IT", "Logistics", "Capex", "Services", "Facilities", "Training"]

suppliers_local = [f"Supplier SA {i:02d}" for i in range(1, 13)]
suppliers_intl = [f"Supplier INTL {i:02d}" for i in range(1, 9)]
suppliers = suppliers_local + suppliers_intl

countries_intl = ["UAE", "USA", "Germany", "China", "India", "UK"]
supplier_rows = []
for s in suppliers_local:
    supplier_rows.append({"Supplier": s, "Supplier_Type": "Local", "Country": "Saudi Arabia"})
for i, s in enumerate(suppliers_intl):
    supplier_rows.append({"Supplier": s, "Supplier_Type": "International", "Country": countries_intl[i % len(countries_intl)]})
df_suppliers = pd.DataFrame(supplier_rows)

def rand_date():
    return START + timedelta(days=random.randint(0, DAYS - 1))

def category_lead_time(cat: str) -> int:
    if cat == "Capex":
        return random.randint(20, 45)
    if cat in ("Logistics", "Services"):
        return random.randint(14, 35)
    if cat in ("MRO", "Safety", "Facilities"):
        return random.randint(7, 25)
    return random.randint(10, 30)

def pr_to_po_days():
    return random.randint(3, 18)

def price_variance_pct():
    r = random.random()
    if r < 0.08:
        return random.uniform(0.08, 0.15)   # bad leakage
    if r < 0.20:
        return random.uniform(-0.05, -0.01) # good negotiation
    return random.uniform(0.00, 0.04)       # normal

N_PR = 1000
prs = []
for i in range(1, N_PR + 1):
    pr_date = rand_date()
    dept = random.choice(departments)
    cat = random.choice(categories)
    est = round(random.uniform(5_000, 250_000), 2)
    prs.append({
        "PR_ID": f"PR-{i:05d}",
        "PR_Date": pr_date.isoformat(),
        "Department": dept,
        "Category": cat,
        "Estimated_Amount": est
    })
df_pr = pd.DataFrame(prs)

# POs: 80% of PRs
pos = []
po_id = 1
for _, pr in df_pr.sample(frac=0.80, random_state=42).iterrows():
    pr_date = date.fromisoformat(pr["PR_Date"])
    po_date = pr_date + timedelta(days=pr_to_po_days())
    supplier = random.choice(suppliers)
    # PO amount around estimate with some noise
    po_amount = float(pr["Estimated_Amount"]) * random.uniform(0.85, 1.20)
    po_amount = round(po_amount, 2)

    var = price_variance_pct()
    contract_price = po_amount / (1 + var)
    contract_price = round(contract_price, 2)

    due = po_date + timedelta(days=category_lead_time(pr["Category"]))

    pos.append({
        "PO_ID": f"PO-{po_id:05d}",
        "PR_ID": pr["PR_ID"],
        "PO_Date": po_date.isoformat(),
        "Supplier": supplier,
        "PO_Amount": po_amount,
        "Contract_Price": contract_price,
        "Delivery_Due_Date": due.isoformat()
    })
    po_id += 1
df_po = pd.DataFrame(pos)

# Deliveries: 93% of POs
deliveries = []
del_id = 1
for _, po in df_po.sample(frac=0.93, random_state=7).iterrows():
    po_date = date.fromisoformat(po["PO_Date"])
    due = date.fromisoformat(po["Delivery_Due_Date"])
    supplier = po["Supplier"]
    is_intl = supplier.startswith("Supplier INTL")

    # Late rate: ~18% local, ~26% intl
    late_chance = 0.26 if is_intl else 0.18
    partial_chance = 0.06

    r = random.random()
    if r < 0.02:
        status = "Cancelled"
        actual = None
    elif r < 0.02 + partial_chance:
        status = "Partial"
        # partial often late by a bit
        actual = due + timedelta(days=random.randint(1, 10))
    else:
        if random.random() < late_chance:
            status = "Late"
            actual = due + timedelta(days=random.randint(1, 14))
        else:
            status = "Delivered"
            # can be early/on-time
            actual = due - timedelta(days=random.randint(0, 3))

    deliveries.append({
        "Delivery_ID": f"DEL-{del_id:05d}",
        "PO_ID": po["PO_ID"],
        "Actual_Delivery_Date": "" if actual is None else actual.isoformat(),
        "Delivery_Status": status
    })
    del_id += 1
df_del = pd.DataFrame(deliveries)

# Budget: monthly by department
budgets = []
for dept in departments:
    base = {
        "Procurement": 1_200_000,
        "Maintenance": 1_500_000,
        "Operations": 2_000_000,
        "Plant": 2_500_000,
        "HR": 600_000,
        "Finance": 500_000
    }[dept]
    for m in range(1, 13):
        month_date = date(2025, m, 1)
        bump = 1.10 if (dept in ("Plant", "Operations") and m in (10, 11, 12)) else 1.0
        noise = random.uniform(0.95, 1.05)
        amt = round(base * bump * noise, 2)
        budgets.append({"Department": dept, "Month": month_date.isoformat(), "Budget_Amount": amt})
df_budget = pd.DataFrame(budgets)

# Write to your existing /data folder
df_pr.to_csv("data/purchase_requisitions.csv", index=False)
df_po.to_csv("data/purchase_orders.csv", index=False)
df_del.to_csv("data/deliveries.csv", index=False)
df_suppliers.to_csv("data/suppliers.csv", index=False)
df_budget.to_csv("data/budget.csv", index=False)

print("Done. Generated CSVs in /data")
