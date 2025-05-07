from fastapi import FastAPI, Request
import mlflow.pyfunc
import pandas as pd
import datetime
import mlflow
import uvicorn

app = FastAPI()

# 🔸 MLflow ile bağlantı
mlflow.set_tracking_uri("http://127.0.0.1:5000")
model_name = "best_telco_churn_model"

# 🔸 Model yükleniyor (try-except burada gerekli değil ama istersen eklenebilir)
model = mlflow.pyfunc.load_model(model_uri=f"models:/{model_name}/Production")

@app.post("/predict")
async def predict(request: Request):
    try:
        # 🔹 Gelen veriyi oku
        json_data = await request.json()
        input_df = pd.DataFrame(data=json_data["data"], columns=json_data["columns"])

        # 🔹 Tahmin yap
        prediction = model.predict(input_df)

        # 🔹 Performans logla
        with mlflow.start_run(run_name="Live Prediction", nested=True):
            mlflow.log_param("timestamp", datetime.datetime.now().isoformat())
            mlflow.log_param("input_shape", str(input_df.shape))
            mlflow.log_metric("prediction", float(prediction[0]))

        # 🔹 Yanıt döndür
        return {"prediction": int(prediction[0])}
    
    except Exception as e:
        return {"error": str(e)}  # 🛠️ Hata olduğunda açıklayıcı yanıt

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
