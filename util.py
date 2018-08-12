import os
import run_nn
import run_dt
import run_rf

AVAILABLE_ALGORITHMS = {'DT': run_dt, 'RF': run_rf, 'NN': run_nn}
ALGORITHMS_NUMS = {'DT': 0, 'RF': 1, 'NN': 2}
ALGORITHMS_NAMES = {'DT': 'Decision Tree', 'RF': 'Random Forest', 'NN': 'Nearest Neighbour'}
FEATURES_MODULES_NUMBER = 3
AUTHORS_NUM = len(os.listdir("corpus/data"))
TEST_SIZE = 0.2
