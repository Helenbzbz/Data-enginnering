import datetime, json, os, random, time

# change project-id to your actual project id from GCP
project = 'neworder-pipeline-270104'

CITIES = ['Chciago', 'Springfield', 'New York', 'Boston',]
FIRST_NAMES = ['Tom', 'Randy', 'Peter', 'Karl', 'Patricia', 'Kathy', 'Cindy', 'Melia','Noel',]
STORE = ['st570','st9300','st2610']
ITEMS = ['0101-shirt-blue-m', '0101-shirt-blue-s', '0101-shirt-blue-l',]

while True:
      first_name, last_name = random.sample(FIRST_NAMES, 2)
      data = {
              'event_timstamp':datetime.datetime.now().strftime("%Y-%m,-%d %H:%M:%S"),
              'order_creation_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
              'first_name': first_name,
              'last_name': last_name,
              'city': random.choice(CITIES),
              'store': random.choice(STORE),
              'item': random.choice(ITEMS),
              'amount': float(random.randrange(5000, 7000)) / 100,
      }
      message = json.dumps(data)
      command = "gcloud --project={} pubsub topics publish neworder --message='{}'".format(project, message)
      print(command)
      os.system(command)
      time.sleep(random.randrange(1, 5))