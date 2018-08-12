import os
import run_svm
import run_dt
import run_rf

AVAILABLE_ALGORITHMS = {'DT': run_dt, 'RF': run_rf, 'SVM': run_svm}
ALGORITHMS_NUMS = {'DT': 0, 'RF': 1, 'SVM': 2}
FEATURES_MODULES_NUMBER = 3
AUTHORS_NUM = len(os.listdir("corpus/data"))
TEST_SIZE = 0.2
