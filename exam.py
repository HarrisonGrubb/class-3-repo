import os

delivery = {
'sender': 'Charlie',
'recipient': 'Anika',
'price': 16.99,
'status': 'In Transit',
'stops': ['New York', 'Denver', 'San Francisco']
}

print('A delivery from ', delivery['sender'], ' to ', delivery['recipient'])

stops = 0
for s in delivery['stops']:
    stops += 1
print(stops)

print(delivery['stops'][-1:])

print(os.path.dirname(__file__))

breakpoint()