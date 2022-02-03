import threading
import requests
import time

ipCamo = "https://camo.githubusercontent.com/c46ade9101ee7d7d6ba8f7b87995263fc1efed462f929c58c4353a5e83dd1ece/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d6c696e7573746f7563687469707326636f6c6f723d384536344430"

nThread = 1
nFors = 100
delays = 0.1


def main(nThreads, nFor, delay):
    th = []
    for i in range(nThreads):
        th.append(threading.Thread(target=get, args=[ipCamo, nFor, delay]))

    for i in range(nThreads):
        th[i].start()

    for i in range(nThreads):
        th[i].join()


def get(ip, times, delayGet):
    for i in range(times):
        r = requests.get(ip)
        if not r.ok:
            print("Error")
            break
        time.sleep(delayGet)


if __name__ == '__main__':
    main(nThread, nFors, delays)
