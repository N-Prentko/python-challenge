#Import csv file 
import csv
import os

#Create variables by assigning values to them
Total_Counted_Votes = 0
Candidate_Array = []
Votes_For_Candidates ={}
Winner = ""
Votes_For_Winner = 0
output_path = os.path.join('..',"voter_output.txt")


#Create an ogject called Election_Data
Election_Data = os.path.join("election_data.csv")

#Open election_data.csv
with open(Election_Data, newline = "") as csvfile:
    #Create a variable that reads election_data.csv
    CSV_Reader = csv.reader(csvfile)

    #Use next() method to return the header row
    CSV_Header = next(CSV_Reader)
    
    #Iterate through each row for loop
    for row in CSV_Reader:
        
        #Write Python shorthand for Total_Counted_Votes = Total_Counted_Votes + 1
        Total_Counted_Votes += 1

        #Differentiate between candidates
        Name_Of_Candidate = row[2]

             #Create a conditional to keep track of candidates
        if Name_Of_Candidate not in Candidate_Array:

            #Add it to Candidate_Array
            Candidate_Array.append(Name_Of_Candidate)

            #Commence counting votes for respective candidate
            Votes_For_Candidates[Name_Of_Candidate] = 0

        #Then add an aditional vote to the respective candidates total
        Votes_For_Candidates[Name_Of_Candidate] = Votes_For_Candidates[Name_Of_Candidate] + 1
        

#Save vote count to text_file
with open(output_path, "w") as txt_file:
       
    Election_Data_Output = (
    f"\n\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {Total_Counted_Votes}\n"
    f"-------------------------\n")
    
    
    txt_file.write(Election_Data_Output)
    print(Election_Data_Output, end = "")
    
    for candidate in Votes_For_Candidates:


        Votes = Votes_For_Candidates.get(candidate)

        Vote_Percentage = float(Votes) / float(Total_Counted_Votes) * 100
        
#Use conditional to determine winner
        if Votes > Votes_For_Winner:
            Votes_For_Winner = Votes
            Winner = candidate

#Display respective candidate's voter count and percentage to terminal
        Voter_Count = (f"{candidate}: {Vote_Percentage:.3f}% ({Votes})\n")
        print(Voter_Count, end="")

#Commit respective candidates voter data to text file
    txt_file.write(Voter_Count)

# #Display winning candidate to terminal
Winner_Synopsis = (
f"-------------------------\n"
f"Winner: {Winner}\n"
f"-------------------------\n")
print(Winner_Synopsis)
