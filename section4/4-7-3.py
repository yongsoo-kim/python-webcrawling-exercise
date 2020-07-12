import io
import sys
import pandas_datareader.data as web
import datetime

from pandas import DataFrame

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# Start date & End date
start = datetime.datetime(2018, 2, 1)
end = datetime.datetime(2018, 2, 15)

# Google info call
gs = web.DataReader('KRX: 035720', 'iex', start, end)
print(gs)
#################################Google financial is not supported by this moudle anymore...
