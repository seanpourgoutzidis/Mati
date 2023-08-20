#IMPORT STATEMENTS
import torch
import yolov5.detect as detect
import yolov5.detect_sean as detect_s
from gtts import gTTS
from playsound import playsound
import LLM

def speak(wordsToSay):
    """
    This function audibly plays the string passed to it using a text to speech library
    """

    tts = gTTS(wordsToSay)

    tts.save("audio.mp3")

    playsound("audio.mp3")  

def generateQuery (objectsDetected, objectFrequency):
    """
    This function uses the objects detected by yolov5 and the amount that they occur to generate a query to the LLM 
    """
    query = "I see "
    
    query = query + constructSubQuery(objectsDetected, objectFrequency)
    
    query = query + " In a concise sentence, what setting might I be in?"
        
    return query

def constructSubQuery (objectsDetected, objectFrequency):
    
    """
    This function formats the objects detected into a subquery which is then used by other functions
    """

    query = ""
    
    iteration = 0
    
    #Iterate through the objects detected
    for item in objectsDetected:
        
        #By default, set the subquery to the item in question
        subQuery = item
        
        #If there's multiple of the item
        if (objectFrequency[item] > 1): 
            subQuery = "multiple " + item + "s"
            
        else:
            subQuery = "a " + item
        
        #Formatting the subquery
        if(iteration == len(objectsDetected) - 1):
            subQuery = subQuery + "."
        
        elif (iteration == len(objectsDetected) - 2):
            subQuery = subQuery + ", and "
            
        else:
            subQuery = subQuery + ", "
            
        #Append subquery to the end of the original query
        query = query + subQuery
        
        iteration = iteration + 1
        
    return query


def stateFoundObjects (objectsDetected, objectFrequency):
    """
    This function formulates a statement that includes all of the objects detected, factoring in their frequency
    """

    statement = "I have detected: "
    
    statement = statement + constructSubQuery(objectsDetected, objectFrequency)

    return statement

#MAIN FUNCTION
def main():
    #Detect the objects (try m for better results)
    objectsDetected, objectFrequency = detect_s.run(source = 0, weights = 'yolov5m.pt', nosave = True, conf_thres = 0.65)

    #State the objects that were detected
    speak(stateFoundObjects(objectsDetected, objectFrequency))

    #Generate query for LLM
    query = generateQuery(objectsDetected, objectFrequency)

    print("Query: " + query)

    #Get the response from LLM
    response = LLM.getResponse(query)

    print("\nResponse: " + response)

    #State the response from our LLM
    speak(response)

if __name__ == '__main__':
    main()