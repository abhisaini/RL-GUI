import some, json
from pprint import pprint

def checkInter(path):
    coord_vis = []
    x_c, y_c = 0, 0
    coord_vis += [(0,0)]
    for x in path:
        if x == 0:
            y_c -= 1
        elif x == 1:
            y_c += 1
        elif x == 2:
            x_c += 1
        elif x == 3:
            x_c -= 1
        else:
            return 0
        if((y_c, x_c) in coord_vis):
            return 0
        coord_vis += [(y_c, x_c)]
    return 1
survey = some.showSurvey(10)
# pprint(survey)

id_f = []


for x in survey:
    path = json.loads(x[2])
    cval = checkInter(path)
    if cval == 0:
        id_f += [x[0]]

print("faulty id : ", id_f)
