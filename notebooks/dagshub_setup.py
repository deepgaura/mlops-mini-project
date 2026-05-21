import dagshub
import mlflow

dagshub.init(repo_owner='deepgaura', repo_name='mlops-mini-project', mlflow=True)

with mlflow.start_run():
    mlflow.log_metric("accuracy", 42)
    mlflow.log_param("Param name", "Value")

print("Experiment logged successfully")