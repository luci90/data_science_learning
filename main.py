from flask import Flask, render_template, request

from tensorflow import keras
import pandas as pd

model = keras.models.load_model('model.h5')

app = Flask(__name__)
@app.route('/', methods=["GET", "POST"])

def index():
    if request.method == "POST":
        pokazatel_1 = float(request.form['pokazatel_1'])
        pokazatel_2 = float(request.form['pokazatel_2'])
        pokazatel_3 = float(request.form['pokazatel_3'])
        pokazatel_4 = float(request.form['pokazatel_4'])
        pokazatel_5 = float(request.form['pokazatel_5'])
        pokazatel_6 = float(request.form['pokazatel_6'])
        pokazatel_7 = float(request.form['pokazatel_7'])
        pokazatel_8 = float(request.form['pokazatel_8'])
        pokazatel_9 = float(request.form['pokazatel_9'])
        pokazatel_10 = float(request.form['pokazatel_10'])
        pokazatel_11 = float(request.form['pokazatel_11'])
        pokazatel_12 = float(request.form['pokazatel_12'])

        d = {'col1': [pokazatel_1],
             'col2': [pokazatel_2],
             'col3': [pokazatel_3],
             'col4': [pokazatel_4],
             'col5': [pokazatel_5],
             'col6': [pokazatel_6],
             'col7': [pokazatel_7],
             'col8': [pokazatel_8],
             'col9': [pokazatel_9],
             'col10': [pokazatel_10],
             'col11': [pokazatel_11],
             'col12': [pokazatel_12]}

        df_pred = pd.DataFrame(data=d)



        result = model.predict(df_pred).flatten()[0]

        return render_template('result.html', pokazatel_1=pokazatel_1,
                               pokazatel_2=pokazatel_2,
                               pokazatel_3=pokazatel_3,
                               pokazatel_4=pokazatel_4,
                               pokazatel_5=pokazatel_5,
                               pokazatel_6=pokazatel_6,
                               pokazatel_7=pokazatel_7,
                               pokazatel_8=pokazatel_8,
                               pokazatel_9=pokazatel_9,
                               pokazatel_10=pokazatel_10,
                               pokazatel_11=pokazatel_11,
                               pokazatel_12=pokazatel_12,
                               result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

