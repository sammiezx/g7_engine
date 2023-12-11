import pandas as pd
from pulp import LpProblem, LpVariable, lpSum, LpMinimize


def optimize_inventory(df_forecast):
    # Define constants
    holding_cost = 1  # Holding cost per unit
    ordering_cost = 50  # Ordering cost per order

    # Create a linear programming problem
    prob = LpProblem("Inventory_Optimization", LpMinimize)

    # Decision variables
    order_vars = LpVariable.dicts("Order", df_forecast.index, lowBound=0, cat='Integer')

    # Objective function
    prob += lpSum(order_vars[i] * ordering_cost for i in df_forecast.index) + \
            lpSum(df_forecast['yhat'][i] * holding_cost * order_vars[i] for i in df_forecast.index), "Total_Cost"

    # Demand constraint
    for i in df_forecast.index:
        prob += order_vars[i] >= df_forecast['yhat'][i], f"Demand_Constraint_{i}"

    # Solve the linear programming problem
    prob.solve()

    # Extract the optimized order quantities
    optimized_orders = {i: order_vars[i].varValue for i in df_forecast.index}

    return optimized_orders