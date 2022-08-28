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