
import os.path as op
import socket

hn = socket.gethostname()


ROOT_DIR = ''

# Use the name of my computer to setup local variables and
# hold different configurations.
if hn == 'calm.local':
    # It is a good idea to setup the INKSCAPE_BINPATH for docstamp on Mac computers.
    INKSCAPE_BIN = '/Applications/Inkscape.app/Contents/Resources/bin/inkscape'
    api_key_file = op.expanduser('~/Projects/ep16/google_api_key.json')
elif hn == 'corsair':
    api_key_file = op.expanduser('~/Projects/ep16/google_api_key.json')
elif hn == "ferrari":
    api_key_file = op.expanduser('~/Projects/ep16/google_api_key.json')
elif hn == "opobook.local":
    api_key_file = op.expanduser('~/Projects/ep16/google_api_key.json')

# the ep2017 responses spreadsheet
sponsors_billing_worksheet = ('16ohl6y4n9RXfG5jizBYl1ns12UKFS3Crauyc1ZsP1G0',
                              'Form responses 1')

docker_name = 'webarch_ep2017_1'
epcon_db_path = '/home/webarch/volumes/webarch_ep2017_data_site/_data'

# TODO: add the key to the finaid submissions spreadsheet
finaid_submissions_worksheet = ('TBD', 'Form responses 1')

# EPS members
epsmembers_dockey = '1HUGxWLbAXg3VFIlbsiTaHTGvhf67_tXgiVCpmay6v4U/edit?ts=56dd7c8d'
