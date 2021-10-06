#       Program:                GPA_Calculator.py
#       Date:                   31/Mar/2020
#       Author:                 Oluwatosin Fletcher
#       Description:            GPA Calculator


def gradeaverage(grades= True):     # Define a function to calculate the grade average
    global courseAvgGrade           # Make the course average grade a global variable so it can be accessed within and outside the fuction.
    listofGrades = []               # Create an empty list called list of grades
    listofLetters = []              # Create an empty list called list of Letters
    gradePoint = []                 # Create an empty list called grade point
    credit = []                     # Create an empty list called credit


    courseName = input("Please enter the course name: ") # Ask the user to input the course name

    while True:

        try:
            courseGrade = float(input("Please enter the course grade (% out of 100): "))                  # The try and except fuction is used to validate that only an integer
            if courseGrade < 0 or courseGrade > 100:                                                    # between 0 and 100 can be taken in as the approriate input for course grade
                print("The correct format is [0-100], Please try again.")                               # and course percentage weigth. Also use use the print statement to notify the
                continue                                                                                # user to try again and enter correct percentage weight format.

            percentageWeight = float(input("Please enter the course percentage weight(% out of 100): "))
            if percentageWeight < 0 or percentageWeight > 100:
                print("The correct format is [0-100], Please try again.")                               # use the print statement to notify the user to try again and enter correct percentage weight format.
                continue

        except Exception:
            print("The correct format is [0-100], Please try again.")
            continue

        percentageWeight /= 100                             # Calculate the actual percentage weight by dividing 100
        gp = round((courseGrade * percentageWeight), 2)     # Multiply the course grade by the percentage weight of the cousre and round it up to 2 decimal places
        listofGrades.append(gp)                             # Add the calculated grade into list created called listofGrades.

        while True:                                         # Create a loop within a loop to validate that only a Y(YES) or N(NO) can be accepted as the appropriate input

            response = input("Would you like to enter more grade to add to the data (Y/N): ")
            response = response.upper()

            if response == True:                            # If the input is true, do nothing
                print("Please enter the correct response (Y/N) to proceed")
                pass

            elif response == "Y" or response == "YES":      # Else if Y or YES is entered as input set the variable v = 1 and exit the loop
                v = 1
                break

            elif response == "N" or response == "NO":       # Else if N or NO is entered as input set the variable v = 0 and exit the loop
                v = 0
                break

            print("The correct format is [Y/N], Please try again")


        if v == 1:                                                      # To get out of the second while loop and return back to the first loop, use an If conditional statement
            continue                                                    # to verify that if the variable v is equals 1 which was created within the second loop when the user's response was Y or YES.
                                                                        # if v is equals to 1 return to the fist while loop.

        else:

            courseAvgGrade = 0                             # Loop through the list of calculated grades and add them all together to get the course average grade.
            for score in listofGrades:
                courseAvgGrade += score


            if courseAvgGrade >= 90 and courseAvgGrade <= 100:      # If the course average grade is between a specific
                listofLetters.append("A+")                          # course average grade, add the corresponding letter
                gradePoint.append(4.2)                              # grade and grade point to the empty list "listofLetters" and "gradePoint".

            elif courseAvgGrade >= 80:
                listofLetters.append("A")
                gradePoint.append(4.0)

            elif courseAvgGrade >= 75:
                listofLetters.append("B+")
                gradePoint.append(3.5)

            elif courseAvgGrade >= 70:
                listofLetters.append("B")
                gradePoint.append(3.0)

            elif courseAvgGrade >= 65:
                listofLetters.append("C+")
                gradePoint.append(2.5)

            elif courseAvgGrade >= 60:
                listofLetters.append("C")
                gradePoint.append(2.0)

            elif courseAvgGrade >= 55:
                listofLetters.append("D+")
                gradePoint.append(1.5)

            elif courseAvgGrade >= 50:
                listofLetters.append("D")
                gradePoint.append(1.0)

            elif courseAvgGrade >= 0:
                listofLetters.append("F")
                gradePoint.append(0.0)


            while True:                                                                     # Use a loop in a loop along with the try and except fuction
                try:                                                                        # to validate that only an integer between 1 and 6 is accepted
                                                                                            # as the appropriate input.
                    courseCredit = int(input("Please enter the course credit units: "))
                    if courseCredit < 1 or courseCredit > 6:
                        print("Try again, Enter a course credit between [1-6]")

                    else:
                        break


                except Exception:
                    print("Try again, Enter a course credit between [1-6]")
                    pass

            credit.append(courseCredit)                     # Add the inputted course credit to the empty list called credit


            for z in gradePoint:                            # Loop through the list Grade Point and multiply the grade
                gpXcd = z * courseCredit                    # point int the list by the course credit unit.
                newlistofgradePoint.append(gpXcd)           # Add the (Grade point X Course credit) to the new list called new list of grade point which is located outside the function


            for q in credit:                                # Loop through the list credit and add value in it to the new list of credit located outside the function.
                newlistofCredit.append(q)

        break


    print("Course", courseName, "final grade:", courseAvgGrade, "% =", listofLetters[0], "=", gradePoint[0], "points")
    print("------------------------------------------------------------------------------")

    while True:                                                                                     # Use the while loop to validate that only a Y(YES) or N(NO)
                                                                                                    # can be taken as the approprate input when the user is prompt
        anotherCourse = input("Would you like to enter another course (Y/N): ")                     # if they would like to add another course.
        anotherCourse = anotherCourse.upper()
        print("------------------------------------------------------------------------------")

        if anotherCourse == True:
            pass

        elif anotherCourse == "Y" or anotherCourse == "YES":

            break

        elif anotherCourse == "N" or anotherCourse == "NO":

            break

        print("The correct format is [Y/N], Please try again")


    for i in anotherCourse:                         # Loop through the variable prompting the user if they would like to
        if i == "Y" or i == "YES":                  # enter another course, if the user inputs a "Y" or "YES", then the execute the
            gradeaverage()                          # grade average function to return back to the start of the program.(function in a function)


        else:
            break


newlistofgradePoint = []                            # New list of grade point were each calculated grade point (Grade point X Course credit unit) for each course within the fuctions are stored.
newlistofCredit = []                                # New list of credit were each inputed credit for each course within the fuctions are stored.


gradeaverage()

def termGPA(overallGPA = True):                     # Define a fuction to calculate the over all term GPA

    overall_gpXcd = 0
    overall_credit = 0


    for y in newlistofgradePoint:                   # Loop through the new list of grade point and add them all together into the above variable
        overall_gpXcd += y                          # overall_gpXcd to calculate the over all grade point (Grade point X Course credit unit)

    for n in newlistofCredit:                       # Loop through the new list of credit and add them all together into
        overall_credit += n                         # the above variable overall_credit


    overall_gpXcd = round(overall_gpXcd, 2)         # Round the over all grade point (Grade point X Course credit unit) into 2 decimal places
    overall_credit = round(overall_credit, 2)       # Round the over all credit into 2 decimal places
    overall_GPA = round(overall_gpXcd / overall_credit, 2)      #Calculate the over all GPA by dividing the over all grade point (Grade point X Course credit unit) by the over all credit

    print("##############################################################################")
    print("Your total grade point for the term is ==>",overall_gpXcd)
    print("Your total credit for the term is ==>",overall_credit)
    print("Your overall Term GPA","(total grade point = ",overall_gpXcd," / total credit = ", overall_credit,") is ==> ",overall_GPA, sep="")
    print("##############################################################################")
    print("This Application is courtesy of: Oluwatosin Fletcher")
    print("##############################################################################")

termGPA()

close = input("Press Enter to exit the application\n")