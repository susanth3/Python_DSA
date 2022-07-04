def KDistinct(String, K):
    '''
        This method finds the longest substring with at most K
        Distinct characters.
        input: string and a number k
        output: longest substring that has at most k distinct characters
    '''

    # define a dictionary that will work as hash table to hold our
    # characters and their frequencies.
    table = dict()

    # two variables will point to the start and end of the window
    start, end = 0, 0

    # variable to hold the size of the longest substring
    longest = 0

    # expand the window
    for end in range(len(String)):
        # get the new character
        newCharacter = String[end]

        # add the new character in the hash table
        if newCharacter in table.keys():
            table[newCharacter] += 1
        else:
            table[newCharacter] = 1

        # check if number of distinct characters in window is more
        # than K
        while len(table) > K:
            startCharacter = String[start]
            start += 1
            table[startCharacter] -= 1
            # if frequency becomes 0 then remove the character
            if table[startCharacter] == 0:
                table.pop(startCharacter)

        # check if current window is greatest seen so far
        if(end - start + 1 > longest):
            longest = end - start + 1

    return longest

# driver program


def main():
    S = "aaabb"
    K = 3
    print(KDistinct(S, K))


if __name__ == '__main__':
    main()