import csv
from pprint import pprint

file = open(
    "/home/amauri/projects/Arquivos/Billing/AWS/Arquivos_CSV/512792422459-aws-billing-detailed-line-items-with-resources-and-tags-2019-05-closed.csv")
fileReader = csv.reader(file)
data_csv = list(fileReader)

dic = {}

for i, data in enumerate(data_csv):
    dic[data_csv[0][i]] = data_csv[1][i]

pprint(dic)
# for i, row in enumerate(dados):
# 	print(f'{i} - {row}')
