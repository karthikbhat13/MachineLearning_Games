# class represents a state of a tic tac toe game.
# 0 represents an unfilled square
# 1 represents an X
# 2 represents an O
import copy
import random
import pickle

class ExperimentGenerator:
    
    def __init__(self):
        self.board = self.generateBoard()
        self.trace = self.generateTrace()
        self.index = 0
        self.history = [copy.deepcopy(self.board)]
        self.traceHistory = [copy.deepcopy(self.trace)]

    def setBoard(self,board):
        if board == 0:
            print("empty")
        self.board = board
        self.history.append(copy.deepcopy(self.board))

    def generateBoard(self):
        board = [ [0,0,0],
                  [0,0,0],
                  [0,0,0] ]
        return board
    
    def generateTrace(self):
        board = [ [0,0,0],
                  [0,0,0],
                  [0,0,0] ]
        return board
    
    def setTrace(self,trace):
        if trace == 0:
            print("empty")
        self.trace = trace
        self.traceHistory.append(copy.deepcopy(self.trace))

    def getTrace(self):
        return trace

    def getWinner(self, board = 0):
        if board == 0:
            board = self.board

        if self.isDone(board):
            
            possibilities = []
            for row in self.getRows(board):
                possibilities.append(row)
            for column in self.getColumns(board):
                possibilities.append(column)
            for diagonal in self.getDiagonals(board):
                possibilities.append(diagonal)
            
            for possibility in possibilities:
                zeros = 0
                Xs = 0
                Os = 0
                for entry in possibility:
                    if entry == 0:
                        zeros += 1
                    elif entry == 1:
                        Xs += 1
                    elif entry == 2:
                        Os += 1
            
                if Xs == 3:
                    return 1
                elif Os == 3:
                    return 2

            return 0

        else:
            print("Game not done, cannot determine winner")

    def isDone(self, board = 0):
        if board == 0:
            board = self.board

        done = True
        for y in range(0,3):
            for x in range(0,3):
                if board[y][x] == 0:
                    done = False
                            
        possibilities = []
        for row in self.getRows(board):
            possibilities.append(row)
        for column in self.getColumns(board):
            possibilities.append(column)
        for diagonal in self.getDiagonals(board):
            possibilities.append(diagonal)
            
        for possibility in possibilities:
            zeros = 0
            Xs = 0
            Os = 0
            for entry in possibility:
                if entry == 0:
                    zeros += 1
                elif entry == 1:
                    Xs += 1
                elif entry == 2:
                    Os += 1
            
            if Xs == 3 or Os == 3:
                done = True
                
        return done

    def getOldFeatures(self, board = 0):
        if board == 0:
            board = self.board
        #x1 = number of instances of 2 x's in a row with an open subsequent square
        #x2 = number of instances of 2 o's in a row with an open subsequent square
        #x3 = number of instances of an x in an open row or column
        #x4 = number of instances of an o in an open row or column
        #x5 = number of instances of 3 xs in a row
        #x6 = number of instances of 3 os in a row
        possibilities = []
        for row in self.getRows(board):
            possibilities.append(row)
        for column in self.getColumns(board):
            possibilities.append(column)
        for diagonal in self.getDiagonals(board):
            possibilities.append(diagonal)

        x1 = 0      
        x2 = 0
        x3 = 0
        x4 = 0
        x5 = 0
        x6 = 0
        for possibility in possibilities:
            zeros = 0
            Xs = 0
            Os = 0
            for entry in possibility:
                if entry == 0:
                    zeros += 1
                elif entry == 1:
                    Xs += 1
                elif entry == 2:
                    Os += 1
            if Xs == 2 and zeros == 1:
                x1 += 1
            elif Os == 2 and zeros == 1:
                x2 += 1
            elif Xs == 1 and zeros == 2:
                x3 += 1
            elif Os == 1 and zeros == 2:
                x4 += 1
            elif Xs == 3:
                x5 += 1
            elif Os == 3:
                x6 += 1

        return x1,x2,x3,x4,x5,x6
    

    def getFeatures(self, board , trace):

        possibilities = []
        for row in self.getRows(board):
            possibilities.append(row)
        for column in self.getColumns(board):
            possibilities.append(column)
        for diagonal in self.getDiagonals(board):
            possibilities.append(diagonal)

        tracePos = []

        for row in self.getRows(trace):
            tracePos.append(row)
        for column in self.getColumns(trace):
            tracePos.append(column)
        for diagonal in self.getDiagonals(trace):
            tracePos.append(diagonal)


        x1 = 0      
        x2 = 0
        x3 = 0
        x4 = 0
        x5 = 0
        x6 = 0
        x7 = 0      
        x8 = 0
        x9 = 0
        x10 = 0
        x11 = 0
        x12 = 0
        for i in range (0,len(possibilities)):
            zeros = 0
            Xs = 0
            Os = 0
            for entry in possibilities[i]:
                if entry == 0:
                    zeros += 1
                elif entry == 1:
                    Xs += 1
                elif entry == 2:
                    Os += 1
            if Xs == 3:
                x1 += 1
            elif Os == 3:
                x2 += 1
            if Xs == 2:
                if zeros == 1:
                    x7+=1
                elif(Os == 1 and possibilities[i][tracePos[i].index(max(tracePos[i]))] == 2):
                    x9+=1
            if Os == 2:
                if zeros == 1:
                    x8+=1
                elif(Xs == 1 and possibilities[i][tracePos[i].index(max(tracePos[i]))] == 1):
                    x10+=1




        x3 = self.getFork(self.getRows(board),self.getColumns(board),1) or self.getFork(self.getDiagonals(board),self.getColumns(board),1) or self.getFork(self.getRows(board),self.getDiagonals(board),1)  
        x4 = self.getFork(self.getRows(board),self.getColumns(board),2) or self.getFork(self.getDiagonals(board),self.getColumns(board),2) or self.getFork(self.getRows(board),self.getDiagonals(board),2)
        
        if(board [1][1] == 1):
            x5 += 1
        elif(board [1][1] == 2):
            x6 += 1
        
        """
        if(board[0][0] == 1 and board[2][2] == 2):
            if(trace[0][0] > trace[2][2]):
                x9 += 1
            elif(trace[0][0] < trace[2][2]):
                x10 += 1
        elif(board[0][0] == 2 and board[2][2] == 1):
            if(trace[0][0] < trace[2][2]):
                x9 += 1
            elif(trace[0][0] > trace[2][2]):
                x10 += 1
        if(board[0][2] == 1 and board[2][0] == 2):
            if(trace[0][2] > trace[2][0]):
                x9 += 1
            elif(trace[0][2] < trace[2][0]):
                x10 += 1
        elif(board[0][2] == 2 and board[2][0] == 1):
            if(trace[0][2] < trace[2][0]):
                x9 += 1
            elif(trace[0][2] > trace[2][0]):
                x10 += 1
            """    

        return x1, x2, x3, x4, x5, x6, x7, x8, x9, x10  

    def getFork(self,row1,row2,mode):
        true1 = False
        true2 = False
        if(row1 == row2):
            return 0
        for row in row1:
            freq = 0
            freq0 = 0
            for i in range(0,len(row)):
                if row[i] == mode:
                    freq+=1
                elif row[i] == 0:
                    freq0+=1
            if(freq == 2 and freq0 == 1):
                true1 = True
                    


        for row in row2:
            freq = 0
            freq0= 0
            for i in range(0,len(row)):
                if row[i] == mode:
                    freq+=1
                elif row[i] == 0:
                    freq0+=1
            if(freq == 2 and freq0 == 1):
                true2 = True
        if(true1 & true2):
            return 1
        return 0
        
            

    def getRows(self, board = 0):
        if board == 0:
            board = self.board
        return board
    
    def getColumns(self,board = 0):
        if board == 0:
            board = self.board

        columns = []
        for x in range(0,3):
            column = []
            column.append(board[0][x])
            column.append(board[1][x])
            column.append(board[2][x])
            columns.append(column)

        return columns

    def getDiagonals(self,board = 0):
        if board == 0:
            board = self.board

        diagonals = []

        diagonal1 = []
        diagonal1.append(board[2][0])
        diagonal1.append(board[1][1])
        diagonal1.append(board[0][2])
        diagonals.append(diagonal1)

        diagonal2 = []
        diagonal2.append(board[0][0])
        diagonal2.append(board[1][1])
        diagonal2.append(board[2][2])
        diagonals.append(diagonal2)

        return diagonals

    def getSuccessorsX(self):
        successors = []
        successors1 = []
        for y in range(0,3):
            for x in range(0,3):
                if self.board[y][x] == 0:
                    successor = copy.deepcopy(self.board)
                    successor1 = copy.deepcopy(self.trace)
                    successor[y][x] = 1
                    successor1[y][x] = self.index+1
                    successors.append(successor)
                    successors1.append(successor1)
        return successors,successors1

    def getSuccessorsO(self):
        successors = []
        successors1 = []
        for y in range(0,3):
            for x in range(0,3):
                if self.board[y][x] == 0:
                    successor = copy.deepcopy(self.board)
                    successor1 = copy.deepcopy(self.trace)
                    successor[y][x] = 2
                    successor1[y][x] = self.index +1
                    successors.append(successor)
                    successors1.append(successor1)
        return successors,successors1

    def getHistory(self):
        return self.history
    
    def gettraceHistory(self):
        return self.traceHistory

    def setX(self,x,y):
        self.board[y][x] = 1
        self.trace[y][x] = self.index + 1
        self.index += 1
        self.history.append(copy.deepcopy(self.board))
        self.traceHistory.append(copy.deepcopy(self.trace))

    def setO(self,x,y):
        self.board[y][x] = 2


    def compareBoard(self,board1,board2):
        for i in range(0,3):
            for j in range(0,3):
                if(board1[i][j] != board2[i][j]):
                    self.trace[i][j] = self.index + 1
                    self.index += 1
                    self.traceHistory.append(copy.deepcopy(self.trace))
                    return 0

    def printBoard(self, board = 0):
        if board == 0:
            board = self.board

        sboard = []
        for row in board:
            srow = []
            for entry in row:
                if entry == 0:
                    srow.append(' ')
                elif entry == 1:
                    srow.append('X')
                elif entry == 2:
                    srow.append('O')
            sboard.append(srow)

        print ""
        print sboard[0][0] + '|' + sboard[0][1] + '|' + sboard[0][2]
        print "-----"
        print sboard[1][0] + '|' + sboard[1][1] + '|' + sboard[1][2]
        print "-----"
        print sboard[2][0] + '|' + sboard[2][1] + '|' + sboard[2][2]
        print ""

