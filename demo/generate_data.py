"""
Generates the Furniture & Office Performance dummy dataset for the hayaData 2026 demo.

Grain: one row per (Month x Region x Product). 9 months (Jan-Sep 2026) x 4 regions x
~20 products (5 categories x 3-6 products) = ~720 rows.

Story baked into the numbers:
  - Every product has a baseline unit price and unit cost (-> baseline margin %).
  - Every region applies a standard, region-specific discount off list price:
      Central -3%, East -10%, West -5%, South -7%.
  - Central is the smallest region by total sales (REGION_SIZE_FACTOR below) — the
    anomaly is a margin story, not a scale story.
  - Every region/month has a small independent profit-ratio wobble (MARGIN_NOISE
    below) so the trend line has natural month-to-month noise instead of a flat rail.
  - Central's profit RATIO (profit / sales) drops sharply in September 2026 — every
    other region (and every other month) stays in its normal, noisy band.
  - The September dip is caused by a MIX SHIFT, not a demand shift: two specific
    low-margin Central products (Task Chair Basic in Seating, Storage Cart in
    Storage) sell at ~8x their normal volume that month. The offsetting trim is
    mostly CONTAINED to each product's own category (see ANOMALY_BOOST_MULT below
    for the full mechanics) — Desks/Tables/Lighting stay in their normal band,
    Central's TOTAL still looks like a normal month, and Seating/Storage's own
    TOTALS move only modestly. There's a deliberate, load-bearing trade-off here:
    Seating and Storage DO show a real ratio dip if you filter to them directly —
    a category is only 7-8 products, so one of them selling 8x doesn't fully
    disappear in the blended average. A strong Region-level signal and a
    perfectly invisible Category-level signal aren't simultaneously achievable
    with 2 products in small categories and a flat-sales constraint; this is the
    practical middle ground. Only filtering all the way down to the Product
    itself makes the cause unambiguous (an 8-9x sales-volume spike).

Output:
  - furniture_office_data.xlsx  (raw row-level data, one sheet)
  - data.js                      (same rows as a JS array literal, for the dashboard)
"""
import json
import random

import pandas as pd

random.seed(42)

MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
REGIONS = ['Central', 'East', 'South', 'West']
REGION_DISCOUNT = {'Central': 0.03, 'East': 0.10, 'South': 0.07, 'West': 0.05}
ANOMALY_REGION = 'Central'
ANOMALY_MONTH = 'Sep'

# Central is the smallest region; East is the largest. Applied on top of REGION_GROWTH.
REGION_SIZE_FACTOR = {'Central': 0.55, 'East': 1.15, 'South': 0.95, 'West': 1.05}

# 5 categories x 3-6 products each, with a baseline unit price/cost (-> margin).
CATALOG = {
    'Seating': [
        ('Task Chair Basic', 89, 68),     # low margin ~24% — one of the two anomaly drivers
        ('Ergo Task Chair', 249, 152),
        ('Executive Chair', 399, 231),
        ('Guest Chair', 129, 84),
        ('Stacking Chair', 69, 47),
        ('Drafting Stool', 149, 97),
        ('Kneeling Chair', 179, 112),
    ],
    'Desks': [
        ('Straight Desk 120cm', 219, 140),
        ('Sit-Stand Desk', 549, 349),
        ('L-Shape Desk', 459, 289),
        ('Standing Desk Converter', 179, 117),
    ],
    'Storage': [
        ('2-Drawer Pedestal', 99, 66),
        ('Storage Cart', 59, 45),          # low margin ~24% — the other anomaly driver
        ('Lateral Filing Cabinet', 289, 187),
        ('Bookcase 5-Shelf', 159, 101),
        ('Locker Unit', 219, 142),
        ('Mobile Caddy', 79, 55),
        ('Shelving Unit', 249, 159),
        ('Under-Desk Drawer', 69, 48),
    ],
    'Tables': [
        ('Meeting Table 6-Seat', 599, 371),
        ('Round Café Table', 249, 156),
        ('Height-Adjustable Table', 429, 267),
    ],
    'Lighting': [
        ('LED Desk Lamp', 39, 22),
        ('Floor Lamp', 89, 54),
        ('Task Light Clamp', 29, 17),
        ('Pendant Fixture', 119, 71),
    ],
}

