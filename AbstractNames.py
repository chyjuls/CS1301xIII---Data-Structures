def abstract_names(listoflist):
    Finaldict = {}
    for item in listoflist:
        for items in item:
            items = items.split()
            item0 = items[0]
            if item0  not in Finaldict:
                Finaldict[item0]=[items[1]]
            else:
                Finaldict[item0]+=[items[1]]
                
    for values in Finaldict.values():
        values.sort()
    return Finaldict
            

#print (although the order of the keys may vary):
#{"David": ["Beckham", "Joyner", "Tennant"], "Ananya": ["Agarwal", "Birla", "Chatterjee", "Roy"], "Inés": ["Melchor", "Sainz", "Suarez"]}
names = [["David Joyner", "David Tennant", "David Beckham"], ["Ananya Birla", "Ananya Agarwal", "Ananya Chatterjee", "Ananya Roy"], ["Ines Sainz", "Ines Suarez", "Ines Melchor"]]
print(abstract_names(names))

# sample solution:


def abstract_names(name_list):
    dictionary = {}

    # We have a for each loop that will go through the name_list
    # which is the list of names given to us

    for fullNameList in name_list:

        # Each 'fullNameList' is another list since the way
        # name_list is formatted is a list within a list.
        #
        # For example, name_list would be ["David Joyner", "David Tennant",
        # "David Beckham"]
        #
        # We sort it before doing anything so that later when we append
        # we are doing it in alphabetical order.

        fullNameList.sort()

        # Within the fullNameList, we iterate with a for
        # each loop to access the fullName
        # With each fullName, we know that first name
        # will always come first, and last name will
        # always be after. Note that fullName as of right now is a
        # string, so we split it to make it accessible per first and
        # last name.

        for fullName in fullNameList:
            first = fullName.split()[0]
            last = fullName.split()[1]

            # An example of fullName is "David Joyner" where first = "David"
            # and last = "Joyner"

            # We now create a key with the first name and append the last names
            # accordingly. The .setdefault() is a method that creates the key
            # if the key does not already exist and sets the initial value to an
            # empty list.

            dictionary.setdefault(first, [])
            dictionary[first].append(last)

    # We return dictionary at the end when everything is finished

    return dictionary


names = [["David Joyner", "David Tennant", "David Beckham"],
         ["Ananya Birla", "Ananya Agarwal", "Ananya Chatterjee", "Ananya Roy"],
         ["Ines Sainz", "Ines Suarez", "Ines Melchor"]]
print(abstract_names(names))
