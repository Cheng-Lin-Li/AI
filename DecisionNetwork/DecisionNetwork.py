#!/usr/bin/env python
# encoding: utf-8
'''
Decision Network with Decision Nodes, Chance Nodes, and Utility Nodes -- An implementation to get probability of Decision node, or Utility Nodes.

The implementation of decision network (Chapter 16, AIMA) uses a Directed Acyclic Graph (DAG) to represent a set of random variables and 
their conditional dependencies within a probabilistic model, while a decision network extends the Bayesian network to include decision nodes and utility nodes.
    
All nodes can have only two values, “+” (True) or “−” (False).
Only one utility node will be considered in this implementation.

This implementation will base on input to generate:
    1)    Calculate a specific joint, marginal, or conditional probability.
    2)    Calculate the expected utility of a particular decision, or determine the decision with the maximum expected utility. 
    
It defines classes_and_methods below:

Decision_Network: A decision network class with decision nodes, chance nodes and utility nodes.
    Operators include: 
    1. xxx
    2. xxx
    
    Major Functions:***

    
Decision_node: A decision node includes name, value(True or False), expected utility (EU), Probability of maximum expected utility (MEU).
    Data structure:
        D(('Decision name', value):(('Parent node name', Parent node value), probability))    
    Major Functions:***
      
    
Chance_node / Variable: A chance node includes name, value(True or False), Parent values, Probability.
    Data structure:
        C(
            ('Chance name', value):({'Parent1 node name':Parent1 node value, 'Parent2 node name':Parent2 node value,...}, probability), 
            ...
        )
    Major Functions:***

    
Utility_node: A utility node includes name='Utility', utility values, parent name, parent values
    Data structure:
        U('Utility name':(('Parent node name', Parent node value), utility value))
    Major Functions:***



Probability_Distribution:
    A discrete probability distribution. 
    Assign the variable as name of the probability distribution, then assign and query probability of values.
    Data Structure:
        Probability distribution name: String.
        Probability table: {True/Value1: Prob1, False/Value2: Prob2, ...]
    
    Major method:
        __init__ (Variable name)
        set_prob(Probability_table)
        get_prob(Value)
        normalized()

Conditional_probability_table:
    Data Structure:
        Conditional Probability Table (CPT): 
                        {'Value1/True':{ tuple(Parent nodes):
                                          {
                                            (Parent1 value1, parent2 value1, ...):Prob1, 
                                            (Parent1 value1, parent2 value2, ...):Prob2, ...
                                          }
                                        },
                        'value2/False': {...}}
        With no parents, Conditional Probability Table (CPT): 
                        {True:{(): {(): Prob1}, 
                         False:{(): {(): Prob2}}}).
            mapping = {():Prob}

Variable:
    Data Structure:
        Variable name: String.
        Value: [True, False]
        Parent nodes: [parent1 name, parent2 name, ...] or None if no parent node.
        Conditional Probability Table (CPT): 
                        {'Value1/True':{ tuple(Parent nodes):
                                          {
                                            (Parent1 value1, parent2 value1, ...):Prob1, 
                                            (Parent1 value1, parent2 value2, ...):Prob2, ...
                                          }
                                        },
                        'value2/False': {...}}
                        
Bayes_network:
    Data Structure:
        Bayes_network [Variable1, Variable2, ....]

enumeration_ask
    Inference by enumeration.
    Reference by AIMA code repository

enumeration_all
    Inference by enumeration.
    Reference by AIMA code repository
    

Query_list:
    A list which store query string.
    
    
@author: Cheng-Lin Li a.k.a. Clark Li

@copyright:    2017 Cheng-Lin Li@University of Southern California. All rights reserved.

@license:    Licensed under the GNU v3.0. https://www.gnu.org/licenses/gpl.html

@contact:    chenglil@usc.edu
@version:    1.0

@create:    April, 16, 2017
@updated:   April, 16, 2017
'''

from __future__ import print_function 
from __future__ import division
import sys
import copy
import random
import collections
import itertools
from datetime import datetime

__all__ = []
__version__ = 0.1
__date__ = '2017-04-16'
__updated__ = '2017-04-16'

