import azure.functions as func
import datetime
import json
import logging
import pickle
from sklearn.ensemble import RandomForestClassifier

app = func.FunctionApp()


@app.route(route="score", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
async def http_score(req: func.HttpRequest) -> func.HttpResponse:
    # Load the model
    with open('./src/rf_model.pkl', 'rb') as f:
        rf = pickle.load(f)

    # Get the parameters from the query string
    quantity = req.params.get('quantity',0)
    price = req.params.get('price',0)

    # Create a dataset for prediction
    dataset = [[quantity, price]]

    # Predict the class and probability
    prediction = rf.predict(dataset)
    probability = rf.predict_proba(dataset).tolist()


    return func.HttpResponse(
        json.dumps({"message": "Prediction successful", 
                    "prediction": prediction.tolist(),
                    "probability": probability,
                    "timestamp": datetime.datetime.now().isoformat()}),
        status_code=200,
        mimetype="application/json"
    )
