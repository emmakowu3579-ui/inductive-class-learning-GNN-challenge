import pandas as pd
import sys

def main(pred_path, test_nodes_path):
    preds = pd.read_csv(pred_path)
    test_nodes = pd.read_csv(test_nodes_path)

    # 1. Check Columns
    if "id" not in preds.columns or "y_pred" not in preds.columns:
        raise ValueError("predictions.csv must contain 'id' and 'y_pred' columns")

    # 2. Check for Duplicates
    if preds["id"].duplicated().any():
        raise ValueError("Duplicate IDs found in submission")

    # 3. Check for Missing Values
    if preds["y_pred"].isna().any():
        raise ValueError("NaN (empty) predictions found")

    # 4. Check Values are Integers (Classes 0-6)
    # We check if they are whole numbers within the valid range
    if not pd.api.types.is_integer_dtype(preds["y_pred"]) and not pd.api.types.is_float_dtype(preds["y_pred"]):
         raise ValueError("y_pred must be numbers (0-6)")
         
    # Ensure they are within 0-6 range (Cora has 7 classes)
    if ((preds["y_pred"] < 0) | (preds["y_pred"] > 6)).any():
        raise ValueError("Predictions must be class IDs between 0 and 6")

    # 5. Check ID Matching
    if set(preds["id"]) != set(test_nodes["id"]):
        missing = set(test_nodes["id"]) - set(preds["id"])
        extra = set(preds["id"]) - set(test_nodes["id"])
        raise ValueError(f"IDs do not match test_nodes.csv. Missing: {len(missing)}, Extra: {len(extra)}")

    print("VALID SUBMISSION")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