DEBUG = 1
PRINT_TIME = False
INPUT_FILE = 'input01.txt'
#OUTPUT_FILE = 'output.txt' # OUTPUT_FILE COULD BE 'OUTPUT_FILE = None' for console or file name (e.g. 'OUTPUT_FILE = 'output.txt') for file.'
OUTPUT_FILE = None # OUTPUT_FILE COULD BE 'OUTPUT_FILE = None' for console or file name (e.g. 'OUTPUT_FILE = 'output.txt') for file.'
INPUT_SPLITTER = ' ' #the splitter for input data.
NETWORK_DELIMITER = '***'
QUERY_DELIMITER = '******' #the separator for query string and Bayes network
TRUE = '+'
FALSE = '-'
VALUE_DOMAIN = [True, False] #Values in this assignment only includes True and False.
EQUATION_SYMBOL = tuple(['(', '|', ')', '='])
PARENT = '|'
DECISION = 'decision'
UTILITY = 'utility'
MINOR_NUMBER = 1e-09
      
def setOutputData(filename='', result_list=list()):
#
# output results. 
#
    try:
        if filename != None :
            orig_stdout = sys.stdout
            f = file(filename, 'w')
            sys.stdout = f
        else:
            pass
##########               
        for _r in result_list:
            # print guest and table number.
            print('%.2f'%(_r+MINOR_NUMBER))          
###########
        sys.stdout.flush()       
        if filename != None :
            sys.stdout = orig_stdout                   
            f.close()
        else:
            pass        
    except IOError as _err:
        if (DEBUG == True): 
            print ('File error: ' + str (_err))
        else :
            pass
        exit()

def decision_ask(X, e, bn):
    '''
    Compute bn's P(X, Y, Z), P(X, Y|e)
    '''
    if e == dict():
        get_join_probability(X, bn)
    else:
        return elimination_ask(X, e, bn)


def get_join_probability(X, bn):    
    factors = list()
    prob_list = list()
    parent_list = list()
    event = dict()
    prob = 1.0
    
    X_list = [_x for _x in X.items()]
          
    for _x in X_list: #Get query variable one by one
        _value = X[_x]        
        if _value != None:     
            parent_tuple = bn.lookup[X].parents
            _variable = bn.get_variable(_x)
            if len(parent_tuple) == 0: #No parents for this variable node
                prob *= _variable.p(_value, tuple())
            else:
                for _parent in parent_tuple: # checking every parent variables and their values
                    for _qvar in X:
                        if _parent == _qvar: # if parent variable in query variable.
                            event[_parent] = X[_qvar]
                        else:   #We have to calculate the probability of the parent node in all value domain.
                            
            for parent in parent_tuple: 
                prob *= 
                    if _evd != _x:
                        _evidents[_evd] = X[_evd]
                    else: break;
        else:
            pass # Probability = 1 for all P(x)                    
    return prob
                            
def elimination_ask(X, e, bn):
    '''Compute bn's P(X|e) by variable elimination. [Figure 14.11]
    >>> elimination_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary)
    node = variables
    variable = name
    '''
#    assert X not in e, "Query variable must be distinct from evidence"
    factors = list()
    prob_list = list()
    prob = 1.0
    _evidents = e
#     od = collections.OrderedDict(sorted(X.items()))
#     X_list = [_x for _x in od.keys()]
    X_list = [_x for _x in X.items()]
    for _X in X_list:
        for var in reversed(bn.variables):
            factors.append(make_factor(var.name, _evidents, bn))
            #Is var.name a hidden variable when querying P(X|e)?
            if var.name !=_X and var.name not in _evidents and var.name != UTILITY:
                factors = sum_out(var.name, factors, bn)
        prob_list.append( pointwise_product(factors, bn).normalize())                
        prob *= pointwise_product(factors, bn).normalize()[X[_x]]

    return prob

# def is_hidden(var, X, e):
#     """Is var a hidden variable when querying P(X|e)?"""
#     return var != X and var not in e and var != UTILITY