class PerformanceSystem:
    def __init__(self,board,hypothesis,updateConstant,mode = 1):
        self.board = board
        self.hypothesis = hypothesis
        self.mode = mode
        self.history = []        
        self.updateConstant = updateConstant

    def setUpdateConstant(self, constant):
        self.updateConstant = constant
    
    def setIndex(self,ind):
        self.index = ind
    
    def getIndex(self,ind):
        return self.index

    def evaluateBoard(self,board,trace):
        x1,x2,x3,x4,x5,x6,x7,x8,x9,x10 = self.board.getFeatures(board,trace)

        w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10 = self.hypothesis

        return w0 + w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5 + w6*x6 + w7*x7 + w8*x8 + w9*x9 + w10*x10

    def setBoard(self, board):
        self.board = board

    def getBoard(self):
        return self.board

    def setHypothesis(self, hypothesis):
        self.hypothesis = hypothesis

    def getHypothesis(self):
        return self.hypothesis
    

    

    def chooseRandom(self):
        if self.mode == 1:
            successors,successors1 = self.board.getSuccessorsX()
        else:
            successors,successors1 = self.board.getSuccessorsO()
            
        temp = random.randint(0,len(successors)-1)
        
        #self.board.compareBoard(self.board.getRows(),randomBoard)
        self.board.index += 1
        self.board.setBoard(successors[temp])
        self.board.setTrace(successors1[temp])

    def chooseMove(self):
        if self.mode == 1:
            successors,successors1 = self.board.getSuccessorsX()
        else:
            successors,successors1 = self.board.getSuccessorsO()

        bestSuccessor = successors[0]
        bestSuccessor1 = successors1[0]
        bestValue = self.evaluateBoard(bestSuccessor,bestSuccessor1)

        for i in range(0,len(successors)):
            value = self.evaluateBoard(successors[i],successors1[i])
            if value > bestValue:
                bestValue = value
                bestSuccessor = successors[i]
                bestSuccessor1 = successors1[i]


        #self.board.compareBoard(self.board.getRows(),bestSuccessor)
        self.board.setBoard(bestSuccessor)
        self.board.setTrace(bestSuccessor1)
        self.board.index += 1 


    def updateWeights(self,history,traceHistory,trainingExamples):
        for i in range(0,len(history)):
            w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10 = self.hypothesis
            vEst = self.evaluateBoard(history[i],traceHistory[i])
            x1,x2,x3,x4,x5,x6,x7,x8,x9,x10 = trainingExamples[i][0]
            vTrain = trainingExamples[i][1]            

            w0 = w0 + self.updateConstant*(vTrain - vEst)
            w1 = w1 + self.updateConstant*(vTrain - vEst)*x1
            w2 = w2 + self.updateConstant*(vTrain - vEst)*x2
            w3 = w3 + self.updateConstant*(vTrain - vEst)*x3
            w4 = w4 + self.updateConstant*(vTrain - vEst)*x4
            w5 = w5 + self.updateConstant*(vTrain - vEst)*x5
            w6 = w6 + self.updateConstant*(vTrain - vEst)*x6
            w7 = w7 + self.updateConstant*(vTrain - vEst)*x7
            w8 = w8 + self.updateConstant*(vTrain - vEst)*x8
            w9 = w9 + self.updateConstant*(vTrain - vEst)*x9
            w10 = w10 + self.updateConstant*(vTrain - vEst)*x10

            self.hypothesis = w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10
    
    
        
            

