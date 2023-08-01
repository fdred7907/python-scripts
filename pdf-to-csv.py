# script to convert pdf to csv for data analysis

import tabula
import pandas
filename = input("Enter File Path:")
df = tabula.read_pdf("sample-csv.pdf",pages='all')

# df.to_csv('output.csv')
print(df)