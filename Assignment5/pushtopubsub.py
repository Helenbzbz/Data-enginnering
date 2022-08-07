### Python code generate orders and messages
# I keep a record of order id as write it to a file index.txt
# And then Increase the order by 1 each time and rewrite
# I don't know what's exact item number, item quantity, or order total
# I keep those 3 variable as text strings
import calendar
import time
f = open('Assignment5/index.txt')
order_id = int(f.readlines()[0])

def writemessage ():
    current_GMT = time.gmtime()
    order_date = calendar.timegm(current_GMT)
    nextorderid = str(order_id+1)
    file = open('index.txt','w')
    file.write(nextorderid)
    return f'{order_id}, {order_date}, Item No, Item Quantity, Order Total.'


### Python code push message to the topic
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='Assignment5/serviceaccount.json'
from google.cloud import pubsub_v1

project_id = "assignment-module-5"
topic_id = "assignment5"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

def pushtotopic():
    message = writemessage()
    data = message.encode("utf-8")
    future = publisher.publish(topic_path, data)
    print(future.result())
print(f"Published messages to {topic_path}.")

pushtotopic()