from sklearn.metrics import f1_score

def get_macro_f1(y_true, y_pred):
    """
    Calculates Macro-F1 score for multiclass classification.
    """
    return f1_score(y_true, y_pred, average="macro")
