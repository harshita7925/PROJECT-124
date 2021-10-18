from flask import Flask,jsonify,request

app=Flask(__name__)
@app.route("/")

contacts=[
    {
        "id":1,
        "Name":"Raju",
        "Contact":"9987644456",
        "done":False
    },
    {
        "id":2,
        "Name":"Rahul",
        "Contact":"9876543222",
        "done":False
    }
]

@app.route("/add-data",methods=["POST"])

def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data!"
        },400)

    contacts={
        "id":tasks[-1]["id"]+1,
        "Name":request.json["Name"],
        "Contact":request.json.get("Contact","")
        "done":False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":"Added task successfully"
        })