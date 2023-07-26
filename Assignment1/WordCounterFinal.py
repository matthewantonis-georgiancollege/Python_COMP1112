"""
Matthew Antonis
200373088
COMP1112: Assignment 1 Word Counter

This script reads a text file, breaks it into words, counts the occurrences of each word, 
sorts the words by count, and then writes the results to a new file. 
The output is formatted as a table with two columns: Word and Frequency. It reads from sample.txt
and writes to report.txt. 

"""

def wordCount(filename):  
    # Open the file in read mode
    with open(filename) as f:
        # Read the entire content of the file
        text = f.read()
        # Split the text into words
        words = text.split()
        # Create an empty dictionary to store word frequencies
        wordFreq = {}  
        # Loop over all words
        for word in words:
            # If the word is not already in the dictionary, add it with a count of 0
            if word not in wordFreq:  
                wordFreq[word] = 0  
            # Increment the count for this word
            wordFreq[word] += 1  
        # Return the dictionary of word frequencies
        return wordFreq  
    
def saveReport(wordFreq, reportFilename):  
    # Sort the words in the dictionary by frequency, in descending order
    sortedWords = sorted(wordFreq.items(), key=lambda x: x[1], reverse=True)  
    # Open the output file in write mode
    with open(reportFilename, 'w') as f:  
        # Write the header line to the output file
        f.write('Word\t\tFrequency\n') 
        # Loop over all words and their frequencies
        for word, freq in sortedWords: 
            # Write the word and its frequency to the output file
            f.write(f'{word}\t|\t{freq}\n')
            
def main():
    # Run the word count function on the input file
    wordFreq = wordCount('sample.txt')  
    # Save the word frequencies to the output file
    saveReport(wordFreq, 'report.txt')  

if __name__ == "__main__":
    # When this script is run directly, call the main() function
    main()