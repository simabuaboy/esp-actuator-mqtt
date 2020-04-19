
def sub_cb(topic, msg):
  a = msg.decode('utf-8')
  if a == '1':
        servo.duty(110)
        time.sleep(1)
        servo.duty(30)
  

def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub
  client = MQTTClient(client_id, mqtt_server)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_sub)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()

try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()

while True:
  try:
    new_message = client.check_msg()
    if new_message != 'None':
      button = Pin(34, Pin.IN)
      if button.value() ==1:
        client.publish(topic_pub, b'1')  
    time.sleep(1)
  except OSError as e:
    restart_and_reconnect()
    