class Critic:
    def __init__(self,hypothesis,mode = 1):
        self.hypothesis = hypothesis
        self.mode = mode
        self.checker = ExperimentGenerator()
        
    
    def evaluateBoard(self,board,trace):
        x1,x2,x3,x4,x5,x6,x7,x8,x9,x10 = self.checker.getFeatures(board,trace)

        w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10 = self.hypothesis

        return w0 + w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5 + w6*x6 + w7*x7 + w8*x8 + w9*x9 + w10*x10 

    def setHypothesis(self,hypothesis):
        self.hypothesis = hypothesis

    def setMode(self,mode):
        self.mode = mode

    def getTrainingExamples(self,history,traceHistory):
        trainingExamples = []

        for i in range(0,len(history)):
            if(self.checker.isDone(history[i])):
                if(self.checker.getWinner(history[i]) == self.mode):
                    trainingExamples.append([self.checker.getFeatures(history[i],traceHistory[i]), ((0.95**(len(history)-i))*100)])
                elif(self.checker.getWinner(history[i]) == 0):
                    trainingExamples.append([self.checker.getFeatures(history[i],traceHistory[i]), ((0.95**(len(history)-i))*0)])
                else:
                    trainingExamples.append([self.checker.getFeatures(history[i],traceHistory[i]), ((0.95**(len(history)-i))* -100)])
            else:
                if i+2 >= len(history):
                    if(self.checker.getWinner(history[len(history)-1]) == 0):
                        trainingExamples.append([self.checker.getFeatures(history[i],traceHistory[i]), ((0.95**(len(history)-i))*0)])
                    else:
                        trainingExamples.append([self.checker.getFeatures(history[i],traceHistory[i]), ((0.95**(len(history)-i))* -100)])
                else:
                    trainingExamples.append([self.checker.getFeatures(history[i],traceHistory[i]), ((0.95**(len(history)-i)) * self.evaluateBoard(history[i+2],traceHistory[i+2]))])

        return trainingExamples



