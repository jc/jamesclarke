#/usr/bin/env python

import sys
import glob
import json

config = {'version': 2,
          'name': 'jamesclarke',
          'routes': [
              {'src' : '/', 'dest': '/public'},
              {'src' : '/(.*)', 'dest' : '/public/$1'}
          ]
          }

routes = config['routes']

base_path = sys.argv[1]
out_path = sys.argv[2]

prefix_length = base_path.find('/public')
src_skip_length = prefix_length + len('/public')

for path in glob.glob('%s/**/*.html' % base_path):
    routes.insert(0, {'src': path[src_skip_length:-5], 'dest': path[prefix_length:]})

with open('%s/now.json' % out_path, 'w') as output:
    json.dump(config, output)

