import os
for d in ['analyzer', 'api_clients', 'data', 'logs', 'reports', 'scripts', 'tests', 'web']:
    p = os.path.join('phishscope', d)
    print(f"=== {d} ===")
    if os.path.exists(p):
        for f in sorted(os.listdir(p)):
            print(f)
    else:
        print("(empty)")