def saveData(filename,obj):
    with open(filename,'a') as fp:
        temp = list(obj)
        temp = [str(i) for i in temp]
        fp.write(' '.join(temp))
        fp.write('\n')

def getData(filename):
    l =[]
    k =[]
    with open(filename,'r') as fp:
        l = fp.readlines()
        for i in l:
            i = i.strip('\n')
            temp = i.split(' ')
            k.append(temp)
    return k

def getHypo(lyst,num):
    temp = lyst[num]
    l = [float(i) for i in temp]

    return tuple(l)
    

filename = 'record.txt'   
choice = 0
if not getData(filename):
    saveData(filename,(.5,.5,.5,.5,.5,.5,.5,.5,.5,.5,.5))


 


while(choice <= 2):
    choice = int(input("enter the chhioce"))
    data = getData(filename)
    num = len(data)
    xwins = 0
    owins = 0
    draws = 0  

    if choice == 1:
       # for k in range(10):
        board = ExperimentGenerator()
        trace = board.trace
        hypothesis1 = getHypo(data,num-2)
        hypothesis2 = getHypo(data,num-1)
        player1 = PerformanceSystem(board,hypothesis1,0.01,1)
        player2 = PerformanceSystem(board,hypothesis2,0.01,2)
        player2.setUpdateConstant(.1)
        critic1 = Critic(hypothesis1,1)
        critic2 = Critic(hypothesis2,2)  


       

        for i in range(0,10000):
            board = ExperimentGenerator()
            trace = board.trace
            player1.setBoard(board)
            player2.setBoard(board)     
            while(not board.isDone()):

                if(i % 250 == 0):
                    player1.chooseMove()
                player1.chooseMove()

                if board.isDone():
                    break

                #player1.chooseRandom()
                player2.chooseRandom()
                
                #player2.chooseMove()
                
                
        # board.printBoard()
            #print(board.trace)

            winner = board.getWinner()
                
            if(winner == 1):
                #print "X wins"
                xwins += 1
            elif(winner == 2):
                #print "O wins"
                owins += 1
            elif(winner == 0):
            # print "game is a draw"
                draws += 1

            critic1.setHypothesis(player1.getHypothesis())
            critic2.setHypothesis(player2.getHypothesis())
            player1.updateWeights(board.getHistory(),board.gettraceHistory(),critic1.getTrainingExamples(board.getHistory(),board.gettraceHistory()))
            player2.updateWeights(board.getHistory(),board.gettraceHistory(),critic2.getTrainingExamples(board.getHistory(),board.gettraceHistory()))

        print "X won " + str(xwins) + " games."
        print "O won " + str(owins) + " games."
        print "There were " + str(draws) + " draws."
        saveData(filename,player1.getHypothesis())
        #saveData(filename,player2.getHypothesis())


    elif(choice == 2):
            board = ExperimentGenerator()
            hypothesis1 = getHypo(data,0)
            hypothesis2 = getHypo(data,num-2)
            player1 = PerformanceSystem(board,hypothesis1,0.1,1)
            player2 = PerformanceSystem(board,hypothesis2,0.1,2)
            while True:
                
                player1.setBoard(board)
                player2.setBoard(board)

                while(not board.isDone()):
                    #board.printBoard()
                    #xval = input("Enter xcoordinate: ")
                    #yval = input("Enter ycoordinate: ")
                    #board.setX(xval,yval)

                    #player1.chooseRandom()
                       


                    player1.chooseMove()
                   
                    if board.isDone():
                        break

                    board.printBoard()
                    xval = input("Enter xcoordinate: ")
                    yval = input("Enter ycoordinate: ")
                    board.setO(xval,yval)
                    
                 

                    #player2.chooseMove()
                    #player2.chooseRandom()
                board.printBoard()

                winner = board.getWinner()
                    
                if(winner == 1):
                    print "X wins"
                    xwins += 1
                elif(winner == 2):
                    print "O wins"
                    owins += 1
                elif(winner == 0):
                    print "game is a draw"
                    draws += 1

                critic1.setHypothesis(player1.getHypothesis())
                critic2.setHypothesis(player2.getHypothesis())

                player1.updateWeights(board.getHistory(),board.gettraceHistory(),critic1.getTrainingExamples(board.getHistory(),board.gettraceHistory()))
                player2.updateWeights(board.getHistory(),board.gettraceHistory(),critic2.getTrainingExamples(board.getHistory(),board.gettraceHistory()))


                saveData(filename,player1.getHypothesis())
                print(getHypo(data,num-1))
                break
                
                