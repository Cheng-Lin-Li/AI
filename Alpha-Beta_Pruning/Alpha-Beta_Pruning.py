#!/usr/bin/env python
# encoding: utf-8
'''
Game Algorithm Name: Alpha-Beta Search Algorithm

@author: Cheng-Lin Li a.k.a. Clark Li

@copyright:    2017 Cheng-Lin Li@University of Southern California. All rights reserved.

@license:    Licensed under the GNU v3.0. https://www.gnu.org/licenses/gpl.html

@contact:    chenglil@usc.edu
@version:    1.0

@create:    February, 4, 2017
@updated:   February, 6, 2017
'''
from __future__ import print_function 
import sys
import copy

__all__ = []
__version__ = 1.0
__date__ = '2017-02-04'
__updated__ = '2017-02-06'

DEBUG = False
INPUT_FILE = 'input.txt'
#OUTPUT_FILE = 'output.txt' # OUTPUT_FILE COULD BE 'OUTPUT_FILE = None' for console or file name (e.g. 'OUTPUT_FILE = 'output.txt') for file.'
OUTPUT_FILE = None # OUTPUT_FILE COULD BE 'OUTPUT_FILE = None' for console or file name (e.g. 'OUTPUT_FILE = 'output.txt') for file.'
POSITIVE_INFINITE = float('inf')
NEGATIVE_INFINITE = float('-inf')
NUMBER2ALPHABET = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h' }

# Define a MXN weighting matrix for evaluation function.
WEIGHT_MATRIX = [
                [99, -8, 8, 6, 6, 8, -8,99],
                [-8,-24,-4,-3,-3,-4,-24,-8],
                [ 8, -4, 7, 4, 4, 7, -4, 8],
                [ 6, -3, 4, 0, 0, 4, -3, 6],
                [ 6, -3, 4, 0, 0, 4, -3, 6],
                [ 8, -4, 7, 4, 4, 7, -4, 8],
                [-8,-24,-4,-3,-3,-4,-24,-8],
                [99, -8, 8, 6, 6, 8, -8,99]
                ]
M = 8 # Define max. column number.
N = 8 # Define max. row number.
BLACK_SYMBLE = 'X'
WHITE_SYMBLE = 'O'
PASS2TERMINAL = 2 #Pass two times will terminal the game.

def getInputData(filename):
#
# Get data from input file. 
#  Leverage two dimension array data structure to store data for each cell.
#  For a MXN board.
#  M=N=8 in our case.
    _player = ""
    _depth = 0
    _row = []
    _status = []
    i = 0
    try:
        with open(filename, 'r') as _fp:
            for _each_line in _fp:
                if i == 0: #Player
                    _player = _each_line[0]
                    i += 1
                elif i == 1: #Depth
                    _depth = int(_each_line[0])
                    i += 1
                else: #Initial Status
                    _row = list(_each_line)
                    if len(_row) >= M:
                        _row = _row[:M]
                    _status.append(_row)
        _fp.close()
        return _player, _depth, _status
    except IOError as _err:
        if (DEBUG): 
            print ('File error: ' + str (_err))
        else :
            pass
        exit()
def setOutputData(filename, actions, next_state):
#
# Save data to output file. 
#
    try:
        if filename != None :
            orig_stdout = sys.stdout
            f = file(filename, 'w')
            sys.stdout = f
        else:
            pass
        
        for _row in next_state:
            for _item in _row:
                print(_item, end ='')
            print(end ='\n')                
        print ('Node,Depth,Value,Alpha,Beta')
        for action in actions:
            print ('%s,%d'%(action[0], int(action[1])), end='')
            if action[2] == float('inf') :
                print (',Infinity', end='')
            elif action[2] == float('-inf') :
                print (',-Infinity', end='')
            else:
                print (',%.0f'%(action[2]), end='')
                
            if action[3] == float('inf') :
                print (',Infinity', end='')
            elif action[3] == float('-inf') :
                print (',-Infinity', end='')
            else:
                print (',%.0f'%(action[3]), end='')
                
            if action[4] == float('inf') :
                print (',Infinity', end='\n')
            elif action[4] == float('-inf') :
                print (',-Infinity', end='\n')
            else:
                print (',%.0f'%(action[4]), end='\n')
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
        
                
#
# Main Class: Alpha-Beta Search Algorithm
#    Alpha-Beta Search Algorithm implementation.
#
        
