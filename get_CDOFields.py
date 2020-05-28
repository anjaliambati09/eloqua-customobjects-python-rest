import sys
import csv
import json
import xlrd
import os
import pandas as pd
import glob

sys.path.append('./lib')
from eloqua_request import EloquaRequest

request = EloquaFieldRequest('site', 'user', 'password')

input_CDO_file = sys.argv[1]
output_CDO_file = sys.argv[2]

loc = (input_CDO_file)   
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
sheet.cell_value(0, 0) 
result_t = []
for i in range(sheet.nrows):
    result_t.__iadd__([sheet.cell_value(i, 0)]) 
    #print(sheet.cell_value(i, 0))
result_t.pop(0)
print(result_t)

for id in result_t: 
    print(id)
    url = '/customObjects/'+ id +'/fields'
    response = request.get(url, None)
#    print(response)
    JSON_object = json.dumps(response.decode('utf-8'))
    JSON_output = json.loads(JSON_object)
#    print (JSON_output)
    json_name = 'id_'+ id +'.json'
    csv_name = 'id_'+ id +'.csv'
#    print(json_name)
    f = open(json_name,'w')
    print (JSON_output, file=f)
    f.close()
    
    with open(json_name) as json_file:
        data = json.load(json_file)
    id_data = data['items']
    data_file = open(csv_name, 'w')
    csv_writer = csv.writer(data_file)
    count = 0
    for field in id_data:
        if count == 0:
            header = "internalName"+ '\n'
            data_file.write(header)
            count += 1
        data_file.write(field.get('internalName')+ '\n')
#        print (field.get('internalName'))
    data_file.close()

path = './'
all_files = glob.glob(os.path.join(path, "*.csv"))

sheet_name = output_CDO_file

writer = pd.ExcelWriter(sheet_name, engine='xlsxwriter')

for f in all_files:
    df = pd.read_csv(f)
    df.to_excel(writer, sheet_name=os.path.splitext(os.path.basename(f))[0], index=False)

writer.save()
print ("Deleting temporary files..........")

files_list = os.listdir(path)

for item in files_list:
    if item.endswith(".json"):
        os.remove(os.path.join(path, item))
    if item.endswith(".csv"):
        os.remove(os.path.join(path, item))
print ("Deleted temporary files Successfully.......")

print ("Program executed Successfully..........")
