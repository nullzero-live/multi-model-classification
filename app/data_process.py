#Sklearn with WandB
import os
import pandas as pd
import wandb
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegressionCV
from sklearn.svm import LinearSVC
from google.cloud import storage
import warnings
from sklearn.exceptions import ConvergenceWarning
import wandb
from aorc import acc_aorc
import wandb
             
def gc_auth():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "app/sklearn-gcp-391120-24b6db43202e.json"
    storage_client = storage.Client()
    bucket = storage_client.bucket("datasets-tabular")
    blob = bucket.blob("Heart_Failure_Details.csv")
    
    try:
        #fs = gcsfs.GCSFileSystem(project='sklearn-gcp')  # replace 'YOUR_PROJECT_ID' with your actual project id
        print("File Loaded...\n")
        with blob.open('r') as f:
            df = pd.read_csv(f)   
        print("successfully authorized...")
    except Exception as e:
        print(e)
        df = ""
    return df
     
def process_data(df):
    api_key = os.getenv("WANDB_API_KEY")

    if api_key is not None:
        # Retrieve the value of wandb api key
        wandb.init(project="multi-model-sklearn")
        wandb.login()
        
    else:
        print("WANDB KEY NOT FOUND")
        Exception("WANDB KEY NOT FOUND")
    #supress convergence warnings
    warnings.filterwarnings("ignore", category=ConvergenceWarning)
    X = df.drop('death', axis=1)
    y = df['death']
    print("dataframe set....\n")    

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)       
    print("fitting model...\n")      
   
    #Set classifiers to use
    clfs = [RandomForestClassifier(n_estimators=100, max_depth=4, random_state=42), LogisticRegressionCV(random_state=42)]
    
    results = {"Classifier": [], "Accuracy": [], "AORC": []}
    
    for classifier in clfs:
        print(f"Running {classifier}...\n")
        result = classifier.fit(X_train, y_train)
        print(f"Getting {classifier} predictions...\n")
        preds = result.predict(X_test)
        probs = classifier.predict_proba(X_test)

        acc, aorc = acc_aorc(y_test, preds)
        labels = ["No Death", "Death"]
        try:
            wandb.sklearn.plot_confusion_matrix(y_test, preds, labels)
            wandb.log({"accuracy": acc})
            wandb.log({"aorc": aorc})
            wandb.sklearn.plot_classifier(classifier, X_train, X_test, y_train, y_test, preds, probs, labels,
                                                            model_name=classifier, feature_names=None)

            wandb.sklearn.plot_roc(y_test, probs, labels)
        except Exception as e:
            print(e)
            pass
            
        print(f"The result for {classifier} is: Acc: {acc} and AORC: {aorc}\n")
        results["Classifier"].append(classifier)
        results["Accuracy"].append(acc)
        results["AORC"].append(aorc)
        
        
    return results

        
        
        
    










