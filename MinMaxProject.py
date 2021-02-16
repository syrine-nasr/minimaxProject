from random import choice
class Node(object): 
    def __init__(self,depth,playerNum,n,value=0,brother=0):
        self.depth=depth
        self.playerNum=playerNum
        self.resultDiv=n
        self.value=value 
        self.brother=brother
        self.children=[]
        self.CreateChildren(n,brother)
        
        
        

    def CreateChildren(self,n,brother):
        
        if (brother == 0):
        
            for i in range (1, n//2 + 1): 
               
                if i == n-i : 
                    continue 
                
                A=(i,n-i)
                if (A[0] not in [1,2] and A[1] in [1,2]) or (A[1] not in [1,2] and A[0] in [1,2]): 
                    RealVal = 0
                    if A[0] not in [1,2]: 
                    
                        self.children.append(Node(self.depth+1,-self.playerNum,A[0],RealVal))
                    
                    if A[0] in [1,2]:
                
                        self.children.append(Node(self.depth+1,-self.playerNum,A[1],RealVal))
                        
                
                elif A[0] not in [1,2] and A[1] not in [1,2]:
                    RealVal=0
                    
                    self.children.append(Node(self.depth+1,-self.playerNum,A[0],RealVal,A[1]))
                    
                    
                if A[0] in [1,2] and A[1] in [1,2]: 
                        RealVal = self.playerNum
                     
                        self.children.append(Node(self.depth+1,-self.playerNum,A[0],RealVal,A[1]))
                        
            
        if (brother!=0):
            if brother in [1,2]:
                return 
            for i in range (1, n//2 + 1): 
               
                if i == n-i : 
                    continue 
                
                A=(i,n-i)
                
                if A[1] in [1,2] and A[0] in [1,2]: 
                    RealVal=0
                    self.children.append(Node(self.depth+1,-self.playerNum,brother,RealVal))
                
            """ if (A[0] not in [1,2] and A[1] in [1,2]) or (A[1] not in [1,2] and A[0] in [1,2]):
                    RealVal = 0
                    if A[0] not in [1,2]: 
                    
                        self.children.append(Node(-self.playerNum,A[0],RealVal,brother))
                    
                    if A[1] not in [1,2]:
                
                        self.children.append(Node(-self.playerNum,A[1],RealVal,brother))"""
                
            for i in range (1,brother//2 +1 ):
                if i== brother -i : 
                    continue 
                A=(i,brother-i)
                if A[1] in [1,2] and A[0] in [1,2]: 
                    RealVal=0
                    self.children.append(Node(self.depth+1,-self.playerNum,n,RealVal))
                
                if (A[0] not in [1,2] and A[1] in [1,2]) or (A[1] not in [1,2] and A[0] in [1,2]):
                    RealVal = 0
                    if A[0] not in [1,2]: 
                    
                        self.children.append(Node(self.depth+1,-self.playerNum,A[0],RealVal,n))
                    
                    if A[1] not in [1,2]:
                
                        self.children.append(Node(self.depth+1,-self.playerNum,A[1],RealVal,n))
                    
                
                
#ALGORITHM
def MinMax(node,depth,playerNum):
    #if(depth==0) or (abs(node.value)==1):
    if(abs(node.value)==1):
        return node.value 
    
    bestValue = -playerNum
    
    for i in range(len(node.children)):
        child=node.children[i]
        val=MinMax(child,child.depth,-playerNum)
        if(abs(playerNum - val)) < abs(playerNum - bestValue):
            bestValue=val 
    return bestValue 


#Wincheckfunction
def WinCheck(pile,playerNum):
    if pile in [1,2]:
        if playerNum>0:
            print("Human wins")
            return 0
        else:
            print("Computer wins")
            return 0
    
    if pile not in [1,2]:
        return 1

    
 
#Main 

firstpile=7 
firstbrother=0 
curPlayer=1 
print("\nInstruction:The player who can not divide the pile loses\nYou can't divide 1 nor 2 \nYou can't divide into two equal piles \n---GoodLuck!---")

pile=firstpile
brother = firstbrother 

depth=1
while(pile not in [1,2] and brother in [0,1,2] or (pile not in [1,2] and brother not in [0,1,2]) ):
#should add another while later pile not in AND brother not in 
    
        
    
        print("\nWhat would you pick?\n")
        depth+=1
        
        for i in range(1,pile//2 +1):
            if i == pile-i : 
                continue 
                    
            A=(i,pile-i)
            print(";","(",A[0],",",A[1],")",";")
            
        
        print("\nEnter the first number of the couple\nExample : 8 if the couple is (8,9)")
        brother=int(input())
        print("\nEnter the second number of the couple\nExample : 9 if the couple is (8,9)")
        pile=int(input())
        
        if (pile not in [1,2] and brother in [0,1,2]):
        
            if brother in [0,1,2]:
                brother=0
                
            # if pile in [1,2] and brother not in [1,2]:
            #     a=brother
            
            
            
            if WinCheck(pile,curPlayer):
                curPlayer*=-1
                node=Node(depth,curPlayer,pile)
                bestChoice=-10
                bestValue=-curPlayer
                
                for i in range(len(node.children)):
                    child=node.children[i]
                    val=MinMax(child,child.depth,-curPlayer)
                    if(abs(curPlayer - val)<= abs(curPlayer - bestValue)):
                        bestValue=val 
                        bestChoice=child.resultDiv
                        bro= pile - child.resultDiv
                        
                print("Computer chooses (",bro,",",bestChoice,")"+" "+"based on value "+" ",bestValue)
                
                pile=bestChoice 
                brother=node.brother
                if WinCheck(pile,curPlayer)==0:
                    print("\nHuman can no longer divide ")
                   # if curPlayer>0 : 
                   #     print("Computer can no longer divide ")
                   # if curPlayer<0: 
                   #     print("Human can no longer divide")
                
                curPlayer *=-1
        
        
        if pile not in [1,2] and brother not in [0,1,2]:
            #pc chooses 3 , donc nasn3ou node mta3 4 w depth +1
            curPlayer*=-1
            node1=Node(depth+1,curPlayer,pile)
            node3=Node(depth,curPlayer,brother,0,pile)
            # node2=Node(depth,curPlayer,brother)
            # houni bch tet9leb 
            bestChoice1=-10
            bestValue1=-curPlayer
                
            for i in range(len(node1.children)):
                    child1=node1.children[i]
                    val1=MinMax(child1,child1.depth,-curPlayer)
                    if(abs(curPlayer - val1)<= abs(curPlayer - bestValue1)):
                        bestValue1=val1 
                        bestChoice1=node3.resultDiv
                        #bro1= brother
            #pc chooses 4, nasn3ou node (3,0) depth 4 check korassa  
            curPlayer2=-curPlayer
            
            node2=Node(depth+2,curPlayer2,brother)
            bestChoice2=-10
            bestValue2=-curPlayer2
                
            for i in range(len(node2.children)):
                    child2=node2.children[i]
                    val2=MinMax(child2,child2.depth,-curPlayer2)
                    if(abs(curPlayer2 - val2)<= abs(curPlayer2 - bestValue2)):
                        bestValue2=val2 
                        bestChoice2=node3.brother
                        #bro2= pile
            
            if bestValue1>bestValue2:
                print("\nComputer chooses (",bestChoice1,")"+" "+"based on value "+" ",bestValue1)
                #here plays human
                print("\nYour choice can be :"+" ",node3.brother)
                pile=int(input("\nEnter the pile to divide:"))
                
                #pile=node1.resultDiv
                brother=0
             
                curPlayer *=-1
            
            if bestValue1<bestValue2: 
                print("\nComputer chooses (",bestChoice2,")"+" "+"based on value "+" ",bestValue1)
                #here plays human
                print("\nYour choices are :"+" ",node3.resultDiv,+" and ",node3.children[0].brother)
                pile=int(input("\nEnter the pile to divide:"))
                print("\nComputer chooses ",node3.children[0].resultDiv,+"based on value "+" ",bestValue1)
                pile=node3.children[0].children[0].resultDiv
                brother= node3.children[0].children[0].brother
                
                curPlayer *=-1

            if bestValue1==bestValue2 :   
                # seq=[bestChoice1,bestChoice2]
                # selection=choice(seq)
                # print("Computer chooses (",selection,")"+" "+"based on value "+" ",bestValue1)
                # if selection == bestChoice1: 
                #     print("\nYour choice can be :"+" ",node3.brother)
                #     pile=int(input("\nEnter the pile to divide:"))
                
                #     brother=0
                # else: 
                    print("\nYour choices are : ",node3.resultDiv," and ",node3.children[0].brother)
                    pile=int(input("\nEnter the pile to divide:"))
                    print("\nComputer chooses ",node3.children[0].resultDiv,"based on value ",bestValue1)
                    pile=node3.children[0].children[0].resultDiv
                    brother= node3.children[0].children[0].brother
                    
            curPlayer *=-1
