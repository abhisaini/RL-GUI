from flask import Flask, render_template, request
app = Flask(__name__)
import some, json
@app.route('/')
def index():
   return render_template('index.html')

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
        print(gridcount)
        tmp = some.getGridDB(gridcount)
        actions = json.loads(tmp[1])
        grid = json.loads(tmp[2])
        print(max(grid))
        return render_template('grid.html', gridcount = gridcount, actions = actions, grid = grid, max = findMax(grid))

@app.route('/survey')
def rewardSubmit():
    if request.method == 'GET':
        gridsz = request.args["gridsz"]
        time = request.args["time"]
        reward = request.args["reward"]
        actions = request.args["actions"]
        some.insertSurvey(gridsz, actions, reward, time)
        return "1"

@app.route('/show')
def getSurvey():
    if request.method == 'GET':
        gridsz = request.args["gridsz"]
        resp = some.showSurvey(gridsz)
        return render_template('survey.html', resp = resp)

if __name__ == '__main__':
    app.use_reloader = True
    app.run(debug = True)



    # CREATE TABLE GRIDS (GRIDSZ PRIMARY INT , PATH TEXT, MATRIX TEXT)
