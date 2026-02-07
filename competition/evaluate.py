import pandas as pd
import sys
from metrics import get_macro_f1

def main(pred_path, label_path):
    # Read files
    preds = pd.read_csv(pred_path).sort_values("id")
    labels = pd.read_csv(label_path).sort_values("id")

    # Merge checks
    merged = labels.merge(preds, on="id", how="inner")
    
    if len(merged) != len(labels):
        raise ValueError(f"ID mismatch! Found {len(merged)} matches, expected {len(labels)}")

    # Calculate Macro-F1 (using 'label' from your hidden file)
    score = get_macro_f1(merged["label"].astype(int), merged["y_pred"].astype(int))
    
    print(f"SCORE={score:.4f}")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
