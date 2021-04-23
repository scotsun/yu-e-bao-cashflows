import numpy as np


def generate_customer_dict(user_id, profile_tbl, cashflow_tbl):
    customer_dict = dict()
    customer_row = profile_tbl.loc[profile_tbl['user_id'] == user_id].iloc[0]
    customer_dict['user_id'] = int(customer_row['user_id'])
    customer_dict['sex'] = int(customer_row['sex'])
    customer_dict['city'] = customer_row['city']
    customer_dict['constellation'] = customer_row['constellation']

    cashflows = []
    num_records = cashflow_tbl.loc[cashflow_tbl['user_id'] == user_id].shape[0]
    for i in range(num_records):
        row = cashflow_tbl.loc[cashflow_tbl['user_id'] == user_id].iloc[i, :]
        cashflow = generate_cashflow_dict(row)
        cashflows.append(cashflow)

    customer_dict['cashflows'] = cashflows
    return customer_dict


def generate_cashflow_dict(row):
    cashflow_dict = dict()
    cashflow_dict['report_date'] = int(row['report_date'])
    # sub dict
    purchase = dict()
    purchase['purchase_bal_amt'] = int(row['purchase_bal_amt'])
    purchase['purchase_bank_amt'] = int(row['purchase_bank_amt'])
    purchase['revenue'] = int(row['share_amt'])

    balance = dict()
    balance['tBalance'] = int(row['tBalance'])
    balance['yBalance'] = int(row['yBalance'])

    redemption = dict()
    redemption['consumption'] = dict()
    consumption = redemption['consumption']
    consumption['category1'] = -1 if np.isnan(row['category1']) else int(row['category1'])
    consumption['category2'] = -1 if np.isnan(row['category2']) else int(row['category2'])
    consumption['category3'] = -1 if np.isnan(row['category3']) else int(row['category3'])
    consumption['category4'] = -1 if np.isnan(row['category4']) else int(row['category4'])

    redemption['transfer'] = dict()
    transfer = redemption['transfer']
    transfer['tftobal_amt'] = int(row['tftobal_amt'])
    transfer['tftocard_amt'] = int(row['tftocard_amt'])
    # assemble
    cashflow_dict['balance'] = balance
    cashflow_dict['purchase'] = purchase
    cashflow_dict['redemption'] = redemption
    return cashflow_dict