# POLICY MIGRATE SCRIPT

import requests

def retrieve_all_policy_ids():
    url = "https://absdcom/api" # Put URL

    AX_HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer Put API Key",
    }

    policy_ids = []

    query = {
    "o": "Put Orgs ID",
    "page": "0",
    "limit": "500"
    }

    ax_policies = requests.get(f"{url}/policies", headers=AX_HEADERS, params=query)
    data = ax_policies.json()
    for policy in data:
        policy_ids.append(policy['id'])

    return policy_ids

def list_specific_policy(policy_ids):

    url = "https://abcd.com/api"

    AX_HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer Put API Key",
    }

    AX_HEADERS_2 = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer Put API Key",
    }

    query = {
        "o": "Put Orgs ID"
    }
    for id in policy_ids:
        ax_policies = requests.get(f"{url}/policies/{id}", headers=AX_HEADERS, params=query)
        data = ax_policies.json()
        query2 = {
        "o": "109007"
        }
        # Formats all relevant info for the current org to be POSTed to the new org
        body = {
        "name": data['name'],
        "policy_type_name": data['policy_type_name'],
        "organization_id": 'Put Orgs ID',
        "schedule_days": data['schedule_days'],
        "schedule_weeks_of_month": data['schedule_weeks_of_month'],
        "schedule_months": data['schedule_months'],
        "schedule_time": data['schedule_time'],
        "configuration": data['configuration']
        }
        ax_policies_post = requests.post(f"{url}/policies", json=body, headers=AX_HEADERS_2, params=query2)
        print(ax_policies_post)

policies = retrieve_all_policy_ids()

list_specific_policy(policies) 