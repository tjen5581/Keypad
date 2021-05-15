#Tatiana Jenkins
 #Final for Embedded Systems 
 #May 11th, 2021


from random import randint


##=========================================================

# Create a state base class
State = type('State',(object,),{})

# Create the two states for the door (locked and unlocked)
class doorLocked(State):
    def Execute(self):
        print('DOOR IS LOCKED!!\n')

class doorUnlocked(State):
    def Execute(self):
        print('DOOR IS UNLOCKED!!\n')

##=========================================================

# Create the transition between the states
class Transition(object):
    def __init__(self, toState):
        self.toState = toState

    def Execute(self):
        print('Transitioning....\n')


##=========================================================

# Creating the finite state machine
class SimpleFSM(object):
    def __init__(self,char):
        self.char = char
        self.states = {}
        self.transitions ={}
        self.curState = None
        self.trans = None
    
    def SetState(self,stateName):
        self.curState = self.states[stateName]
   
    def Transition(self, transName):
        self.trans = self.transitions[transName]

    def Execute(self):
        if (self.trans):
            self.trans.Execute()
            self.SetState(self.trans.toState)
            self.trans = None
        self.curState.Execute()
##=========================================================
# Create a character class
class Char(object):
    def __init__(self):
        self.FSM = SimpleFSM(self)
        self.doorLocked = True

##=========================================================

# Main Program
if __name__ == '__main__':
    door = Char()

    door.FSM.states['Locked'] = doorLocked()
    door.FSM.states['Unlocked'] = doorUnlocked()
    door.FSM.transitions['toLocked'] = Transition('Locked')
    door.FSM.transitions['toUnlocked'] = Transition('Unlocked')

    door.FSM.SetState('Locked')
    
    reset = '#'
    code = str(input('PLEASE ENTER THE SIX DIGIT PASSCODE!\n'))
    while reset == '#':
        pass
 
        if code == '147258':
            door.FSM.Transition('toUnlocked')
            door.doorLocked = False
            reset = 0
        else:
            door.FSM.Transition('toLocked')
            door.doorLocked = True
            reset = '#'
            print('WRONG PASSCODE!\n')
            print('PLEASE ENTER THE SIX DIGIT PASSCODE!\n')
            code = input()
            
        door.FSM.Execute()
