## __Author identification for literature books__

This library helps classify an author out of a candidates list, based only on a given text sample.

#### Running the library
We included an option to run this library using `venv` module to create a [virtual environment](https://docs.python.org/3/tutorial/venv.html) using:
```python
python3 -m venv env
source env/bin/activate
```
A dedicated file that will update the required libraries (you can check them over Dependencies section) and runs the program with its default parameters:
```python
run.sh
```
Running the program with selected parameters:
```python
usage: run.sh "author_auth.py [-h] [-authors_num AUTHORS_NUM] [-test TEST]
                              [-algo_list ALGO_LIST [ALGO_LIST ...]] [-split_by_book]
                              [-repeat] [-no_nltk_dwn] [-export_tree]"
```
##### For example:
To run over `7` different writers using `30%` of the data for test over *`Random Forest`* and *`Decision Tree`* algorithms for `100` (can be changed in `util.py`) iterations each, and finnaly will export a visualistion of the decision tree to `dt.pdf` file.
```python
run.sh "author_auth.py -authors_num 7 -test 0.3 -algo_list NN RF"
```
To find an informative description for each parameter use:
```python
run.sh "author_auth.py -h"
```

__For the course staff:__ Note that if you want to run with `-calc_data` flag, over the submitted `.zip` file you'll need a complete `/corpus/data` folder which can be achived in by download it [here](https://drive.google.com/open?id=1s1BBR1dwIDp4MRLOiFoT0-2Ls4Xbrlzb). (We did not submitted it due to size bound at the moodle submmit link)

#### Dependencies
Installing the required libraries can be done in two main ways:
```python
python3 dependencies/install_packages.py dependencies/requirements.txt
```
or
```
pip install --upgrade numpy scipy scikit-learn sklearn nltk matplotlib graphviz
```