def make_factor(var, e, bn):
    '''
    Return the factor for var in bn's joint distribution given e.
    That is, bn's full joint distribution, projected to accord with e,
    is the pointwise product of these factors for bn's variables.
    e=dict(JohnCalls=T, MaryCalls=T)
    '''
    _query_variable = bn.get_variable(var)
    _search_variables = [var] + list(_query_variable.parents)
    _factor_variables = list()
    _cpt = dict()
    _evidents = e
    for _x in _search_variables:
        if _x not in _evidents:
            _factor_variables.append(_x) #Hidden variables
    for _e1 in all_events(_factor_variables, bn, _evidents):
        _cpt[event_values(_e1, _factor_variables)] = _query_variable.p(_e1[var], _e1)

    return Factor(_factor_variables, _cpt)

def event_values(event, variables):
    """Return a tuple of the values of variables in event.
    >>> event_values ({'A': 10, 'B': 9, 'C': 8}, ['C', 'A'])
    (8, 10)
    >>> event_values ((1, 2), ['C', 'A'])
    (1, 2)
    event = {'C':True, 'B':True}
    variables = ('B',)
    """
    if isinstance(event, tuple) and len(event) == len(variables):
        return event
    else:
        return tuple([event[var] for var in variables])
    
def all_events(variables, bn, e):
    """Yield every way of extending e with values for all variables."""
    if not variables:
        yield e
    else:
        X, rest = variables[0], variables[1:]
        for e1 in all_events(rest, bn, e):
            for x in bn.get_values(X):
                yield extend(e1, X, x)

def extend(s, var, val):
    """Copy the substitution s and extend it by setting var to val; return copy."""
    s2 = s.copy()
    s2[var] = val
    return s2
    
def pointwise_product(factors, bn):
    return reduce(lambda f, g: f.pointwise_product(g, bn), factors)

def sum_out(var, factors, bn):
    """Eliminate var from all factors by summing over its values."""
    result = list()
    var_factors = list()
    for f in factors:
        (var_factors if var in f.variables else result).append(f)
    result.append(pointwise_product(var_factors, bn).sum_out(var, bn))
    return result

class Factor (object):
    """A factor in a joint distribution."""

    def __init__(self, variables, cpt):
        self.variables = variables
        self.cpt = cpt

    def pointwise_product(self, other, bn):
        """Multiply two factors, combining their variables."""
        variables = list(set(self.variables) | set(other.variables))
        cpt = {event_values(e, variables): self.p(e) * other.p(e)
               for e in all_events(variables, bn, {})}
        return Factor(variables, cpt)

    def sum_out(self, var, bn):
        """Make a factor eliminating var by summing over its values."""
        variables = [X for X in self.variables if X != var]
        cpt = {event_values(e, variables): sum(self.p(extend(e, var, val))
                                               for val in bn.get_values(var))
               for e in all_events(variables, bn, {})}
        return Factor(variables, cpt)

    def normalize(self):
        '''
        Return my probabilities; must be down to one variable.
        '''
        assert len(self.variables) == 1
        return ProbDist(self.variables[0],
                        {k: v for ((k,), v) in self.cpt.items()})

    def p(self, e):
        """Look up my value tabulated for e."""
        return self.cpt[event_values(e, self.variables)]

class ProbDist:
    '''
    A discrete probability distribution. You name the random variable
    in the constructor, then assign and query probability of values.
    >>> P = ProbDist('Flip'); P['H'], P['T'] = 0.25, 0.75; P['H']
    0.25
    >>> P = ProbDist('X', {'lo': 125, 'med': 375, 'hi': 500})
    >>> P['lo'], P['med'], P['hi']
    (0.125, 0.375, 0.5)
    '''

    def __init__(self, varname=None, freqs=None):
        """If freqs is given, it is a dictionary of values - frequency pairs,
        then ProbDist is normalized."""
        self.prob = dict()
        self.varname = varname
        self.values = list()
        if freqs:
            for (v, p) in freqs.items():
                self[v] = p
            self.normalize()

    def __getitem__(self, val):
        """Given a value, return P(value)."""
        try:
            return self.prob[val]
        except KeyError:
            return 0
 
    def __setitem__(self, val, p):
        """Set P(val) = p."""
        if val not in self.values:
            self.values.append(val)
        self.prob[val] = p

    def normalize(self):
        """Make sure the probabilities of all values sum to 1.
        Returns the normalized distribution.
        Raises a ZeroDivisionError if the sum of the values is 0."""
        total = sum(self.prob.values())
        if abs(total - 1.0) > MINOR_NUMBER:
            for val in self.prob:
                self.prob[val] /= total
        return self

