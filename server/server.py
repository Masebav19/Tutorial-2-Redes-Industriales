from flask import Flask, request,Response,json
from Scripts.user_env import env
from flask_cors import CORS
from Scripts.modbus_conection import  *
from Scripts.mysql_client import mysql_client

venv = env()

app = Flask(__name__)
CORS(app)


@app.route('/')
def main():
    return "Hola"
@app.route("/api/coil", methods=["POST"])
def WriteCoil():
    # Para Coil
    # Dir IP
    # MbAddres
    # Value
    if request.method=="POST":
        #NewRequ -> {MbServer,MbAdd,Value}
        NewRequ  = request.json
        try:
            state=write_simple_coil(ip= NewRequ["MbServer"],address=int(NewRequ["MbAdd"]),value=int(NewRequ["Value"]))
            newSql = mysql_client().insert_data(data={"MbType": "Coil","MbAdd": "0000"+str(NewRequ["MbAdd"]),"MbValue":NewRequ["Value"]})
            if state:
                return Response(response=json.dumps(NewRequ),status=200)
            else:
                return Response(response="No Modbus server "+NewRequ["MbServer"]+" response",status=500)
        except:
            return Response(response="Bad data",status=406)
        
@app.route("/api/contact",methods=["POST"])
def ReadContact():
    #Para conctact
    # Dir IP
    # MbAddres
    # Length
    if request.method=="POST":
        NewRequ  = request.json
        Value=read_contacts(ip= NewRequ["MbServer"],address=int(NewRequ["MbAdd"]),Length=int(NewRequ["Length"]))
        newSql = mysql_client()
        #for i in range(NewRequ["Length"]):
         #   newSql.insert_data(data={"MbType": "Contact","MbAdd": "1000"+str(int(NewRequ["MbAdd"])+i),"MbValue":int(Value[i])})
        if Value:
            return Response(response=json.dumps({"Value": Value}),status=200)
        else:
            return Response(response="No Modbus server "+NewRequ["MbServer"]+" response",status=500)
        
@app.route("/api/coils",methods=["POST"])
def WriteCoils():
    # Para Coil
    # Dir IP
    # MbAddres
    # Values
    if request.method=="POST":
        #NewRequ -> {MbServer,MbAdd,Values}
        NewRequ  = request.json
        try:
            state=write_multiple_coils(ip= NewRequ["MbServer"],address=int(NewRequ["MbAdd"]),value=int(NewRequ["Values"]))
            newSql = mysql_client()
            for i in range(len(NewRequ["Values"])):
                newSql.insert_data(data={"MbType": "Contact","MbAdd": "0000"+str(NewRequ["MbAdd"]+i),"MbValue":NewRequ["Values"][i]})
            if state:
                return Response(response=json.dumps(NewRequ),status=200)
            else:
                return Response(response="No Modbus server "+NewRequ["MbServer"]+" response",status=500)
        except:
            return Response(response="Bad data",status=406)
        
@app.route("/api/input",methods=["POST"])
def ReadInput():
    #Para conctact
    # Dir IP
    # MbAddres
    # Length
    if request.method=="POST":
        NewRequ  = request.json
        try:
            Values=read_inputs(ip= NewRequ["MbServer"],address=int(NewRequ["MbAdd"]),Length=int(NewRequ["Length"]))
            newSql = mysql_client()
            #for i in range(NewRequ["Length"]):
            #    newSql.insert_data(data={"MbType": "Contact","MbAdd": "3000"+str(int(NewRequ["MbAdd"])+i),"MbValue":Values[i]})
            if Values:
                return Response(response=json.dumps({"Value": Values}),status=200)
            else:
                return Response(response="No Modbus server "+NewRequ["MbServer"]+" response",status=500)
        except:
            return Response(response="Bad data",status=406)
        
@app.route("/api/holding",methods=["POST"])
def WriteHolding():
    # Para Coil
    # Dir IP
    # MbAddres
    # Value
    if request.method=="POST":
        #NewRequ -> {MbServer,MbAdd,Value}
        NewRequ  = request.json
        try:
            state=write_simple_holding(ip= NewRequ["MbServer"],address=int(NewRequ["MbAdd"]),value=int(NewRequ["Value"]))
            newSql = mysql_client().insert_data(data={"MbType": "Coil","MbAdd": "4000"+str(NewRequ["MbAdd"]),"MbValue":NewRequ["Value"]})
            if state:
                return Response(response=json.dumps(NewRequ),status=200)
            else:
                return Response(response="No Modbus server "+NewRequ["MbServer"]+" response",status=500)
        except:
            return Response(response="Bad data",status=406)
@app.route("/api/holdings",methods=["POST"])
def WriteHoldings():
    # Para Coil
    # Dir IP
    # MbAddres
    # Values
    if request.method=="POST":
        #NewRequ -> {MbServer,MbAdd,Values}
        NewRequ  = request.json
        try:
            state=write_multiple_holding(ip= NewRequ["MbServer"],address=int(NewRequ["MbAdd"]),value=int(NewRequ["Values"]))
            newSql = mysql_client()
            for i in range(len(NewRequ["Values"])):
                newSql.insert_data(data={"MbType": "Contact","MbAdd": "4000"+str(NewRequ["MbAdd"]+i),"MbValue":NewRequ["Values"][i]})
            if state:
                return Response(response=json.dumps(NewRequ),status=200)
            else:
                return Response(response="No Modbus server "+NewRequ["MbServer"]+" response",status=500)
        except:
            return Response(response="Bad data",status=406)

if __name__ == "__main__":
    app.run(debug=True,port=venv.SERVER_PORT,host='0.0.0.0')