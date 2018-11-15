import some, json
from pprint import pprint
import sqlite3

def getCoordis(path, scene):
    if scene == 1:
        x_c = 0
        y_c = 0
    elif scene == 3:
        x_c = 9
        y_c = 0
    elif scene == 2:
        x_c = 0
        y_c = 9
    elif scene == 4:
        x_c = 9
        y_c = 9
    elif scene == 5:
        x_c = 0
        y_c = 0
    coord_vis = [(y_c, x_c)]
    for x in path:
        if x == 0:
            y_c -= 1
        elif x == 1:
            y_c += 1
        elif x == 2:
            x_c += 1
        elif x == 3:
            x_c -= 1
        coord_vis += [(y_c, x_c)]
    return coord_vis

def getRew(grid):
    scene = grid[3]
    mat = json.loads(grid[2])
    path = json.loads(grid[1])
    if scene == 1:
        x_c = 0
        y_c = 0
    elif scene == 3:
        x_c = 9
        y_c = 0
    elif scene == 2:
        x_c = 0
        y_c = 9
    elif scene == 4:
        x_c = 9
        y_c = 9
    elif scene == 5:
        x_c = 0
        y_c = 0
    total_rew = mat[y_c][x_c]

    for x in path:
        if x == 0:
            y_c -= 1
        elif x == 1:
            y_c += 1
        elif x == 2:
            x_c += 1
        elif x == 3:
            x_c -= 1
        total_rew += mat[y_c][x_c]
    return total_rew


def compPath(coords, optCoords):
    total_dist = 0
    for point in coords:
        mdist = 20
        for optpt in optCoords:
            tmp_dist = (optpt[0] - point[0]) + (optpt[1] - point[1])
            if tmp_dist < mdist:
                mdist = tmp_dist
        total_dist += mdist
    return total_dist

def insertCalc(s0):
    global grid_coordis, grid_rew
    pdf = compPath(getCoordis(s0[2], s0[5]), grid_coordis[s0[5]])
    plen = len(s0[2])
    rew_diff = grid_rew[s0[5]] - s0[3]
    scene = s0[5]
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO calcs ( survey_id ,reward_diff, pdiffs, scenerio) VALUES (?,?,?,?)",(s0[0], rew_diff, pdf/ plen, scene) )
    conn.commit()

grids = []
grid_coordis = [0]
grid_rew = [0]
for x in range(1,6):
    gd = some.getGridDB(10, x)
    grids += [gd]
    grid_coordis += [getCoordis(json.loads(gd[1]),x)]
    grid_rew += [getRew(gd)]



# surveys = some.showSurvey(10)
# for s0 in surveys:
#     insertCalc(s0)
