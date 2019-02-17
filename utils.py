from sklearn.metrics import roc_auc_score
import sys
import pandas as pd

def get_auc(y_true, y_score):
    auc = roc_auc_score(y_true, y_score)
    return auc


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) < 2:
        print "python calc_args.py <score_csv> <label_csv>"
        exit()
    score_csv = args[0]
    label_csv = args[1]
    y_score = pd.read_csv(score_csv).score.values
    y_true = pd.read_csv(label_csv).score.values
    auc = get_auc(y_true, y_score)
    print "AUC: ", auc
