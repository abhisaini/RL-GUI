
import sqlite3
import json, generate
# from # # print import # # print
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
        # print(x)
        coord_vis += [(y_c, x_c)]
    # print(len(coord_vis))
    return coord_vis

def getRew(grid, path, scene):

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
    total_rew = grid[y_c][x_c]

    for x in path:
        if x == 0:
            y_c -= 1
        elif x == 1:
            y_c += 1
        elif x == 2:
            x_c += 1
        elif x == 3:
            x_c -= 1
        # print( "p ", y_c, x_c, path)
        # return
        total_rew += grid[y_c][x_c]
    return total_rew


def compPath(coords, optCoords):
    total_dist = 0.0
    # # # print(coords)
    for point in coords:
        mdist = 20.0
        for optpt in optCoords:
            tmp_dist = abs(optpt[0] - point[0]) + abs(optpt[1] - point[1])
            if tmp_dist < mdist:
                mdist = tmp_dist
                # # print("tmp : ", point, optpt)
        total_dist += mdist
    # print(total_dist)
    return total_dist

def insertCalc(s0):
    load_grids()
    global grid_coordis, grid_rew
    # # print(getCoordis(s0[2], s0[5]))
    mycoords = getCoordis(json.loads(s0[2]), s0[5])
    pdf = compPath(mycoords, grid_coordis[s0[5]])
    plen = len(s0[2])
    rew_diff =( s0[3] - plen * plen * 0.5 * 0.1) / grid_rew[s0[5]]
    print("curr : ", str( s0[3] - plen * plen * 0.5 * 0.1),  " || opt : ", str(grid_rew[s0[5]]))
    plen_diff =  len(grid_coordis[s0[5]]) - len(mycoords)
    scene = s0[5]
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO calcs ( survey_id ,reward_diff, pdiffs, scenerio, path_len) VALUES (?,?,?,?,?)",(s0[0], rew_diff, pdf/ plen, scene, plen_diff) )
    conn.commit()


def insertDB(grid_sz, grid_nw, actions, scene):

	print(actions)
	conn = sqlite3.connect('database.db')
	cur = conn.cursor()
	cur.execute("INSERT INTO GRIDS (GRIDSZ ,PATH ,MATRIX, scenerio) VALUES (?,?,?,?)",(grid_sz, actions, grid_nw, scene) )
	conn.commit()
	return


def getGridDB(grid_sz, scene):
	conn = sqlite3.connect('database.db')
	cur = conn.cursor()
	cmd = "SELECT * FROM GRIDS WHERE GRIDSZ=" + str(grid_sz) + " AND scenerio = " +  str(scene)
	cur.execute(cmd)
	row = cur.fetchone()
	return row

def insertSurvey(gridsz, actions, reward, time, scene):
	conn = sqlite3.connect('database.db')
	cur = conn.cursor()
	tmp = "SELECT MAX(ID) FROM survey_resp"
	cur.execute(tmp)
	eid = cur.fetchone()[0]
	# print(eid)

	cur.execute("INSERT INTO survey_resp (gridsz ,action ,reward, time, scenerio) VALUES (?,?,?,?, ?)",(gridsz, actions, reward, time, scene) )
	conn.commit()

	tmp = "SELECT * FROM survey_resp where id =" + str(eid + 1)
	cur.execute(tmp)
	s0 = cur.fetchone()
	# # print(s0)
	insertCalc(s0)
	return

def showSurvey(grid_sz):
	conn = sqlite3.connect('database.db')
	cur = conn.cursor()
	cmd = "SELECT * FROM survey_resp WHERE gridsz=" + str(grid_sz)
	cur.execute(cmd)
	row = cur.fetchall()
	return row

def showCalcs():
	conn = sqlite3.connect('database.db')
	cur = conn.cursor()
	cmd = "SELECT * FROM calcs"
	cur.execute(cmd)
	row = cur.fetchall()
	return row


def getAVG(p):
    PD = 0.0
    DDPS = 0.0
    RW = 0.0
    ctr = 0
    calcs = showCalcs()
    # print(type)
    if p == 0:
        len(calcs)
        for x in calcs:
            PD += x[4]
            DDPS += x[2]
            RW += x[1]
            ctr += 1
        return PD/ctr, DDPS/ctr, RW/ctr
    for x in calcs:
        if x[3] == p:
            PD += x[4]
            DDPS += x[2]
            RW += x[1]
            ctr += 1
    return PD/ctr, DDPS/ctr, RW/ctr


def insertCalc_new(user_name, user_roll, grid, opt_action, gridsz, actions, reward, time, timeg, scene):

    # # print(getCoordis(s0[2], s0[5]))
    mycoords = getCoordis(json.loads(actions), int(scene))
    grid_coords = getCoordis(json.loads(opt_action), int(scene))

    pdf = compPath(mycoords, grid_coords)
    plen = len(json.loads(actions))
    rew_diff = (float(reward) - plen * plen * 0.5 * 0.1) /  getRew(json.loads(grid), json.loads(opt_action), int(scene))
    # printq("curr : ", (reward - plen * plen * 0.5 * 0.1), " || ", getRew(grid, opt_action, scene))
    # print("curr : ", str( s0[3] - plen * plen * 0.5 * 0.1),  " || opt : ", str(grid_rew[s0[5]]))
    plen_diff =  len(grid_coords) - len(mycoords)
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO calcs (name, roll_no, reward_diff, pdiffs, scenerio, path_len, time_taken, time_given ) VALUES (?,?,?,?,?,?,?,?)",
    (user_name, user_roll, rew_diff, pdf/ plen, scene, plen_diff, time, timeg) )
    # ( survey_id ,reward_diff, pdiffs, scenerio, path_len)
    conn.commit()
    if rew_diff > 0.75 :
        generate.updateTime(-1, scene)
    else:
        generate.updateTime(1, scene)




