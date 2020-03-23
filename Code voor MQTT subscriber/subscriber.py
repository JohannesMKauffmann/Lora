import ttn

# ------BEGIN MQTT TTN PART------ #

app_id = "co2_sensor_stenden"
access_key = "ttn-account-v2.J5ws5KGhK9jVP5p56HfG1VyLka8PecrVTtIsam6MpWA"


def uplink_callback(msg, client):
    humidity = msg.payload_fields.humidity
    temperature = msg.payload_fields.temperature
    datetime = msg.metadata.time
    add_meting(msg.dev_id, temperature, humidity, datetime)


handler = ttn.HandlerClient(app_id, access_key)
mqtt_client = handler.data()
mqtt_client.set_uplink_callback(uplink_callback)
mqtt_client.connect()
# ------END MQTT TTN PART------ #

def add_meting(nodeID, temperature, humidity, datetime):
    data = {'nodeID': nodeID, 'temperature': temperature, 'humidity': humidity, 'datetime': datetime}
    r = requests.post("https://lora2d.herokuapp.com/addmeasurement", json=data)
    print(r.status_code)
    data = r.json()
    print("added measurement with ID:" + str(data['measurement_id']))


while True:
    pass




