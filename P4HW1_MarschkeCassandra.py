# CTI-110
# P4HW1 - Score List
# Cassandra Marschke
# 14 November 2022
#
# This program takes input from the user and displays results based on the input
# This creates a list to store scores
# This program asks the user to input how many scores the user would like entered
# The user inputs all scores and the program returns with the lowest score, score list, scores average, and letter grade



scores_list = []

score_input = int(input("How many scores do you want to enter? "))

num_scores = 0

while(True):
    
   
    while(num_scores<score_input):
        scores = float(input('Enter score #{}: '.format(num_scores+1)))
        
        
        while(True):
            if(scores<0 or scores>100):
                print("\nINVALID Score entered!!!!\nScore should be between 0 and 100")
                scores = float(input('Enter score #{} again: '.format(num_scores+1)))
            
              
            else:
                
                
                scores_list.append(scores)
                
               
                break
        
      
        num_scores+=1 
        
        
    
    if(num_scores==score_input):
        
        break


min_score = min(scores_list)
scores_list.remove(min(scores_list))
avg = sum(scores_list)/len(scores_list)

if avg >= 90:
    grade = 'A'
elif avg >= 80:
    grade = 'B'
elif avg >= 70:
    grade = 'C'
elif avg >= 60:
    grade = 'D'
elif avg <= 59:
    grade = 'F'
    
print()
print()
print("--------------------Results----------------------")
print("Lowest Score  :",min_score)
print("Modified List :",scores_list)
print("Scores Average:",avg)
print("Grade         :",grade)
print("-------------------------------------------------")

        
        
        
    
        
    
