import requests

response = requests.get("https://api.data.gov.my/flood-warning")
data = response.json()

states = set() # get all of states within malaysia
for entry in data:
    states.add(entry["state"])

numbered_states = []
for i, state in enumerate(sorted(states)):
    numbered_states.append((i+1, state))

print(numbered_states)
