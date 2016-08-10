# Name: Praneet Jain
# Task: Election prediction

import csv
import os
import time

def read_csv(path):
    """
    Reads the CSV file at path, and returns a list of rows. Each row is a
    dictionary that maps a column name to a value in that column, as a string.
    """
    output = []
    for row in csv.DictReader(open(path)):
        output.append(row)
    return output


################################################################################
# Problem 1: State edges
################################################################################

def row_to_edge(row):
    """
    Given an election result row or poll data row, returns the Democratic edge
    in that state.
    """
    return float(row["Dem"]) - float(row["Rep"])  

def state_edges(election_result_rows):
    """
    Given a list of election result rows, returns state edges.
    The input list does has no duplicate states;
    that is, each state is represented at most once in the input list.
    """
    #TODO: Implement this function
    
    dictionary = {}
    for row in election_result_rows:
        dictionary [row['State']] = row_to_edge(row)
        
    return dictionary
    pass


################################################################################
# Problem 2: Find the most recent poll row
################################################################################

def earlier_date(date1, date2):
    """
    Given two dates as strings (formatted like "Oct 06 2012"), returns True if 
    date1 is after date2.
    """
    return (time.strptime(date1, "%b %d %Y") < time.strptime(date2, "%b %d %Y"))

def most_recent_poll_row(poll_rows, pollster, state):
    """
    Given a list of poll data rows, returns the most recent row with the
    specified pollster and state. If no such row exists, returns None.
    """
    mrpr={}
    for item in poll_rows:
        if (item["State"] in state and item["Pollster"] in pollster):
            if mrpr:
                if earlier_date(mrpr["Date"], item["Date"]):
                    mrpr = item
            else:
                mrpr = item
                
    if mrpr:
        return mrpr
    else: 
        return None 





################################################################################
# Problem 3: Pollster predictions
################################################################################


def unique_column_values(rows, column_name):
    """
    Given a list of rows and the name of a column (a string), returns a set
    containing all values in that column.
    """
    u=[]
    for item in rows:
        u.append(item[column_name])
        ucv = set(u)
    return ucv 

class nesteddict(dict):
    def __getitem__(self,item):
        try:
            return dict.__getitem__(self,item)
        except KeyError:
            value = self[item] = type(self)()
            return value

def pollster_predictions(poll_rows):
    """
    Given a list of poll data rows, returns pollster predictions.
    """
    pp=nesteddict()
    s={}
    for state in unique_column_values(poll_rows,"State"):
        for pollster in unique_column_values(poll_rows,"Pollster"):
            s = most_recent_poll_row(poll_rows, pollster, state)
            if s:
                key = pollster
                key1 = state 
                pp[key][key1]=row_to_edge(s)
    return pp    




            
################################################################################
# Problem 4: Pollster errors
################################################################################

def average_error(state_edges_predicted, state_edges_actual):
    """
    Given predicted state edges and actual state edges, returns
    the average error of the prediction.
    """
    #TODO: Implement this function
    sums=0.0
    length=0
    first=0.0
    second=0.0
    final=0.0
    if len(state_edges_predicted) >= len(state_edges_actual):
        length = len(state_edges_actual)
    else:
        length = len(state_edges_predicted)
    for i in range(-1,length-1):
        first = state_edges_actual.values()[i]
        second = state_edges_predicted.values()[i]
        final = abs(first - second)
        sums=sums+final
    avg = sums*1.0/length
    return avg
    
def pollster_errors(pollster_predictions, state_edges_actual):
    """
    Given pollster predictions and actual state edges, retuns pollster errors.
    """
    #TODO: Implement this function
    dictionary={}
    for key,value in pollster_predictions.items():
        avj=0.0
        sums=0.0
        count=0
        for key_key,key_value in value.items():
            first=key_value
            length=len(state_edges_actual)
            for keyss in range(0,length):
                temp = state_edges_actual.keys()[keyss]
                if temp==key_key:
                   temp_val=state_edges_actual.values()[keyss]
                   diff=abs(key_value-temp_val)
                   sums=sums+diff
                   count=count+1
            avj = sums/count
            dictionary[key]=avj
    return dictionary


################################################################################
# Problem 5: Pivot a nested dictionary
################################################################################

def pivot_nested_dict(nested_dict):
    """
    Pivots a nested dictionary, producing a different nested dictionary
    containing the same values.
    The input is a dictionary d1 that maps from keys k1 to dictionaries d2,
    where d2 maps from keys k2 to values v.
    The output is a dictionary d3 that maps from keys k2 to dictionaries d4,
    where d4 maps from keys k1 to values v.
    For example:
      input = { "a" : { "x": 1, "y": 2 },
                "b" : { "x": 3, "z": 4 } }
      output = {'y': {'a': 2},
                'x': {'a': 1, 'b': 3},
                'z': {'b': 4} }
    """
     #TODO: Implement this function
    dictionary={}
    for key,value in nested_dict.items():
        for key2,value2 in value.items():
            dictionary_temp={}
            dictionary_temp[key]=value2
            if key2 in dictionary:
                dictionary[key2].update(dictionary_temp)
            else:
                dictionary[key2]=dictionary_temp
    return dictionary