ANOMALY_PRODUCTS = {'Task Chair Basic', 'Storage Cart'}
# How many times its own normal volume each anomaly product sells in September.
# The offsetting trim is CONTAINED to that product's own category (its siblings)
# down to SIBLING_TRIM_FLOOR; only the (small) leftover that siblings genuinely
# can't absorb spills — thinly, down to OUTSIDE_TRIM_FLOOR — across every OTHER
# category, so Central's TOTAL still lands at a normal month's total. Net effect:
# Desks/Tables/Lighting are essentially untouched; Seating/Storage's own totals
# move only modestly; Seating/Storage's own RATIO does dip for real (a category is
# only 5-8 products, so one of them selling 8x doesn't disappear in the average);
# the anomaly products themselves spike ~8-9x, unmistakable once isolated. Both
# categories were widened to 7-8 products (from 5-6) specifically to buy enough
# sibling headroom for this multiplier without the leftover spilling far.
ANOMALY_BOOST_MULT = 8.0
SIBLING_TRIM_FLOOR = 0.15   # a category's siblings can be trimmed by at most 85%
OUTSIDE_TRIM_FLOOR = 0.85   # every other category can be trimmed by at most 15%

# Baseline monthly unit-volume index per region (mild, realistic growth Jan->Sep),
# shared by every product — this is what keeps "a regular month" comparable.
REGION_GROWTH = {
    'Central': [1.00, 1.03, 1.06, 1.04, 1.08, 1.10, 1.12, 1.11, 1.14],
    'East':    [1.00, 1.04, 1.08, 1.06, 1.10, 1.13, 1.16, 1.14, 1.18],
    'South':   [1.00, 1.02, 1.05, 1.04, 1.07, 1.09, 1.11, 1.10, 1.13],
    'West':    [1.00, 1.03, 1.07, 1.05, 1.09, 1.11, 1.14, 1.12, 1.16],
}

PRICE_OF = {name: price for products in CATALOG.values() for name, price, cost in products}
CATEGORY_OF = {name: cat for cat, products in CATALOG.items() for name, price, cost in products}
CATEGORY_PRODUCTS = {cat: [name for name, price, cost in products] for cat, products in CATALOG.items()}

# Baseline monthly unit volume per product (roughly proportional to price band,
# cheaper/more common items sell more units), before region growth is applied.
def base_units(price):
    if price < 60:
        return 140
    if price < 120:
        return 95
    if price < 250:
        return 55
    if price < 450:
        return 28
    return 14

