from flask import Flask, render_template, request
import random
import OpticFlowFinal
app = Flask(__name__)


def returnSpeed():
    #Put your speed function here
    
    return OpticFlowFinal.valRet()
@app.route('/',methods= ['GET'])
def aji():
    speed=returnSpeed()
    if returnSpeed()[3] == 1:
    	return render_template('speed.html',speed=returnSpeed()[0],currVol=returnSpeed()[1],predictedVol=returnSpeed()[2])
    else:
    	return render_template('speed1.html',speed=returnSpeed()[0],currVol=returnSpeed()[1],predictedVol=returnSpeed()[2])
if __name__ == '__main__':
   app.run(debug = True)
