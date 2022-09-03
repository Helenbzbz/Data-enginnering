import json, os, random, time

project_id = "optical-torch-360720"
topic_name = "review_receiver"

reviews = open('Project/reviews.csv').readlines()
order_headers = reviews[0].strip().split(',')
row_index = 1

while True:
    entry = reviews[row_index].strip().split(',')
    data = {
        order_headers[0].replace('"',''):entry[0].replace('"',''),
        order_headers[1].replace('"',''):entry[1].replace('"',''),
        order_headers[2].replace('"',''):float(entry[2].replace('"','')),
        order_headers[3].replace('"',''):entry[3].replace('"',''),
        order_headers[4].replace('"',''):entry[4].replace('"',''),
        order_headers[5].replace('"',''):entry[5].replace('"',''),
        order_headers[6].replace('"',''):entry[6].replace('"','')
      }
    row_index += 1

    message = json.dumps(data)
    command = "gcloud --project={} pubsub topics publish review_receiver --message='{}'".format(project_id, message)
    print(command)
    os.system(command)
    time.sleep(random.randrange(1, 5))