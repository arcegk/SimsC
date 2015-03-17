# Full path and name to your csv file
csv_filepathname="/home/arce/Control/ControlSims/test.csv"
# Full path to your django project directory
your_djangoproject_home="/home/arce/Control"

import sys,os
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'ControlSims.settings'

from control.models import Sim
import datetime

import csv
dataReader = csv.reader(open(csv_filepathname), delimiter=';', quotechar='"')

for row in dataReader:
	if row[0] != 'numero': # Ignore the header row, import everything else
		zipcode = Sim()
		zipcode.numero = row[0]
		zipcode.ide = row[1]
		zipcode.valor = row[2]
		zipcode.activa = True
		zipcode.fecha = datetime.datetime.now()
		zipcode.save()
