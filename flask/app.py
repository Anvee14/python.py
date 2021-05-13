from flask import Flask,jsonify,request
app = Flask(__name__)
'''
@app.route("/")
def hello_world():
    return "hello world"

if __name__ == "__main__":
    app.run()'''
#creating array of task with each task as adifferent object
tasks = [{
    'id':1,
    'title':u'buy groceries',
    'discription':u'milk,cheese,fruits',
    'done':False
},
{
    'id':2,
    'title':u'learning python',
    'discription':u'python tutorial on web',
    'done':False
}]
@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
        'status':"error",
        'message':"pls provide data",
        },400)
    task = {

        'id':tasks[-1]['id']+1,
        'title':request.json['title'],
        'discription':request.json.get('discription',""),
        'done':False
    }
    tasks.append(task)
    return jsonify({
        'status':"success",
        'message':"task added successfully",})

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })
if __name__ == "__main__":
    app.run()