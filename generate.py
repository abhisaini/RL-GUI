import subprocess, json
def generateGrid(gridcount, scene):
    subprocess.call(['./generator', scene] , stdout=subprocess.PIPE)
    data = open('results.txt').read().strip().split("\n")
    grid_nw = []
    for x in data[4:-1]:
        tmp = []
        for y in x.strip().split(" "):
            tmp += [float(y)]
        grid_nw += [tmp]
    print(data[-1].split(" "))
    actions = [int(x) for x in data[-1].split(" ")]
    # print( grid_nw ,actions)
    return grid_nw, actions

def readtime(scene):
    fl = open("time.json", "r").read()
    return json.loads(fl)[scene]

def updateTime(flag, scene):
    fl = open("time.json", "r")
    data = json.loads(fl.read())
    fl.close()
    fl = open("time.json", "w")
    data[scene] += flag * 10
    fl.write(json.dumps(data))
# generateGrid(10, 1)
