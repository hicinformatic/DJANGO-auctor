from library import Task
import os, sys, base64

scriptname = os.path.basename(__file__)[:-3]
taskid = sys.argv[1]
settings_dir = sys.argv[2]
task = Task(taskid, scriptname, settings_dir)
default_namespace = task.namespace
task.update('start', 'Started')

import urllib.request, urllib.parse, json, html
url = 'article/list/full.json'
task.namespace = 'auctor'
url = task.getUrl(url)
task.update('running', 'Get images')
task.namespace = default_namespace

def get_image(get_url, path_static):
    if get_url != 'None' and path_static != 'None':
        get_url = 'http://localhost:{port}{url}'.format(port=task.port, url=get_url)
        credentials = ('%s:%s' % (task.username, task.password))
        encoded_credentials = base64.b64encode(credentials.encode('ascii'))
        image = urllib.request.Request(get_url)
        image.add_header('Authorization', 'Basic %s' % encoded_credentials.decode("ascii"))
        if not os.path.exists(os.path.dirname(path_static)): os.makedirs(os.path.dirname(path_static))
        f = open(path_static,'wb')
        f.write(urllib.request.urlopen(image).read())
        f.close()
        print(get_url)

def get_articles(url, page):
    page_url = '%s?page=%s' % (url, page)
    curl = urllib.request.Request(page_url)
    credentials = ('%s:%s' % (task.username, task.password))
    encoded_credentials = base64.b64encode(credentials.encode('ascii'))
    curl.add_header('Authorization', 'Basic %s' % encoded_credentials.decode("ascii"))
    with urllib.request.urlopen(curl) as articles_url:
        articles = json.loads(articles_url.read().decode())
        for article in articles:
            get_image(article['get_thumbnail'], article['root_thumbnail'])
            get_image(article['get_banner'], article['root_banner'])
        if article['pagination']['current'] < article['pagination']['number']:
            get_articles(url, article['pagination']['current']+1)
    return True
get_articles(url, 1)

task.update('complete', 'Complete')