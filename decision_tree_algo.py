import numpy as np
import random
import copy
from numpy.core.defchararray import startswith, endswith
import matplotlib.pyplot as plt
from treelib import Tree, Node
from math import log

original_tree = None
index = 0
j = 0


def set_index_value():
    global index
    index = 1


def get_data(file_name):
    data = []
    for line in open(file_name).readlines():
        data.append(line.split())
    return data

"""
@examples: list that is not empty.
"""
def get_majority_label(examples):
    labels_list = {}
    for example in examples:
        label = example[len(example)-1]
        if label in labels_list:
            labels_list[label] += 1
        else:
            labels_list[label] = 1

    major_label = None
    count_label = 0
    for label in labels_list:
        if labels_list[label] > count_label:
            count_label = labels_list[label]
            major_label = label

    return major_label


def information_gain(prob_list):
    if len(prob_list) == 0 or len(prob_list) == 1:
        return 0
    result = 0
    for prob in prob_list:
        if prob != 0:
            result -= prob * log(prob, 2)
    return result


def information_gain_process(examples):
    dict_pos = {}
    for example in examples:
        current_option = example[len(examples[0]) - 1]
        if current_option in dict_pos:
            dict_pos[current_option] += 1
        else:
            dict_pos[current_option] = 1

    probablities_list = []
    for pos in dict_pos:
        probablities_list.append(dict_pos[pos] / len(examples))

    return information_gain(probablities_list)


def feature_gain(examples, feature, possiblities_list):
    new_gain = 0.0
    for possiblity in possiblities_list:
        pos_subset = split_data(examples, feature, possiblity)  # only examples that equal to pos are left
        if len(pos_subset) == 0:
            break
        probability = float(len(pos_subset) / len(examples))
        # conditional_probablity = len(split_data(examples_subset, len(examples[0]) - 1, value)) / \
        #                          len(examples_subset)
        new_gain += (probability * information_gain_process(pos_subset))
    return new_gain


def get_optimal_feature(examples, all_features, possiblities_list):
    optimal_feature = -1
    higher_gain = 0.0
    # TODO delete
    # labels_list = ['republican.', 'democrat.']
    # label_split = split_data(examples, len(examples[0]) - 1, labels_list[0])
    # if len(label_split) != 0 and len(examples) != 0:
    #     current_gain = information_gain(len(label_split) / len(examples))
    if len(examples) != 0:
        current_gain = information_gain_process(examples)
    else:
        current_gain = 0

    for feature in all_features:
        calculate_gain = current_gain
        # TODO for specific features
        # possiblities_list = ['y', 'n', 'u']
        # new_gain = feature_gain(examples, feature, possiblities_list[feature])
        new_gain = feature_gain(examples, feature, possiblities_list)
        calculate_gain -= new_gain
        # print(str(feature)+" = "+ str(calculate_gain))
        if calculate_gain >= higher_gain:
            higher_gain = calculate_gain
            optimal_feature = feature

    return optimal_feature


"""
@:return the examples that their optimal features equals to the chosen_pos
"""


def split_data(examples, optimal_feature, chosen_pos):
    new_data = []
    for example in examples:
        if example[optimal_feature] == chosen_pos:
            new_list = example[:]
            new_data.append(new_list)
    return new_data


def merge_trees(my_tree, sub_tree, node_id, i, value, examples):
    global index
    if sub_tree is not None:
        if isinstance(sub_tree, Tree):
            node = sub_tree.get_node(node_id)
            name = str(node.tag)
            identifier = str(node.identifier)
            my_tree.create_node(name, identifier, parent=i)

            for child in sub_tree.children(node_id):
                child_subtree = sub_tree.subtree(child.identifier)
                if isinstance(child_subtree, Tree):
                    my_tree.paste(str(node_id), child_subtree)
                else:
                    name = str(child.tag)
                    identifier = str(child.identifier)
                    my_tree.create_node(name, identifier, parent=id)
        else:
            name = str(value) + " : " + str(sub_tree)
            my_tree.create_node(str(name), index, parent=i)
        index += 1
        return my_tree
    else:
        # TODO random result and not majority ???
        if not examples:
            name = str(value) + " : " + random.choice(labels_list)
        else:
            name = str(value) + " : " + str(get_majority_label(examples))
        print(name)
        my_tree.create_node(str(name), index, parent=i)
        index += 1
        return my_tree


