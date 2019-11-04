import requests, yaml, click, json, pickle

def gethost():
    global URL, API, HOST_ID
    get_host = requests.get(URL + '/api/v1/entity/infrastructure/hosts',
     params=API)
    print(get_host.url)
    host_list = get_host.json()
    for host in host_list:
        HOST_ID = host['entityId']
        break
    dumpwithpickle()

def posthost_tag(tag):
    global URL, API, HOST_ID
    tags = {'tags':[tag]}
    stat = requests.post(URL + '/api/v1/entity/infrastructure/hosts/'+HOST_ID,
    headers={'Content-Type': 'application/json', 'charset':'utf-8'},
    data=json.dumps(tags), params=API)
    print(stat.status_code)

def deletehost_tag(tag):
    global URL, API, HOST_ID
    stat = requests.delete(URL + '/api/v1/entity/infrastructure/hosts/'+HOST_ID+'/tags/'+tag,
    headers={'Content-Type': 'application/json', 'charset':'utf-8'}, 
    params=API)
    print(stat.status_code)

def dumpwithpickle():
    global HOST_ID
    pickle.dump(HOST_ID, open("host_id.p", "wb"))

def loadwithpickle():
    global HOST_ID
    HOST_ID = pickle.load(open("host_id.p", "rb"))

@click.command()
@click.option('--script','-s', 
help='''-----------Available Scripts-----------\n
    gethost : REQ: NONE ----- RES: Get's host entityID's\n
    post_tag : REQ: tag ----- RES: Sets tag for a host\n
    delete_tag : REQ: tag ----- RES: Removes tags for a host\n
    --------------------------------------\n''') 
@click.option('--tag')

def main(script, tag):
    global URL, API

    with open('etc/auth_param.yaml') as auth_file:
        config = yaml.load(auth_file, Loader=yaml.FullLoader)

    URL = config['auth'][0]['url']
    API = {'Api-Token': config['auth'][0]['api']}
    
    if script == 'gethost':
        gethost()
    elif script == 'post_tag' and tag:
        loadwithpickle()
        posthost_tag(tag)
    elif script == 'delete_tag' and tag:
        loadwithpickle()
        deletehost_tag(tag)
    else:
        print("No script with that name: {}".format(script))

if __name__ == "__main__":
    main()