#     def show_approx(self, numfmt='{:.3g}'):
#         """Show the probabilities rounded and sorted by key, for the
#         sake of portable doctests."""
#         return ', '.join([('{}: ' + numfmt).format(v, p)
#                           for (v, p) in sorted(self.prob.items())])

                   
class Bayesian_network(object):
    "Bayesian network: a graph of variables connected by parent links."
     
    def __init__(self): 
        self.variables = list() # List of variables, in parent-first topological sort order
        self.lookup = dict()    # Mapping of {variable_name: variable} pairs
        self.nodes = list()
            
    def add(self, name, value, parentnames, cpt, value_domain=VALUE_DOMAIN):
        "Add a new Variable to the BayesNet. Parentnames must have been added previously."
        parents = [_p_name for _p_name in parentnames]
        var = Variable(name, value, cpt, tuple(parents), value_domain)
        self.variables.append(var)
        self.lookup[name] = var
        self.value_domain = value_domain
        return self
    def get_variable(self, var_name):
        '''
        Return the variable for the variable named var_name.
        '''
        for _v in self.variables:
            if _v.name == var_name:
                return _v
        raise Exception('No such variable: %s'%(str(var_name)))
    def get_values(self, variable):
        '''
        return all value domains
        '''
        return self.value_domain    
        
class Variable(object):
    '''A discrete random variable; conditional on zero or more parent Variables.
    Data Structure:
        Variable name: String.
        Value: [True, False]        
        Parent nodes: [parent1 name, parent2 name, ...] or None if no parent node.
        Conditional Probability Table (CPT) list: 
                        [{'Value1' or True:{ tuple(Parent nodes):
                                          {
                                            (Parent1 value1, parent2 value1, ...):Prob1, 
                                            (Parent1 value1, parent2 value2, ...):Prob2, ...
                                          }
                                        },
                        {'value2' or False: {...}}]   
        With no parents, Conditional Probability Table (CPT) list: 
                        [{True:{(): {(): Prob1}}, 
                         {False:{(): {(): Prob2}}].
            mapping = {():Prob}    
    '''
    def __init__(self, name, value, cpt=dict(), parents=(), value_domain=VALUE_DOMAIN):
        '''A variable has a name, list of parent variables, and a Conditional Probability Table.
        '''
        
        self.name = name
        self.value = value
        self.parents = parents
        self.cpt=Conditional_probability_table()
        self.cpt.add(value, parents, cpt)
        self.value_domain = value_domain
        if name != UTILITY: self.get_negative_prob(value_domain)
        
