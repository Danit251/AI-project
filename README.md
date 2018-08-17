## __Author identification for literature books__ 

This library helps classify an author out of a candidates list, based only on a given text sample.
#### Dependencies
Installing the required libraries can be done in two main ways:
```python
python3 dependencies/install_packages.py dependencies/requirements.txt
```
or 
```
pip install --upgrade numpy scipy scikit-learn sklearn nltk matplotlib graphviz
```

#### Running the library
A dedicated file that will update the required libraries and runs the program with its default parameters:
```python
run.sh
```
Running the program with selected parameters:
```python
usage: author_auth.py [-h] [-authors_num AUTHORS_NUM] [-test TEST]
                      [-algo_list ALGO_LIST [ALGO_LIST ...]] [-split_by_book]
                      [-repeat] [-no_nltk_dwn] [-export_tree]
```
##### For example:
To run `author_auth.py` over `4` different writers using `30%` of the data for test over *`Random Forest`* and *`Decision Tree`* algorithms for `100` (can be changed in `util.py`) iterations each, and finnaly will export a visualistion of the decision tree to `dt.pdf` file.
```python
author_auth.py -authors_num 4 -test 0.3 -algo_list RF DT -repeat -export_tree
```
To find an informative description for each parameter use:
```python
author_auth.py -h
```