class AlphaBetaSearch(object):
    '''
    This class implements the minimax value for given positions of the Reversi game, 
    using the Alpha-Beta pruning algorithm with positional weight evaluation functions.
    '''

    def __init__(self, initial_player="", depth=0, state=[[]]):
        '''
        Constructor
        '''
        self.depth_restriction = int(depth)
        self.state = state
        self.current_player = initial_player
        self.max_player = initial_player # Initial player is MAX, opponent is MIN.
        self.min_player = ""
        self.utility = 0        
        self.action = ""
        self.current_depth = 0
        self.output_actions = []
        self.pass_count = 0
        self.i = -1
        self.j = -1
        self.isTreeEnd = False
        self.isGoDown = True
        self.next_state = list() #[next_status]
        self.max_value = float('-inf')
        if initial_player == BLACK_SYMBLE :
            self.min_player = WHITE_SYMBLE
        else :
            self.min_player = BLACK_SYMBLE
            
        
    def executeSearch(self, state=[[]]):
        v = 0
        _action = (-1, -1, 0, 0)
        _state = [[]]
        if state != [[]]:
            _state = state
            self.state = state
        else:
            _state = self.state
        a = NEGATIVE_INFINITE
        b = POSITIVE_INFINITE
        
        v = self.getMaxValue(_state, a, b, 0)
        
        return v, self.next_state
        
    def getMaxValue (self, state, a, b, depth):
        # Get Max Value
        #         
        current_depth = depth        
        parent_coordinates = self.getCoordinates(self.i, self.j)
        actions = list()
        self.current_player = self.max_player
        self.isGoDown = True
        
        # Test Terminal conditions
        if self.getTerminalTest(state, current_depth) == True :
            self.isTreeEnd = True
            return self.getUtility(state)
        else:
            self.isTreeEnd = False

        initial_v = POSITIVE_INFINITE        
        v = NEGATIVE_INFINITE 
        actions = list(self.getActions(state))
        if (not actions and self.pass_count <= PASS2TERMINAL):   
            actions.append((-9, -9, ((0, 0))))        
        for _action in actions:
            self.output_actions.append([parent_coordinates, current_depth, v, a, b]) #go down
            self.current_player = self.max_player
            _i = _action[0]
            _j = _action[1]

            _v = self.getMinValue(self.setResult(state, _action), a, b, current_depth + 1)            
            v = max([v, _v])           
            if v >= b:
                if DEBUG == True: print('[v, a, b]= %f, %f, %f'%(v,a,b))   
                coordinates = self.getCoordinates(_i, _j)
                if (self.isGoDown):
                    if (self.isTreeEnd):   
                        self.output_actions.append([coordinates, current_depth + 1, _v, a, b]) #return value.
                        self.isGoDown = False 
                        self.isTreeEnd = False
                    else :
                        self.output_actions.append([coordinates, current_depth + 1, initial_v, a, b]) 
                else: 
                    pass                   
                self.output_actions.append([parent_coordinates, current_depth, v, a, b]) #Parent node           
                return v
            else:
                coordinates = self.getCoordinates(_i, _j)                
                if (self.isGoDown):
                    if (self.isTreeEnd):   
                        self.output_actions.append([coordinates, current_depth + 1, _v, a, b]) #return value.
                        a = max([a, v])
                        self.isGoDown = False 
                        self.isTreeEnd = False
                    else :
                        a = max([a, v])
                        self.output_actions.append([coordinates, current_depth + 1, initial_v, a, b])
                else:     
                    a = max([a, v])  
        self.output_actions.append([parent_coordinates, current_depth, v, a, b]) 
        if DEBUG == True: print('[v, a, b]= %f, %f, %f'%(v,a,b))   
        return v

    def getMinValue (self, state, a, b, depth):
        # Get Min Value
        # 
        current_depth = depth        
        parent_coordinates = self.getCoordinates(self.i, self.j)
        actions = list()
        self.current_player = self.min_player
        self.isGoDown = True
        if self.getTerminalTest(state, current_depth) == True :
            self.isTreeEnd = True
            if current_depth == 1: self.setNextState(self.getUtility(state), state) # New add code: Record down the best move            
            return self.getUtility(state)
        else:
            self.isTreeEnd = False
            
        initial_v = POSITIVE_INFINITE
        v = POSITIVE_INFINITE
        actions = list(self.getActions(state))
        if (not actions and self.pass_count <= PASS2TERMINAL):   
            actions.append((-9, -9, ((0, 0))))       
        for _action in actions:
            self.output_actions.append([parent_coordinates, current_depth, v, a, b]) #go down
            self.current_player = self.min_player 
            _i = _action[0]
            _j = _action[1]
        
            _v = self.getMaxValue(self.setResult(state, _action) , a, b, current_depth + 1)
            # Record down the best move
            if current_depth == 1: self.setNextState(_v, state)         
            v = min([v, _v])
            if v <= a:
                if DEBUG == True: print('[v, a, b]= %f, %f, %f'%(v,a,b))
                coordinates = self.getCoordinates(_i, _j)   
                if (self.isGoDown): 
                    if (self.isTreeEnd):   
                        self.output_actions.append([coordinates, current_depth + 1, _v, a, b]) #return value.
                        self.isGoDown = False 
                        self.isTreeEnd = False
                    else :
                        self.output_actions.append([coordinates, current_depth + 1, initial_v, a, b])
                else: 
                    pass           
                self.output_actions.append([parent_coordinates, current_depth, v, a, b]) #Parent node  
                return v
            else:
                coordinates = self.getCoordinates(_i, _j)
                if (self.isGoDown):  
                    if (self.isTreeEnd):   
                        self.output_actions.append([coordinates, current_depth + 1, _v, a, b]) #return value.
                        b = min([b, v])
                        self.isGoDown = False 
                        self.isTreeEnd = False
                    else :
                        b = min([b, v])
                        self.output_actions.append([coordinates, current_depth + 1, initial_v, a, b])
                else:     
                    b = min([b, v])               
        self.output_actions.append([parent_coordinates, current_depth, v, a, b]) #Parent node
        if DEBUG == True: print('[v, a, b]= %f, %f, %f'%(v,a,b))   
        return v

    def getUtility (self, state):
        # Based on weight matrix and current state to calculate utility
        #
        value = 0
        _max = 0
        _min = 0
        
        for i, row in enumerate(state):
            for j, cell in enumerate(row):
                if cell == self.min_player:
                    _min += WEIGHT_MATRIX[i][j]
                elif cell == self.max_player:
                    _max += WEIGHT_MATRIX[i][j]
                else:
                    pass
        value = _max - _min
        return value
        
    def getTerminalTest (self, state, current_depth):
        # Test Termination condition
        # Either tree depth reach the restriction or no more action can be considered.
        isTerminal = False
        
        if (self.depth_restriction <= current_depth):
            isTerminal = True
        elif (not self.getActions(state)): #empty list
            self.i = -9
            self.j = -9
            self.pass_count += 1
            if (self.pass_count > PASS2TERMINAL):
                isTerminal = True
            else:
                pass
        else:
            self.pass_count = 0

        return isTerminal
        
    def setResult (self, state, action):
        # Based on action to transfer current state to next state.
        # action = (i, j, increase_i, increase_j)
        next_state = copy.deepcopy(state) #create a new state
        player = ""
        player = self.current_player
        if (player == BLACK_SYMBLE) :
            opponent = WHITE_SYMBLE
        else :
            opponent = BLACK_SYMBLE        
        i = action[0]
        j = action[1]
        self.i = i
        self.j = j

        if (self.i == -9 and self.j == -9):
            return next_state
        else :
            pass
        # Place piece
        next_state[i][j] = player
                            
        for _direction in action[2]:
            increase_i = _direction[0]
            increase_j = _direction[1]
            x = 0
            y = 0
            row_bound = 0
            column_bound = 0
            
            if increase_i > 0: row_bound = M
            elif increase_i < 0: row_bound = -1
            else: row_bound = i + 1
                
            if increase_j > 0: column_bound = N
            elif increase_j < 0: column_bound = -1
            else:   column_bound = j + 1        
        
            #Get neighbor's coordinates.
            x = i+increase_i
            y = j+increase_j
                  
            # Flip pieces or D1 and D5 direction.
            if (increase_i != 0 and increase_j == 0):
                for i1 in range(x, row_bound, increase_i) :
                    if (state[i1][y] == opponent):
                        next_state[i1][y] = player
                    elif (state[i1][y] == player):
                        break
                    else:
                        break 
            # Flip pieces on D3 or D7 direction.
            elif (increase_i == 0 and increase_j != 0):
                for j1 in range(y, column_bound, increase_j) :
                    if (state[x][j1] == opponent):
                        next_state[x][j1] = player
                    elif (state[x][j1] == player):
                        break
                    else:
                        break      
            # Flip pieces on D2, D4, D6, or D8 direction
            elif (increase_i !=0 and increase_j != 0):
                for i1, j1 in zip (range(x, row_bound, increase_i), range (y, column_bound, increase_j)):
                    if (state[i1][j1] == opponent):
                        next_state[i1][j1] = player
                    elif (state[i1][j1] == player):
                        break
                    else:
                        break                 
            else:
                pass                
        if DEBUG : print ('Next state = %s'%next_state)
        return next_state
        
    def getActions (self, state):
        # Get next valid action from exist state
        # Test each cell with 8 directions to validate the availabilities. 
        # Direct D1 = upper, D2 = upper right, D3 = right, D4 = bottom right, D5 = bottom, D6 = bottom left, D7 = left, D8 = upper left. 
        # For an MXN array, cell (i, j) have to test neighbor cells: D1=(i-1,j), D2=(i-1,j+1), D3=(i,j+1), D4=(i+1, j+1), D5(i+1, j), D6=(i+1, j-1), D7=(i, j-1), D8=(i-1,j-1) 
        # If neighbor cell is opposite piece, then we have to test same direction to test continuous opposite pieces until a same piece.
        # Put all valid move as tuple of coordinate into action list.
        # actions = [(i1,j1, ((i direction, j direction),...,(i,j)), (i2, j2, ((i direction, j direction),...,(i,j)), ... , (ik, jk, ((i direction, j direction),...,(i,j)]
        # i direction = 1 => row + 1, i direction = -1 =>  row - 1, j direction = 1=> column +1, j direction = -1=> column -1

        actions = list()
        directions = list()
        palyer = ""
        opponent = ""
        valid = False
        player = self.current_player

        for i, row in enumerate(state):
            for j, cell in enumerate(row):
                # Investigate this cell is a valid move by 8 directions.
                if(state[i][j] != BLACK_SYMBLE and state[i][j] != WHITE_SYMBLE): #The cell should be empty
                    # Neighbor in D1=(i-1,j)
                    if self.getValidMove(state, i, j, -1, 0) :
                        directions.append((-1, 0))
                        valid = True       
                    #Neighbor in D2=(i-1,j+1)
                    if self.getValidMove(state, i, j, -1, 1):
                        directions.append((-1, 1))
                        valid = True        
                    #Neighbor in D3=(i,j+1)
                    if self.getValidMove(state, i, j, 0, 1):
                        directions.append((0, 1))
                        valid = True 
                    #Neighbor in D4=(i+1, j+1)
                    if self.getValidMove(state, i, j, 1, 1):
                        directions.append((1, 1))
                        valid = True 
                    #Neighbor in D5(i+1, j)
                    if self.getValidMove(state, i, j, 1, 0):
                        directions.append((1, 0))
                        valid = True 
                    #Neighbor in D6=(i+1, j-1)
                    if self.getValidMove(state, i, j, 1, -1):
                        directions.append((1, -1))
                        valid = True 
                    #Neighbor in D7=(i, j-1)
                    if self.getValidMove(state, i, j, 0, -1):
                        directions.append((0, -1))
                        valid = True 
                    #Neighbor in D8=(i-1,j-1) 
                    if self.getValidMove(state, i, j, -1, -1):
                        directions.append((-1, -1)) 
                        valid = True                               
                    if valid :
                        actions.append((i, j, directions))
                        valid = False
                        directions = list()
                    
                else:
                    pass
        if DEBUG : print ('Player=%s, actions = [%s]'%(player, actions))
        
        return actions
                
    def getValidMove (self, state, i, j, increase_i, increase_j):
        # Testing cell (i, j) is a valid move or not from existing state.
        # Test each cell with 8 directions to validate the availabilities. 
        # Direct D1 = upper, D2 = upper right, D3 = right, D4 = bottom right, D5 = bottom, D6 = bottom left, D7 = left, D8 = upper left. 
        # For an MXN array, cell (i, j) have to test neighbor cells: D1=(i-1,j), D2=(i-1,j+1), D3=(i,j+1), D4=(i+1, j+1), D5(i+1, j), D6=(i+1, j-1), D7=(i, j-1), D8=(i-1,j-1) 
        # If neighbor cell is opposite piece, then we have to test same direction to test continuous opposite pieces until a same piece.
        palyer = ""
        opponent = ""
        isValid = False
        x = 0
        y = 0
        row_bound = 0
        column_bound = 0
        player = self.current_player
        if (player == BLACK_SYMBLE) :
            opponent = WHITE_SYMBLE
        else :
            opponent = BLACK_SYMBLE
        #Get neighbor's coordinates.
        x = i+increase_i
        y = j+increase_j
        #Neighbor is opponent.
        if (x >=0 and x < M and y >=0 and y < N and state[x][y] == opponent):
            if DEBUG : print ('i,j = %d, %d has an opponent neighbor'%(i, j))
            if increase_i > 0: row_bound = M
            elif increase_i < 0: row_bound = -1
            else: row_bound = i + 1
                
            if increase_j > 0: column_bound = N
            elif increase_j < 0: column_bound = -1
            else:   column_bound = j + 1

            # Move to D1 or D5
            if (increase_i != 0 and increase_j == 0):
                for i1 in range(x, row_bound, increase_i) :
                    if (state[i1][y] == opponent):
                        pass
                    elif (state[i1][y] == player):
                        isValid = True
                        break
                    else:
                        break 
            # Move to D3, 7
            elif (increase_i == 0 and increase_j != 0):
                for j1 in range(y, column_bound, increase_j) :
                    if (state[x][j1] == opponent):
                        pass
                    elif (state[x][j1] == player):
                        isValid = True
                        break
                    else:
                        break      
            # Move to D2, D4, D6, D8         
            elif (increase_i !=0 and increase_j != 0):
                for i1, j1 in zip (range(x, row_bound, increase_i), range (y, column_bound, increase_j)):
                    if (state[i1][j1] == opponent):
                        pass
                    elif (state[i1][j1] == player):
                        isValid = True
                        break
                    else:
                        break                 
            else:
                pass                
        else:
            pass    
        return isValid

    def getCoordinates (self, i=-1, j=-1):
        # Convert the system internal coordinates system to board system.
        coordinates = 'root'
        
        if (i == -1 and j == -1):
            return coordinates
        elif (i == -9 and j == -9):
            return 'pass'
        else:
            coordinates = NUMBER2ALPHABET.get(j+1, None) + str(i+1) 
        
        return coordinates
    
    def setNextState (self, value, next_state):
        # put next step into memory    
        if (self.max_value < value):
            self.next_state = copy.deepcopy(next_state)
            self.max_value = value
       
if __name__ == "__main__":

    '''
        Main program.
            Construct Alpha-Beta-Search with input data.
            Build Tree model after search valid action.
            Print next state and evaluation data
    '''
    #program_name = sys.argv[0]
    #input_file = sys.argv[1]
    input_file = INPUT_FILE
    actions = []
    value = 0
    
    player, depth, initial_state = getInputData(input_file)
    abs = AlphaBetaSearch(player, depth, initial_state)
    value, next_state = abs.executeSearch()
    action_steps = abs.output_actions
        
    setOutputData(OUTPUT_FILE, action_steps, next_state)
                     
                   


    


        