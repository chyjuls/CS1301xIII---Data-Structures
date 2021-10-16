def names_to_apa(string):

    string = string.split(',')
    Finalstring = ""
    for item in string:
        if " and " in item:
            item = item.split()
            Finalstring+="& "+item[2]+", "+item[1][:1]+"."
        else:
            item = item.split()
            Finalstring+=item[1]+", "+item[0][:1]+"., "

    return Finalstring

#print: Last, F., Joyner, D., & Burdell, G.
print(names_to_apa("First Last, David Joyner, and George Burdell"))

#Sample solution:
#with "," since the names are separated with commas
#We also create an empty string where we will concatenate all
#the abbreviated APA versions of the names.

    list_names = string.split(",")
    result = ""

#Now, from the list of names we have made, we iterate through
#with a for each loop. 'name' variable is currently a string.
#In order to separately access the first and last name of each
#author, we have to further split the 'name' string.
#Note that name (for example) will be: and George Burdell

    for name in list_names:
        fullName = name.split() 

#Now, fullName is, for example, is ["David", "Joyner"]
#
#Since the last name will always have the world "and"
#if the 0th index of the fullName list is NOT "and"
#we have the format of: Last, F.,
#
#Last name is accessed by fullName[1]
#The first letter of the first name is accessed by fullName[0][0]
#The first [0] means the index of the list and the second [0]
#means the first letter of the string
#We concatenate appropriately with spaces, commas and periods.

        if fullName[0] != "and":
            result += fullName[1] + ", " + fullName[0][0] + "., "

#From the condition, we know that if the first index is "and"
#then it is the last name on the list.
#For example, fullName would be ["and", "George", "Burdell"]
#Thus we will format it and correctly access the index and
#concatenate to the result string

        else:
            result += "& " + fullName[2] + ", " + fullName[1][0] + "."

#Once done, we return the result

    return result
