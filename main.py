import threading
import requests
import time
import sys, argparse

def startBotting(nThreads, nFor, delay, link):
    th = []
    for i in range(nThreads):
        th.append(threading.Thread(target=get, args=[link, nFor, delay]))

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


def setupArgouments():
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser()
        parser.add_argument('--username', help="Name github")
        parser.add_argument('--times', type=int, help="Times you want it to be done")
        parser.add_argument('--delay', type=float, help="Delay between each times")
        parser.add_argument('--threads', type=int, help="Numbers of threads")
        args = parser.parse_args()

        nameStart = args.username
        nForStart = args.times
        delaysStart = args.delay
        nThreadStart = args.threads
        return nameStart, nForStart, delaysStart, nThreadStart
    return None, None, None, None


def askMissingArgouments(nameInput, nForInput, delaysInput, nThreadInput):
    if nameInput is None:
        nameInput = input("Name github: ")
    if nForInput is None:
        nForInput = input("N Times: ")
    if delaysInput is None:
        delaysInput = float(input("Delay:"))
    if nThreadInput is None:
        nThreadInput = input("N Threads: ")
    return nameInput, nForInput, delaysInput, nThreadInput

def getCamoIp(github):
    # https://camo.githubusercontent.com
    html = requests.get("https://github.com/" + github)
    content = html.content.__str__()
    start = content.find("https://camo.githubusercontent.com")
    if start == -1:
        return False
    end = content[start:].find('"')
    return content[start:start+end]


if __name__ == '__main__':
    name, nFor, delays, nThread = setupArgouments()
    name, nFor, delays, nThread = askMissingArgouments(name, nFor, delays, nThread)
    ipCamo = getCamoIp(name)
    if not ipCamo:
        print("This user doesnt have a views counter")
    else:
        print("Start botting")
        startBotting(nThread, nFor, delays, ipCamo)
