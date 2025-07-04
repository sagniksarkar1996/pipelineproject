from flask import Flask, request, render_template, jsonify
# Alternatively can use Django, FastAPI, or anything similar
from src.pipeline.prediction_pipeline import CustomData, PredictPipeline
 
application = Flask(__name__, static_folder='templates')
app = application
 
@app.route('/', methods = ['POST', "GET"])
 
def predict_datapoint():
    if request.method == "GET":
        return render_template("form.html")
    else:
        data = CustomData(
            carat = float(request.form.get('carat')),
            depth = float(request.form.get('depth')),
            table = float(request.form.get("table")),
            x= float(request.form.get("x")),
            y = float(request.form.get("y")),
            z = float(request.form.get("z")),
            cut = request.form.get("cut"),
            color = request.form.get("color"),
            clarity = request.form.get("clarity")
        )
    new_data = data.get_data_as_dataframe()
    predict_pipeline = PredictPipeline()
    pred = predict_pipeline.predict(new_data)
 
    results = round(pred[0],2)
 
    return render_template("form.html", final_result = results)
 
if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug= True)
 
#http://127.0.0.1:5000/ in browser
 