from flask import Flask,url_for,request,redirect,render_template
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("Diabetes.pkl","rb"))

@app.route('/')
def home():
    return render_template("index.html")
@app.route('/predict',methods = ['POST','GET'])
def predict():
    if request.method == 'POST':
        value1 = request.form['1']
        value2 = request.form['2']
        value3 = request.form['3']
        value4 = request.form['4']
        value5 = request.form['5']
        value6 = request.form['6']
        value7 = request.form['7']
        value8 = request.form['8']

        pred_df=pd.DataFrame([pd.Series([value1,value2,value3,value4,value5,value6,value7,value8])])
        prediction = model.predict_proba(pred_df)
        result='{0:.{1}f}'.format(prediction[0][1], 2)
        result = str(float(result)*100)+'%'
        print(result)
        if result>str(0.5):
            return render_template('result.html',pred=f'You may have diabetes.\nProbability of having Diabetes is {result}')
        else:
            return render_template('result.html',pred=f'You are safe :)\n Probability of having diabetes is {result}')
if __name__ == '__main__':
    app.run(debug=True,use_reloader = False)