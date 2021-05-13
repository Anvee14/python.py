from flask import Flask,jsonify,request
app = Flask(__name__)

#creating array of task with each task as a different object
data=[{
        'id':1,
        'contact':"9201299292",
        'name':'Hannah',
        'done':False
     },
     {
        'id':2,
        'contact':"9726547238",
        'name':'Folrina',
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

        'id':data[-1]['id']+1,
        'name':request.json['name'],
        'contact':request.json.get('contact',""),
        'done':False
    }
    data.append(task)
    return jsonify({
        'status':"success",
        'message':"task added successfully",})

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":data
    })
print(data)
if __name__ == "__main__":
    app.run()