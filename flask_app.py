from flask import Flask, render_template, request
app = Flask(__name__)
import some, json, generate
@app.route('/')
def index():
   return render_template('index.html')

@app.route('/demo')
def demo():
   return render_template('demo.html')


def findMax(grid):
    mx = 0.0
    for i in grid:
        if max(i) > mx:
            mx = max(i)
    return mx
@app.route('/grid')
def getGrid():
    if request.method == 'GET':
        gridcount = request.args["gridcount"]
        scene = request.args["scene"]
        grid, actions = generate.generateGrid(gridcount, scene)
        return render_template('grid.html', gridcount = gridcount, actions = actions,
         grid = grid, max = findMax(grid), scene = scene, timer = generate.readtime(scene))

@app.route('/survey')
def rewardSubmit():
    if request.method == 'GET':

        user_name = request.args["user_name"]
        user_roll = request.args["user_roll"]
        grid = request.args["grid"]
        opt_action = request.args["opt_action"]
        gridsz = request.args["gridsz"]
        scene = request.args["scene"]
        # some.insertDB(gridsz, grid, opt_action, scene)
        time = request.args["time"]
        reward = request.args["reward"]
        actions = request.args["actions"]
        timeg = request.args["tg"]
        print(request.args.to_dict(flat=False))

        # fl = open("surveys_raw.json", "r")
        # data = json.loads(fl.read())
        # print(5 * "*\n", data, 5 * "*\n")
        # fl.close()
        # fl = open("surveys_raw.json", "w")
        # data += [request.args.to_dict(flat=False)]
        # print(5 * "*\n", data, 5 * "*\n")
        # fl.write(json.dumps(data))
        # fl.close()
        some.insertCalc_new(user_name, user_roll, grid, opt_action, gridsz, actions, reward, time, timeg, scene)
        return "1"

@app.route('/show')
def getSurvey():
    if request.method == 'GET':


        gridsz = request.args["gridsz"]
        resp = some.showSurvey(gridsz)
        if "json" in request.args:
            return json.dumps(resp)
        # print(resp)
        return render_template('survey.html', resp = resp)

@app.route('/calc')
def getCalcs():
    calcs = some.showCalcs()
    return render_template('calcs.html', calcs = calcs)
if __name__ == '__main__':
    app.use_reloader = True
    app.run(debug = True)



    # CREATE TABLE GRIDS (GRIDSZ PRIMARY INT , PATH TEXT, MATRIX TEXT)
