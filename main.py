import threading
from queue import Queue
from spider import *
from general import *
from domain import *
from link_finder import *

Project_name = 'facebook'

homepage = 'https://facebook.com/'

Domain_name = get_domain_name(homepage)

queue_file = Project_name + '/queue.txt'

crawled_file = Project_name + '/crawled.txt'

number_thread = 8 

queue = Queue()
Spider(Project_name,homepage,Domain_name)


def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name,url)
        queue.task_done()


# create worker threads
def create_workers():
    for _ in range(number_thread):
        t= threading.Thread(target=work)
        t.daemon = True
        t.start()




def create_jobs():
    for links in file_to_set(queue_file):
        queue.put(links)
    queue.join()
    crawl()
# check if items in queue then crawl
def crawl():
    queued_links = file_to_set(queue_file)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + 'that no. of queues ')
        create_jobs()



create_workers()
crawl()