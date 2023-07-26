from google.colab import auth
auth.authenticate_user()

import gspread
from google.auth import default
import pandas as pd

creds, _ = default()
gc = gspread.authorize(creds)
worksheet = gc.open('OE-QA').sheet1
rows = worksheet.get_all_values()

df = pd.DataFrame.from_records(rows[1:], columns=rows[0])
df
