from sklearn.metrics import roc_auc_score
from sklearn.metrics import accuracy_score

def acc_aorc(y_true, y_pred):
    aorc = roc_auc_score(y_true, y_pred)
    acc = accuracy_score(y_true, y_pred)
    return aorc, acc

