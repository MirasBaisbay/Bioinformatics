import requests
import json

query_url = "https://search.rcsb.org/rcsbsearch/v2/query?json="

query = {
    "query": {
        "type": "group",
        "logical_operator": "and",
        "nodes": [
            # {
            #     "type": "terminal",
            #     "service": "text",
            #     "parameters": {
            #         "attribute": "rcsb_entity_source_organism.taxonomy_lineage.name",
            #         "operator": "exact_match",
            #         "value": "Homo sapiens"
            #     }
            # },
            {
                "type": "terminal",
                "service": "text",
                "parameters": {
                    "attribute": "exptl.method",
                    "operator": "exact_match",
                    "value": "X-RAY DIFFRACTION"
                }
            },
            # {
            #     "type": "terminal",
            #     "service": "text",
            #     "parameters": {
            #         "attribute": "rcsb_entry_info.resolution_combined",
            #         "operator": "less_or_equal",
            #         "value": 3.0  
            #     }
            # },
            {
                "type": "terminal",
                "service": "text",
                "parameters": {
                    "attribute": "struct.title",
                    "operator": "contains_words",
                    # "value": "Vitamin D receptor"
                    "value" : "VDR"
                }
            }
        ]
    },
    "return_type": "entry",
    "request_options": {
        "paginate": {
            "start": 0,
            "rows": 120
        },
        "sort": [
            {
                "sort_by": "score",
                "direction": "desc"
            }
        ]
    }
}

response = requests.post(query_url, json=query)
print("Status Code:", response.status_code)

try:
    data = response.json()
    print("Response JSON:")
    print(json.dumps(data, indent=2))
except Exception as e:
    print("Error parsing JSON:", e)
    data = {}

if "result_set" in data:
    pdb_ids = [entry["identifier"] for entry in data["result_set"]]
    print("Found PDB IDs:", pdb_ids)
else:
    print("Key 'result_set' not found in the response.")