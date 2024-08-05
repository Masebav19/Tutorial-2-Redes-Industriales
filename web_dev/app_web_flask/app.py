from flask import Flask, render_template,request
from Scripts.Venv import env
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
venv = env()

@app.route('/',methods =['GET','POST'])
def main():
    class MbData:
        MbDirIp= "0.0.0.0",
        MbDir =[],
        State = False
    if request.method == 'POST':
        MbData.MbDirIp= request.form.get('DirIp')
        MbData.MbDir= [request.form.get('StartAdd'),request.form.get('StopAdd'),
                  request.form.get('StatusAdd'),request.form.get('ValueAdd')]
        MbData.State = True

        return render_template('index.html', data = MbData)
    else:
        return render_template('index.html', data = MbData)
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=venv.PORT,debug=False)