################################################################################
# Problem 6: Average the edges in a single state
################################################################################

def average_error_to_weight(error):
    """
    Given the average error of a pollster, returns that pollster's weight.
    The error must be a positive number.
    """
    return error ** (-2)

# The default average error of a pollster who did no polling in the
# previous election.
DEFAULT_AVERAGE_ERROR = 5.0

def pollster_to_weight(pollster, pollster_errors):
    """"
    Given a pollster and a pollster errors, return the given pollster's weight.
    """
    if pollster not in pollster_errors:
        weight = average_error_to_weight(DEFAULT_AVERAGE_ERROR)
    else:
        weight = average_error_to_weight(pollster_errors[pollster])
    return weight


def weighted_average(items, weights):
    """
    Returns the weighted average of a list of items.
    
    Arguments:
    items is a list of numbers.
    weights is a list of numbers, whose sum is nonzero.
    
    Each weight in weights corresponds to the item in items at the same index.
    items and weights must be the same length.
    """
    assert len(items) > 0
    assert len(items) == len(weights)
    #TODO: Implement this function
    sums=0.0
    for i in range(len(items)):
        val_item=items[i]
        val_weight=weights[i]
        mult=val_item*val_weight
        sums=sums+mult
    total=sums/sum(weights)
    return total


def average_edge(pollster_edges, pollster_errors):
    """
    Given pollster edges and pollster errors, returns the average of these edges
    weighted by their respective pollster errors.
    """
    #TODO: Implement this function
    s = []
    ae = 0
    for key in pollster_edges.keys() and pollster_edges.keys():
        s.append(pollster_to_weight(key,pollster_errors))   
    ae = weighted_average(pollster_edges.values(),s)
    return ae
    
    
################################################################################
# Problem 7: Predict the 2012 election
################################################################################

def predict_state_edges(pollster_predictions, pollster_errors):
    """
    Given pollster predictions from a current election and pollster errors from
    a past election, returns the predicted state edges of the current election.
    """
    #TODO: Implement this function
    predict_state_edge_dict = {}
    pivot_pollster_predictions = pivot_nested_dict(pollster_predictions)
    for state in pivot_pollster_predictions:
        predict_state_edge_dict[state] = average_edge(pivot_pollster_predictions[state], pollster_errors)
    return predict_state_edge_dict
  
    

################################################################################
# Electoral College, Main Function, etc.
################################################################################

def electoral_college_outcome(ec_rows, state_edges):
    """
    Given electoral college rows and state edges, returns the outcome of
    the Electoral College, as a map from "Dem" or "Rep" to a number of
    electoral votes won.  If a state has an edge of exactly 0.0, its votes
    are evenly divided between both parties.
    """
    ec_votes = {}               # maps from state to number of electoral votes
    for row in ec_rows:
        ec_votes[row["State"]] = float(row["Electors"])

    outcome = {"Dem": 0, "Rep": 0}
    for state in state_edges:
        votes = ec_votes[state]
        if state_edges[state] > 0:
            outcome["Dem"] += votes
        elif state_edges[state] < 0:
            outcome["Rep"] += votes
        else:
            outcome["Dem"] += votes/2.0
            outcome["Rep"] += votes/2.0
    return outcome


def print_dict(dictionary):
    """
    Given a dictionary, prints its contents in sorted order by key.
    Rounds float values to 8 decimal places.
    """
    for key in sorted(dictionary.keys()):
        value = dictionary[key]
        if type(value) == float:
            value = round(value, 8)
        print key, value


def main():
    """
    Main function, which is executed when election.py is run as a Python script.
    """
    # Read state edges from the 2008 election
    edges_2008 = state_edges(read_csv("data/2008-results.csv"))
    
    # Read pollster predictions from the 2008 and 2012 election
    polls_2008 = pollster_predictions(read_csv("data/2008-polls.csv"))
    polls_2012 = pollster_predictions(read_csv("data/2012-polls.csv"))
    
    # Compute pollster errors for the 2008 election
    error_2008 = pollster_errors(polls_2008, edges_2008)
    
    # Predict the 2012 state edges
    prediction_2012 = predict_state_edges(polls_2012, error_2008)
    
    # Obtain the 2012 Electoral College outcome
    ec_2012 = electoral_college_outcome(read_csv("data/2012-electoral-college.csv"),
                                        prediction_2012)
    
    print "Predicted 2012 election results:"
    print_dict(prediction_2012)
    print
    
    print "Predicted 2012 Electoral College outcome:"
    print_dict(ec_2012)
    print    


# If this file, election.py, is run as a Python script (such as by typing
# "python election.py" at the command shell), then run the main() function.
if __name__ == "__main__":
    main()