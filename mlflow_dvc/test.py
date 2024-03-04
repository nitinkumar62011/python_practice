from flask import Flask
#mlflow ui for visualisation of mlflow
import mlflow
def Calculate(x,y):
    return x+y
if __name__=="__main__":
    with mlflow.start_run():
        x=10
        y=90
        result=Calculate(x,y)
        mlflow.log_param("x",x)
        mlflow.log_param("y",y)
        mlflow.log_param("result",result)