#         self.domain   = set(itertools.chain(*self.cpt.values())) # All the outcomes in the CPT
        
    def get_negative_prob(self, value_domain=VALUE_DOMAIN):
        _mapping = dict()
        _value = None
        _cpt = self.cpt.get()
        if len(_cpt) + 1 == len(value_domain): # Only missing last value, calculate 1-P for last value.
            # Sum up current probabilities
            for _val in value_domain:
                if tuple([_val]) in _cpt and _mapping == dict():
                    _mapping = copy.deepcopy(_cpt[tuple([_val])]) #Copy one of CPT value as template
                elif tuple([_val]) in _cpt and _mapping != dict(): #Calculate the sum of probabilities.
                    for (_row, _dist) in _cpt[tuple([_val])][0].items(): #_dict={(parent1 value, parent2 value):Prob1, ...}}
                        _mapping[0][0][_row] += _dist
                else:
                    _value = _val
                    
            # Calculate probability for last value:
            for (_row, _dist) in _mapping.items(): #_mapping={(parents):{(parent1 value, parent2 value):Prob1, ...}}
                for (_r, _p) in _dist.items():
                    _mapping[_row][_r] = 1- _p
            _cpt[tuple([_value])]= _mapping
            self.cpt = _cpt
        else:
            pass                
    def get_values(self):
        '''
        return all value domains
        '''
        return self.value_domain
        
    def p(self, value, event):
        '''
        Return the conditional probability
        P(X=value | parents=parent_values), where parent_values
        are the values of parents in event. (event must assign each
        parent a value.)
        >>> bn = BayesNode('X', 'Burglary', {T: 0.2, F: 0.625})
        >>> bn.p(False, {'Burglary': False, 'Earthquake': True})
        0.375
        Conditional Probability Table (CPT) list: 
                        [{('Value1') or (True,):{ tuple(Parent nodes):
                                          {
                                            (Parent1 value1, parent2 value1, ...):Prob1, 
                                            (Parent1 value1, parent2 value2, ...):Prob2, ...
                                          }
                                        },
                        {('value2',) or (False,): {...}}]   
        With no parents, Conditional Probability Table (CPT) list: 
                        [{(True,):{(): {(): Prob1}}, 
                         {(False,):{(): {(): Prob2}}].
            mapping = {():Prob}         
        '''
        assert isinstance(value, bool)
        if isinstance(self.cpt, Conditional_probability_table):
            _cpt = self.cpt.get()
        else:
            _cpt = self.cpt
        try:
            _p = _cpt[tuple([value])][self.parents][event_values(event, self.parents)]
        except KeyError:
            _p = 1-_p
        return _p
        
class Conditional_probability_table(object):
    '''A mapping of where each row is a dictionary value of the parent variables.
        Conditional Probability Table (CPT): 
                        {'Value2' or True:{ tuple(Parent nodes):
                                          {
                                            (Parent1 value1, parent2 value1, ...):Prob1, 
                                            (Parent1 value1, parent2 value2, ...):Prob2, ...
                                          }
                                        },
                        'Value2' or False: {...}
                        }       
        With no parents, Conditional Probability Table (CPT): 
                        {True:{(): {(): Prob1}},
                        False: {...}}.
            mapping = {():Prob}
    '''
    def __init__(self):
        self.cpt = dict()

    def add(self, value, parents=(), mapping=dict()):
        if len(parents) == 0 and isinstance(mapping, dict): # No parent
            self.cpt[tuple([value])] = {(): mapping}
        else:
            self.cpt[tuple([value])] = {tuple(parents):mapping}
    def get(self):
        return self.cpt     

def getInputData(filename):
#
# Get data from input file. 
#  Leverage two dimension array data structure to store data for each line.
    _query = list()
    _var_name = None
    _parent_names = list()
    _is_Query = True
    _is_Network = False
    _is_Utility = False
    _is_Var = False
    _prob = 0.0
    _parent_values = list()
    _map_dict = dict()
    _bn = Bayesian_network()
    
    try:
        with open(filename, 'r') as _fp:
            for _each_line in _fp:
                _each_line =_each_line.strip()
                _row = _each_line.strip().split(INPUT_SPLITTER)
                if _each_line != QUERY_DELIMITER and _is_Query == True:
                    #Get query string
                    _query.append(_each_line)
                elif _each_line == QUERY_DELIMITER and _is_Query == True :
                    #Switch to Bayes Network section
                    _is_Query = False
                    _is_Network = True
                    _is_Var = True
                elif _each_line != QUERY_DELIMITER and _each_line != NETWORK_DELIMITER and (_is_Network == True or _is_Utility == True):
                    #Construct variable and Bayesian Network
                    if _is_Var == True: # Construct variable
                        _parent_names = list()
                        for _i in range(len(_row)):
                            if _is_Var == True and _row[_i] != PARENT:
                                _var_name= _row[_i]
                            elif _row[_i] == PARENT :
                                _is_Var = False
                                _is_parent = True
                            elif _is_parent == True and _row[_i] != PARENT :
                                _parent_names.append(_row[_i])
                            else:
                                pass                   
                        _is_Var = False
                        _map_dict = dict()
                    else: # Construct CPT dictionary
                        _prob = 0.0
                        _parent_values = list()                        
                        if _each_line == DECISION: # If the node is decision node.
                            _prob = 1/len(VALUE_DOMAIN)
                        else:
                            for _i in range(len(_row)): # Parser parent values and probability
                                if _i == 0:
                                    _prob = float(_row[_i])
                                else:
                                    if _row[_i] == TRUE:
                                        _parent_values.append(True)
                                    elif _row[_i] == FALSE:
                                        _parent_values.append(False)
                                    
                        _map_dict[tuple(_parent_values)] = _prob
                elif (_each_line == NETWORK_DELIMITER or  _each_line == QUERY_DELIMITER) and _is_Network == True:
                    # Another new node
                    _is_Network = True
                    _is_Var = True
                    
                    
                    _bn.add(_var_name, True ,tuple(_parent_names), _map_dict)
                                       
                elif _each_line == QUERY_DELIMITER and _is_Network == True:
                    #switch to Decision network
                    _is_Query = False
                    _is_Network = False
                    _is_Utility = True
                    _is_Var = True
                else:
                    pass    
            
            _bn.add(_var_name, True ,tuple(_parent_names), _map_dict)
        _fp.close()
        return _query, _bn
    except IOError as _err:
        if (DEBUG): 
            print ('File error: ' + str (_err))
        else :
            pass
        exit()

