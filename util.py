import os
import run_svm
import run_dt
import run_rf

AVAILABLE_ALGORITHMS = {'DT': run_dt, 'RF': run_rf, 'SVM': run_svm}
ALGORITHMS_NUMS = {'DT': 0, 'RF': 1, 'SVM': 2}
authors_num = len(os.listdir("corpus/data"))
