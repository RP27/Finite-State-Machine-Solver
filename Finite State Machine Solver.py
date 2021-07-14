testData = (
    {
        "Time mode": ("Timer mode", "Timezone2 mode", "Time set mode"), 
        "Time set mode": ("Time set mode", "Time mode", "Date set mode"), 
        "Timer mode": ("Stopwatch mode", "Timer set mode", "Timer mode"), 
        "Timer set mode": ("Timer set mode", "Timer mode", "Timer set mode"), 
        "Date set mode": ("Date set mode", "Time set mode", "Date set mode"), 
        "Stopwatch mode": ("Alarm 1 mode", "Stopwatch mode", "Stopwatch mode"), 
        "Alarm 1 mode": ("Alarm 2 mode", "Alarm 1 mode", "Alarm 1 set mode"), 
        "Alarm 1 set mode": ("Alarm 1 set mode", "Alarm 1 mode", "Alarm 1 set mode"), 
        "Alarm 2 mode": ("Time mode", "Alarm 2 mode", "Alarm 2 set mode"), 
        "Alarm 2 set mode": ("Alarm 2 set mode", "Alarm 2 mode", "Alarm 2 set mode"), 
        "Timezone2 mode": ("Timezone2 mode", "Time mode", "Timezone2 mode")
    }, 
    'Time mode', 
    'Date set mode'
)

# Status of whether the destination state is found
foundStatus = [0]

# Sequence of button presses required to take the watch from the starting state to the destination state
buttonPresses = []  

# Creates a list of 0s, with each 0 representing a mode. Once a mode is searched, the value of the mode in the list is then set to 1.
modeLinkSearched = [0] * len(testData[0])

# Helper method for the solution function
def solutionHelper(instance, startingMode, destinationMode):
    stateAcceptanceCriteria = instance

    # Gets all the keys inside the stateAcceptanceCriteria
    keys  = list(stateAcceptanceCriteria.keys())

    # If the destination mode is not within the current state's accepting states
    if not destinationMode in stateAcceptanceCriteria[startingMode]:
        
        # Finds the index of the current state in list of keys
        index = keys.index(startingMode)
        # Sets the mode link to 1 as it is going to be searched
        modeLinkSearched[index] = 1        

        # For each state within the current state's accepting states
        for state in stateAcceptanceCriteria[startingMode]:

            # Finds index number of the state within the list of keys
            newIndex = keys.index(state)

            # If the mode link has not been searched
            if modeLinkSearched[newIndex] == 0:
                buttonPresses.append(stateAcceptanceCriteria[startingMode].index(state))
                
                solutionHelper(stateAcceptanceCriteria, state, destinationMode)

                if(foundStatus[0] == 0):
                    buttonPresses.pop()
                else:
                    break             
    else:
        foundStatus[0] = 1
        buttonPresses.append(stateAcceptanceCriteria[startingMode].index(destinationMode))                

def solution(problemInstance):
    instance = problemInstance[0]
    start = problemInstance[1]
    end = problemInstance[2]
    print("\nStarting from " + start + " and going to " + end + ", the sequence of button presses required are in this order: ")
    solution = solutionHelper(instance, start, end)     

def printSolution(solutionInstance):    
    buttonPress = {0: "Press Mode", 1: "Press Set", 2: "Long press Set"}

    i = 0
    for buttonType in buttonPresses:
        print(str(i+1) + ". " + buttonPress.get(buttonType))
        i += 1

printSolution(solution(testData)) 
