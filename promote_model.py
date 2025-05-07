from mlflow.tracking import MlflowClient

client = MlflowClient()

client.transition_model_version_stage(
    name="best_telco_churn_model",
    version=17,
    stage="Production"
)
