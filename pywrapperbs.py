import requests

import json

url_base = "https://api.browserstack.com/4"

headers = {
    'authorization': "Basic xxxxxxxxxxxxxxxxxxxxxx"
    }


def get_browsers(flat=False,beta=False):
    url = url_base + "/browsers"
    params = {}

    if flat:
        params["flat"] = "true"

    if beta:
        params["all"] = "true"

    response = json.loads(requests.request("GET", url, headers=headers,params=params).text)
    print(response)
    return response

def create_worker(worker):
    url = url_base + "/worker"

    worker["url"] = "http://google.com"
    params = worker

    response = json.loads(requests.request("POST", url, headers=headers, params=params).text)
    print(response)
    return response

def take_screenshot(worker_id,format):
    url = url_base + "/worker/"+str(worker_id)+"."+format
    if format == "json":
        response = json.loads(requests.request("GET", url, headers=headers).text)
        print(response)
    return response

def get_worker_status(worker_id):
    url = url_base + "/worker/"+str(worker_id)

    response = json.loads(requests.request("GET", url, headers=headers).text)
    print(response)
    return response

def terminate_worker(worker_id):
    url = url_base + "/worker/"+str(worker_id)

    response = requests.request("DELETE", url, headers=headers)
    print(response)
    return response


def sample_js_test():
    browsers = get_browsers(True)
    worker = create_worker(browsers[0])
    if "id" in worker:
        take_screenshot(worker["id"],"json")
        status = get_worker_status(worker["id"])
        print status["status"]
        
        terminate_worker(worker["id"])


sample_js_test()