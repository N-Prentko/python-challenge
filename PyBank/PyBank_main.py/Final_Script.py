#Import os library to efficiently import csv file
import os
#Import csv file 
import csv

#Create variables by assigning a value to them
Total_Months = 0
Net_Total_PL = 0
Value_PL = 0
Value_Change = 0
Profit_Loss = []

Dates = []

output_path = os.path.join('..',"output.txt")
#Create an object called Budget_Data from the budget_data.csv
Budget_Data = os.path.join('..',"budget_data.csv")

with open(Budget_Data) as csvfile:
    #Create variable that reads budget_data.csv
    CSV_Reader = csv.reader(csvfile, delimiter = ",")

    #Use next() method to return the header row
    CSV_Header = next(CSV_Reader)

    #Use next() method to return the first row
    First_Row = next(CSV_Reader)
    
    #Write Python shorthand for Total_Months = Total_Months + 1
    Total_Months += 1

    #Use Python shorthand for Net_Total_PL = Net_Total_PL + int(string, base)
    Net_Total_PL += int(First_Row[1])

    #Use int() function to assign value to Value_PL
    Value_PL = int(First_Row[1])

    #Iterate through each row after the first row of data by using a for loop
    for row in CSV_Reader:
        
        Total_Months += 1

        #Calculate the Value_Change via int function - Value_PL
        Value_Change = int(row[1])-Value_PL
    
        #Add Profit_Loss to the list of changes via append function
        Profit_Loss.append(Value_Change)

        #Calculate total PL during duration
        Net_Total_PL = int(row[1]) + Net_Total_PL

        #Reassign Value_PL value as integer of first row
        Value_PL = int(row[1])

        #Append each date to Dates list
        Dates.append(row[0])

    #Determine average of change in profit/losses over the entire period by adding all PL and dividing by total amount variables in category
    Average_Change_PL = sum(Profit_Loss)/len(Profit_Loss)
    
    #Determine greatest increase in profits
    Greatest_Increase_In_Profits = max(Profit_Loss)

    #Perform index method on respective variable  
    Greatest_Index_In_Profits = Profit_Loss.index(Greatest_Increase_In_Profits)

    #Determine greatest decrease in losses
    Greatest_Decrease_In_Losses = min(Profit_Loss)

    #Determine average of change in profit/losses over the entire period by adding all PL and dividing by total amount variables in category
    Average_Change_PL = sum(Profit_Loss)/len(Profit_Loss)
    
    #Determine greatest increase in profits
    Greatest_Increase_In_Profits = max(Profit_Loss)

    #Find associated date
    Greatest_Date = Dates[Greatest_Index_In_Profits]

    #Determine greatest decrease in losses
    Greatest_Decrease_In_Losses = min(Profit_Loss)

    #Perform index method on respective variable
    Decrease_Index_In_Losses = Profit_Loss.index(Greatest_Decrease_In_Losses)

    #Find associated date
    Decrease_Date = Dates[Decrease_Index_In_Losses]

    #Print analysis to terminal
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {str(Total_Months)}")
    print(f"Total: ${str(Net_Total_PL)}")
    print(f"Average Change: ${str(round(Average_Change_PL,2))}")
    print(f"Greatest Increase in Profits: {Greatest_Date} (${str(Greatest_Increase_In_Profits)})")
    print(f"Greatest Decrease in Profits: {Decrease_Date} (${str(Greatest_Decrease_In_Losses)})")

            #Export a text file with the analysis
    #Exported_Analysis   =   ("Exported_Analysis.text","W")

    output = (
      f"\nFinancial Analysis\n"
       "----------------------------\n"
        f"\nTotal Months: {(Total_Months)}\n"
        f"\nTotal: ${(Net_Total_PL)}\n"
        f"\nAverage Change: ${(round(Average_Change_PL,2))}\n"
        f"\nGreatest Increase in Profits: {Greatest_Date} (${(Greatest_Increase_In_Profits)})\n"
        f"\nGreatest Decrease in Profits: {Decrease_Date} (${(Greatest_Decrease_In_Losses)})\n"
    
    )
    #Exported_Analysis.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(Line_1,Line_2,Line_3,Line_4,Line_5,Line_6,Line_7))
    
    with open(output_path, "w") as txt_file:
        txt_file.write(output)
    