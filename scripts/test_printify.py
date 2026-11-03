import os, urllib.request, json

env_path = '.env'
if not os.path.exists(env_path):
    print('STATUS:NO_ENV')
    exit(0)

lines = open(env_path, 'r', encoding='utf-8').read().splitlines()
token = ''
for line in lines:
    if line.strip().startswith('PRINTIFY_API_TOKEN='):
        token = line.split('=', 1)[1].strip('\"\' ')

if not token or token == 'PASTE_YOUR_PRINTIFY_API_TOKEN_HERE':
    print('STATUS:PLACEHOLDER')
    exit(0)

req = urllib.request.Request('https://api.printify.com/v1/shops.json', headers={'Authorization': f'Bearer {token}', 'User-Agent': 'TallSlimCollins-App'})
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        print('STATUS:SUCCESS')
        for s in data:
            print(f"SHOP_ID: {s.get('id')} | TITLE: {s.get('title')} | CHANNEL: {s.get('sales_channel')}")
except Exception as e:
    print(f'STATUS:ERROR - {e}')