def ask(query, bn):
    _result = None
    _query_type = None
    _variables = dict()
    _name = None
    _evidents = dict()
    _ename = None
    _is_Var = True
    _is_Value = False
    _is_Evident = False
    _is_Evident_value = False
    
    _qt = query.strip().split('(')
    _query_type = _qt[0]

    for _item in _qt[1].strip().split(INPUT_SPLITTER):
        if _is_Var == True and (_item != '=' and _item != PARENT):
            _name = _item.replace(',','').replace(')', '')
            if _query_type == 'MEU':
                _variables[_name] = None
            else:
                _is_Var = False
                _is_Value = True
        elif _is_Value == True and (_item != '=' and _item != PARENT):
            if _item.replace(',', '').replace(')', '') == TRUE:
                _variables[_name] = True
            else:
                _variables[_name] = False
            _is_Var = True
            _is_Value = False
        elif _is_Var == True and _item == '=':
            _is_Var = False
            _is_Value = True
        elif _item == PARENT:
            _is_Var = False
            _is_Value = False
            _is_Evident = True            
            _is_Evident_value = False
        elif _is_Evident == True and _item != '=':
            _ename = _item
            _is_Evident = False
            _is_Evident_value = True
        elif _is_Evident_value == True and _item != '=':
            if _item.replace(',', '').replace(')', '') == TRUE:
                _evidents[_ename]=True
            else:
                _evidents[_ename]=False
            _is_Evident = True
            _is_Evident_value = False
        else:
            pass    

    if  DEBUG: print('query_type=%s, variable=%s, _evidents=%s'%(_query_type, _variables, _evidents))
                
    if _query_type =='P':
        #Caculate probability
        if DEBUG: print('elimination_ask(_variables, _evidents, bn)=%s, %s, %s'%(str(_variables), str(_evidents), str(bn)))
        return elimination_ask(_variables, _evidents, bn)
#        enumerate_all(_variables, _evidents, bn)
    elif _query_type == 'EU':
        #Caculate EU
        pass
    elif _query_type == 'MEU':
        #Caculate MEU
        pass
    else:
        pass
    
    
    return _result

if __name__ == "__main__":

    '''
        Main program.
            Construct Decision Network class with input data.
            Then input query string into the ask the network to get the answer.
    '''
    #program_name = sys.argv[0]
    #input_file = sys.argv[1]
    input_file = INPUT_FILE
    _result_list = []
    
    query, bn = getInputData(input_file)
    if DEBUG : print('query=%s, bn=%s'%(str(query), str(bn)))
    for _q in query:
        _result_list.append(ask(_q, bn))
    pass
    setOutputData(OUTPUT_FILE, _result_list)
    
    