def are_samples_equals(examples):
    label = examples[0][len(examples[0]) - 1]
    for example in examples:
        if example[len(examples[0]) - 1] != label:
            return None
    return label


def build_tree(examples, all_features, i, value, possibilities_list, height):
    # examples_list = [example[-1] for example in examples]
    my_tree = Tree()

    # if examples is None:
    #     return None

    if not examples:
        return None

    all_equals = are_samples_equals(examples)
    if all_equals is not None:
        return all_equals

    if height == 0 or len(all_features) == 0:
        return get_majority_label(examples)

    if len(all_features) == 1:
        optimal_feature = all_features.pop()
    else:
        optimal_feature = get_optimal_feature(examples, all_features, possibilities_list)

    if value is None:
        my_tree.create_node(optimal_feature, i)
    else:
        # feature = features_list[optimal_feature]
        # name = str(value) + " : " + feature
        name = str(value) + " : " + str(optimal_feature)
        my_tree.create_node(str(name), i)
    all_features.discard(optimal_feature)

    global index
    index += 1

    # TODO possibilities_list for specific feature
    for pos in possibilities_list:
        tree1_index = index
        features_copy = all_features.copy()
        partial_examples = split_data(examples, optimal_feature, pos)
        new_tree1 = build_tree(partial_examples, features_copy, tree1_index, pos, possibilities_list, height - 1)
        my_tree = merge_trees(my_tree, new_tree1, tree1_index, i, pos, partial_examples)

    return my_tree


def find_child(children, node, feature_choice):
    for child in children:
        name = child.tag
        if startswith(name, feature_choice):
            return child
    return None


def is_error(my_tree, data):
    if not isinstance(my_tree, Tree):
        if my_tree == data[len(data) - 1]:
            return 0
        return 1
    node = my_tree.get_node(my_tree.root)
    first = True
    while node is not None:
        tree = my_tree.subtree(node.identifier)
        if len(tree.nodes) > 1:
            if first:
                feature = data[int(node.tag)]
                first = False
            else:
                feature = data[int(node.tag[4:])]
            children = my_tree.children(node.identifier)
            node = find_child(children, node, feature)
        else:
            tree_label = node.tag
            data_label = data[len(data) - 1]
            if endswith(tree_label, data_label):
                return 0
            else:
                return 1
    return 1


def calculate_error(my_tree, data_list):
    num = 0
    for data in data_list:
        num += is_error(my_tree, data)
    return num / len(data_list)


# main
set_index_value()
training_examples = get_data("features files/training_examples.txt")
validations_examples = get_data("features files/test_examples.txt")

# TODO features name list
features_list = []

# TODO add possiblities for each feature
# possiblities_list = ['y', 'n', 'u']
possiblities_list = ['0', '1']
# possibilities_list = {'features': ['1', '2']}

# TODO add list of labels
# labels_list = ['republican.', 'democrat.', 'other.']
labels_list = ['austen', 'bronte', 'melville', 'verne']

features_num = len(training_examples[0]) - 1
# all_features = {k for k in range(16)}
all_features = {k for k in range(1)}

train = []
validation = []

# TODO for height
# for i in range(features_num + 1):
for i in range(features_num, features_num + 1):
    j = 0
    features_copy = all_features.copy()
    my_tree = build_tree(training_examples, features_copy, 1, None, possiblities_list, i)
    # train_error = calculate_error(my_tree, training_examples)
    # validation_error = calculate_error(my_tree, validations_examples)
    # train.append(train_error)
    # validation.append(validation_error)
    print("height = " + str(i))
    if my_tree is not None:
        if isinstance(my_tree, Tree):
            my_tree.show()

# plotting graph
# xvalue = np.arange(0, 17, 1)
# plt.plot(xvalue, train, label="train")
# plt.plot(xvalue, validation, label="validation")
# plt.ylim(0, 0.4)
# plt.legend()
# plt.show()

