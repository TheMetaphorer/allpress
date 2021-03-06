
import allpress
import threading

from importlib import reload
from os import stat
from sys import argv
from time import sleep

class ModuleReload(Exception):

    def __init__(self):
        super().__init__()

def stat_file(uri):
    stamp = stat(uri)
    while True:
        sleep(5)
        if stamp != stat(uri):
            raise ModuleReload
        else:
            continue
    

if __name__ == '__main__':
    while True:
        thread = threading.Thread(target=stat_file, args=('./allpress',))
        thread.start()
        try:
            test_crawl_url = argv[1]
            test_crawl_num_to_index = int(argv[2])
            test_crawler = allpress.web.Crawler(test_crawl_url)
            test_crawler.index_site(num_to_index=test_crawl_num_to_index)
        except KeyboardInterrupt:
            print('Keyboard interrupt. Hit enter to continue.')
            a = input(' ')
            print(test_crawler)
            del test_crawler
            reload(allpress)
            reload(allpress.web)
        except ModuleReload:
            print('Change in module detected. Reloading...')
            del test_crawler
            reload(allpress)
            reload(allpress.web)
        print('Tasks complete. Hit enter to reload modules and re-run.')
        a = input(' ')
        reload(allpress)
        reload(allpress.web)
