import json, os, random, time

def datamerger():    
    order_items = open('Project/order_items.csv').readlines()
    orders = open('Project/orders.csv').readlines()

    dic_1 = {}
    dic_final = {}
    for line in order_items:
            row_list = line.strip().split(',')
            header = row_list[0].replace('"','')
            row_list.pop(0)
            dic_1[header] = row_list

    for line in orders:
            row_list = line.strip().split(',')
            header = row_list[0].replace('"','')
            if header in dic_1.keys():
                row_list.pop(0)
                dic_final[header] = dic_1[header]+row_list
                
    return dic_final

project_id = "optical-torch-360720"
topic_name = "order_receiver"

orders = datamerger()
ids = list(orders.keys())
infos = list(orders.values())
order_headers = [ids[0]]+infos[0]
row_index = 1

while True:
    entry = [ids[row_index]]+infos[row_index]
    data = {
        order_headers[0].replace('"',''):entry[0].replace('"',''),
        order_headers[1].replace('"',''):int(entry[1].replace('"','')),
        order_headers[2].replace('"',''):entry[2].replace('"',''),
        order_headers[3].replace('"',''):entry[3].replace('"',''),
        order_headers[4].replace('"',''):entry[4].replace('"',''),
        order_headers[5].replace('"',''):float(entry[5].replace('"','')),
        order_headers[6].replace('"',''):float(entry[6].replace('"','')),
        order_headers[7].replace('"',''):entry[7].replace('"',''),
        order_headers[8].replace('"',''):entry[8].replace('"',''),
        order_headers[9].replace('"',''):entry[9].replace('"',''),
        order_headers[10].replace('"',''):entry[10].replace('"',''),
        order_headers[11].replace('"',''):entry[11].replace('"',''),
        order_headers[12].replace('"',''):entry[12].replace('"',''),
        order_headers[13].replace('"',''):entry[13].replace('"','')
      }
    row_index += 1

    message = json.dumps(data)
    command = "gcloud --project={} pubsub topics publish order_receiver --message='{}'".format(project_id, message)
    print(command)
    os.system(command)
    time.sleep(random.randrange(1, 5))