def load_grids():
    global grid_coordis, grid_rew
    grid_coordis = [0]
    grid_rew = [0]
    for x in range(1,6):
        gd = getGridDB(10, x)
        grid_coordis += [getCoordis(json.loads(gd[1]),x)]
        grid_rew += [getRew(gd)]


# # # print(grid_coordis)

# surveys = showSurvey(10)
# for s0 in surveys:
# 	insertCalc(s0)

#
# me = """9.93902 12.8421 8.71663 13.8168 1.23127 20.6623 2.51048 14.2361 8.65642 8.53208
# 2.61363 27.9924 16.4527 1.90766 11.6631 9.18846 17.6012 0.932384 11.7058 16.7574
# 7.24286 3.76452 4.03663 11.2972 7.19652 7.50594 1.55235 8.51413 7.77937 8.60909
# 5.28398 19.4578 7.55837 5.78214 3.9705 4.79105 18.9326 18.3731 18.9479 8.70942
# 27.9211 6.55108 16.0663 16.7635 10.4953 3.46503 5.92905 7.70239 8.38791 7.47266
# 8.75266 18.3099 8.45757 10.3794 18.276 1.53727 15.1478 10.8083 26.8213 18.7753
# 10.5989 19.5487 3.67239 16.0351 18.1285 6.07885 16.0667 20.3353 24.0237 18.9332
# 3.92238 11.587 6.01947 16.4635 10.2552 15.9228 22.0852 18.5281 20.0235 13.0041
# 11.265 16.2228 24.5859 0.77565 12.752 16.1233 11.2271 2.99652 8.6946 14.1279
# 20.9075 12.5259 10.7525 14.1224 6.9909 1.11627 11.568 12.2467 14.6226 20.3782"""

# act = ["2 1 2 0 2 1 1 3 3 1 3 1 1 2 1 1 1 2 1 2 2 0 2 0 2 2 0 2 0 2 1 1 3 1 1 2 ",
# "2 2 0 3 3 0 0 0 0 0 2 0 0 0 2 1 1 2 1 1 3 1 3 1 1 2 2 0 2 0 0 2 2 1 2 2 2 0 3 0 3 3 3 0 3 0 3 0 2 2 2 2 2 1 2 0 ",
# "1 3 1 1 3 3 1 1 2 2 2 1 3 3 1 2 2 1 1 3 0 3 3 0 0 3 1 1 3 0 3 0 2 0 2 0 3 3 3 1 3 1 1 1 2 1 3 3 ",
# "0 0 0 0 3 1 3 1 2 1 1 3 3 0 0 0 0 2 0 3 0 2 2 2 0 0 0 3 3 3 3 3 3 3 3 1 2 1 3 1 3 0 0 0 ",
# "2 1 2 0 2 1 1 3 3 1 3 1 2 2 2 2 1 1 1 2 2 2 0 2 0 2 1 1 3 1 1 3 3 0 3 3 1 3 3 0 3 1 3 "
# ]
# ctr = 1
# for x in act:
# 	insertDB(10, me, x, ctr)
# 	getGridDB(10, ctr)
# 	ctr += 1
# insertDB(10, me, "2 2 0 3 3 0 0 0 0 0 2 0 0 0 2 1 1 2 1 1 3 1 3 1 1 2 2 0 2 0 0 2 2 1 2 2 2 0 3 0 3 3 3 0 3 0 3 0 2 2 2 2 2 1 2 0 ", 2)


# def calSCAL(a, scene):
#     t_PD = 0.0
#     t_DDPS = 0.0
#     t_ctr = 0.0
#     for i in a:
#         PD = 0.0
#         DDPS = 0.0
#         ctr = 0
#         path_i = json.loads(i[2])
#         coords_i = some.getCoordis(path_i, scene)
#         for x in a:
#             if i == x:
#                 continue
#             path_x = json.loads(x[2])
#             coords_x = some.getCoordis(path_x, scene)
#             ddf = some.compPath(coords_i, coords_x) / len(path_x)
#             PD += abs(len(path_i) - len(path_x))
#             DDPS += ddf
#             ctr += 1
#         print("%.2f" % (PD/ctr), "%.2f" % (DDPS/ctr))
#         t_PD += (PD/ctr)
#         t_DDPS += (DDPS/ctr)
#         t_ctr += 1
#     print("%.2f" % (t_PD/t_ctr), "%.2f" % (t_DDPS/t_ctr))

'''

data = json.loads(open("data.json","r").read())

for x in data:
    if x[1] == 10:
        some.insertCalc(x)

'''