rows = []
for month_i, month in enumerate(MONTHS):
    for region in REGIONS:
        growth = REGION_GROWTH[region][month_i] * REGION_SIZE_FACTOR[region]
        discount = REGION_DISCOUNT[region]
        is_anomaly = (region == ANOMALY_REGION and month == ANOMALY_MONTH)

        # Independent per-region-month margin wobble (input-cost/mix noise), so the
        # profit-ratio line has natural bounce instead of sitting on a flat rail.
        # It stacks on top of, and is much smaller than, the anomaly's mix shift.
        margin_noise = random.uniform(-0.045, 0.045)

        # First pass: "normal" unit volume for every product this region/month.
        normal_units = {}
        for category, products in CATALOG.items():
            for name, price, cost in products:
                bu = base_units(price) * growth
                bu *= random.uniform(0.93, 1.07)  # small noise, same every region
                normal_units[name] = bu

        if is_anomaly:
            # Mix shift, mostly contained per category: each anomaly product sells
            # ANOMALY_BOOST_MULT x its own normal volume. Its own category's
            # siblings absorb as much of that as they plausibly can (down to
            # SIBLING_TRIM_FLOOR); whatever they can't spills thinly across every
            # OTHER category, so total Central revenue this month still lands at a
            # normal month's total.
            final_units = dict(normal_units)
            residual_value = 0.0
            anomaly_categories = {CATEGORY_OF[n] for n in ANOMALY_PRODUCTS}

            for name in ANOMALY_PRODUCTS:
                cat = CATEGORY_OF[name]
                siblings = [p for p in CATEGORY_PRODUCTS[cat] if p != name]
                boosted_units = normal_units[name] * ANOMALY_BOOST_MULT
                extra_value = (boosted_units - normal_units[name]) * PRICE_OF[name]
                siblings_value = sum(normal_units[s] * PRICE_OF[s] for s in siblings)
                max_absorb = siblings_value * (1 - SIBLING_TRIM_FLOOR)
                absorbed = min(extra_value, max_absorb)
                residual_value += extra_value - absorbed

                trim_scale = 1 - (absorbed / siblings_value if siblings_value else 0)
                final_units[name] = boosted_units
                for s in siblings:
                    final_units[s] = normal_units[s] * trim_scale

            if residual_value > 0:
                outside_products = [n for n in normal_units if CATEGORY_OF[n] not in anomaly_categories]
                outside_value = sum(normal_units[n] * PRICE_OF[n] for n in outside_products)
                outside_trim_scale = max(OUTSIDE_TRIM_FLOOR, 1 - residual_value / outside_value)
                for n in outside_products:
                    final_units[n] = normal_units[n] * outside_trim_scale
        else:
            final_units = normal_units

        for category, products in CATALOG.items():
            for name, price, cost in products:
                units = round(final_units[name])
                if units < 1:
                    units = 1
                gross_sales = units * price
                sales = gross_sales * (1 - discount)
                discount_amount = gross_sales * discount
                total_cost = units * cost * (1 + margin_noise)
                profit = sales - total_cost
                # Orders: a handful of units per order, with mild noise.
                avg_units_per_order = random.uniform(1.6, 2.4)
                orders = max(1, round(units / avg_units_per_order))

                rows.append({
                    'Month': month,
                    'Region': region,
                    'Category': category,
                    'Product': name,
                    'Units': units,
                    'Sales': round(sales, 2),
                    'Cost': round(total_cost, 2),
                    'Profit': round(profit, 2),
                    'Orders': orders,
                    'Discount Amount': round(discount_amount, 2),
                })

df = pd.DataFrame(rows)

out_dir = r"C:\Users\Haim\OneDrive - Shmulik Yoffe\Desktop\Roster\1_O-output\projects\speaker-development\hayadata-2026-talk\demo"
xlsx_path = out_dir + r"\furniture_office_data.xlsx"
df.to_excel(xlsx_path, index=False, sheet_name='Data')

# Sanity check: print profit ratio by region/month to confirm the story.
pivot = df.groupby(['Region', 'Month']).apply(lambda g: g['Profit'].sum() / g['Sales'].sum())
pivot = pivot.reindex(pd.MultiIndex.from_product([REGIONS, MONTHS], names=['Region', 'Month']))
print(pivot.unstack().round(3).to_string())

print("\nCentral sales by month (check 'regular month' claim):")
central_sales = df[df.Region == 'Central'].groupby('Month')['Sales'].sum().reindex(MONTHS)
print(central_sales.round(0).to_string())

js_path = out_dir + r"\data.js"
with open(js_path, 'w', encoding='utf-8') as f:
    f.write('// Generated by generate_data.py from furniture_office_data.xlsx — do not hand-edit.\n')
    f.write('const RAW_ROWS = ')
    f.write(json.dumps(rows, separators=(',', ':')))
    f.write(';\n')

print(f"\nWrote {len(rows)} rows to:\n  {xlsx_path}\n  {js_path}")
