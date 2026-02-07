import pandas as pd
import sys

def main(pred_path, test_nodes_path):
    preds = pd.read_csv(pred_path)
    test_nodes = pd.read_csv(test_nodes_path)

    # Basic Checks
    if "id" not in preds.columns or "y_pred" not in preds.columns:
        raise ValueError("predictions.csv must contain 'id' and 'y_pred'")

    if preds["id"].duplicated().any():
        raise ValueError("Duplicate IDs found")

    if preds["y_pred"].isna().any():
        raise ValueError("NaN predictions found")

    # Check for valid class integers (0-6)
    if not pd.api.types.is_integer_dtype(preds["y_pred"]) and not pd.api.types.is_float_dtype(preds["y_pred"]):
         raise ValueError("y_pred must be numbers")
         
    # Ensure range 0-6 (Cora has 7 classes)
    if ((preds["y_pred"] < 0) | (preds["y_pred"] > 6)).any():
        raise ValueError("Predictions must be class IDs between 0 and 6")

    # Check IDs match exactly
    if set(preds["id"]) != set(test_nodes["id"]):
        raise ValueError("Prediction IDs do not match test_nodes.csv")

    print("VALID SUBMISSION")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
