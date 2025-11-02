#/usr/bin/env python

import sys
import glob
import json

routes = [
    {'src': '/', 'dest': '/public'},
    {'src': '/(.*)', 'dest': '/public/$1'}
]

base_path = sys.argv[1]
out_path = sys.argv[2]

prefix_length = base_path.find('/public')
src_skip_length = prefix_length + len('/public')

for path in glob.glob('%s/**/*.html' % base_path):
    routes.insert(0, {'src': path[src_skip_length:-5], 'dest': path[prefix_length:]})

def write_vercel_config(filename, extra=None):
    output_config = {}
    rewrite_rules = []
    for route in routes:
        source = route['src']
        if '(' in source:
            continue
        if source == '/':
            continue
        destination = route['dest']
        if destination.startswith('/public'):
            destination = destination[len('/public'):]
            if not destination:
                destination = '/'
        rewrite_rules.append({'source': source, 'destination': destination})
    output_config['rewrites'] = rewrite_rules

    if extra:
        output_config.update(extra)

    with open('%s/%s' % (out_path, filename), 'w') as output:
        json.dump(output_config, output)

write_vercel_config('vercel.json', {'$schema': 'https://openapi.vercel.sh/vercel.json'})
