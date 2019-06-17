import unittest
import test_word_ladder

# NOTES: when testing this file we used the supplied dictionary.txt file as well as text file of not allowed words
# called notAllowed.txt containing the words 'side' and 'load' without this file the tests in this file will not work.

class test_case(unittest.TestCase):
    def setUp(self):
        self.test = test_word_ladder
        # this setup is purely for readability of the test cases below.

    def test_same(self):
        # tests for the same function in the test_word_ladder.py file

        item = 'hide'
        target = 'seek'
        self.assertEqual(self.test.same(item, target), 0)
        # checks that 'hide' and 'seek' have no letters in common in the same position.


        item = 'lead'
        target = 'gold'
        self.assertEqual(self.test.same(item, target), 1)
        # checks that 'lead' and 'gold' have 1 letter in common in the same position.


        item = 'lead'
        target = 'lead'
        self.assertEqual(self.test.same(item, target), 4)
        # checks that 'lead' and 'lead' have 4 letter in common in the same position.

    def test_build(self):
        # tests for the build function in the test_word_ladder.py file

        pattern = 'ti.e'
        words = ['hide', 'side', 'site', 'sits', 'sies', 'sees', 'seek']
        seen = {}
        list = ['lead', 'gold']
        self.assertEqual(self.test.build(pattern, words, seen, list), [])
        # tests that no words match the pattern 'ti.e' in the words list
        # with the '.' being a wildcard for any character.


        pattern = '.ide'
        words = ['hide', 'side', 'site', 'sits', 'sies', 'sees', 'seek']
        seen = {}
        list = ['lead', 'gold']
        self.assertEqual(self.test.build(pattern, words, seen, list), ['hide', 'side'])
        # tests that 'hide' and 'side' are found from the words list as they match the
        # pattern '.ide' with the '.' being a wildcard for any character.


        pattern = '.ide'
        words = ['hide', 'side', 'site', 'sits', 'sies', 'sees', 'seek']
        seen = {'hide': True, 'side': True}
        list = ['lead', 'gold']
        self.assertEqual(self.test.build(pattern, words, seen, list), [])
        # tests that even though 'hide' and 'side' match the pattern '.ide' with the '.' being
        # a wildcard for any character. They are not found because they are in the seen dictionary.


        pattern = '.ide'
        words = ['hide', 'side', 'site', 'sits', 'sies', 'sees', 'seek']
        seen = {'hide': True}
        list = ['lead', 'gold']
        self.assertEqual(self.test.build(pattern, words, seen, list), ['side'])
        # tests that even though 'hide' and 'side' match the pattern '.ide' with the '.' being
        # a wildcard for any character. 'side' is the only one that is output as 'hide' is in the seen dictionary.

    def test_find(self):
        # tests for the find function in the test_word_ladder.py file

        start = 'hide'
        words = ['hide', 'side', 'site', 'sits', 'sies', 'sees', 'seek']
        seen = {start: True}
        target = 'seek'
        path = []
        shortFlag = True
        self.assertTrue(self.test.find(start, words, seen, target, path, shortFlag))
        # checks if the path between 'hide' and 'seek' is found.


        start = 'hide'
        words = ['hide', 'side', 'sits', 'sies', 'sees', 'seek']
        seen = {start: True}
        target = 'seek'
        path = []
        shortFlag = True
        self.assertFalse(self.test.find(start, words, seen, target, path, shortFlag))
        # checks if the path between 'hide' and 'seek' cannot be found.


        words = []
        self.assertFalse(self.test.find(start, words, seen, target, path, shortFlag))
        # checks if the list has zero words in it

    def test_notAllowed(self):
        # tests for the notAllowed function in the test_word_ladder.py file


        exWordFile = 'notallowed.txt'
        words = ['lead', 'load', 'gold']
        remWordList = ['side', 'load', 'apple']
        self.assertEqual(self.test.notAllowed(words, exWordFile, remWordList), ['lead', 'gold'])
        # tests that words from the input list are removed from the main word list


        words = ['lead', 'load', 'gold']
        remWordList = []
        self.assertEqual(self.test.notAllowed(words, exWordFile, remWordList), ['lead', 'load', 'gold'])
        # tests that an empty word list does not remove words unintentionally


        exWordFile = False
        self.assertEqual(self.test.notAllowed(words, exWordFile, remWordList),
                         "That file either does not exist or is not a .txt file. Please try again.")
        # checks that the file exists otherwise the function produces an error message


        exWordFile = 'notallowed'
        self.assertEqual(self.test.notAllowed(words, exWordFile, remWordList),
                         "That file either does not exist or is not a .txt file. Please try again.")
        # checks that the file is a text file (.txt)

    def test_shortestPath(self):
        # tests for the shortestPath function in the test_word_ladder.py file

        self.assertTrue(self.test.shortestPath('yes'))
        self.assertTrue(self.test.shortestPath('y'))
        # tests that when the user inputs the expected characters to select the shortest path
        # the function return a 'True' value to let the program select the shortest path and proceed.


        self.assertFalse(self.test.shortestPath('no'))
        self.assertFalse(self.test.shortestPath('n'))
        # tests that when the user inputs the expected characters to not select the shortest path
        # the function return a 'False' value to let the program proceed with the long path.


        self.assertEqual(self.test.shortestPath('@'), "Answer unclear. Please try again")
        self.assertEqual(self.test.shortestPath('fadfafawe'), "Answer unclear. Please try again")
        self.assertEqual(self.test.shortestPath('yesyes'), "Answer unclear. Please try again")
        self.assertEqual(self.test.shortestPath('yy'), "Answer unclear. Please try again")
        # tests that various incorrect user inputs for the function return an error.


        shortFlag = None
        self.assertEqual(self.test.shortestPath(shortFlag), "Answer unclear. Please try again")
        # tests that the program does not break if no value is input into the function.

    def test_mainProgram(self):
        # tests for the mainProgram function in the test_word_ladder.py file

        startWord = 'lead'
        targetWord = 'gold'
        fileName = 'dictionary.txt'
        excludeWords = 'n'
        exWordFile = 'notallowed.txt'
        remWordList = ['side', 'load', 'apple']
        # initial variable setup for mainProgram tests


        shortest = 'YES'
        self.assertEqual(self.test.mainProgram(startWord, targetWord, fileName, shortest, excludeWords, exWordFile,
                                               remWordList), (3, ['lead', 'load', 'goad', 'gold']))
        # tests that the shortest path inputs can be entered in uppercase and are converted using the .lower() method.


        shortest = 'n'
        self.assertEqual(self.test.mainProgram(startWord, targetWord, fileName, shortest, excludeWords, exWordFile,
                                               remWordList), (8, ['lead', 'bead', 'bend', 'band', 'bard', 'bird',
                                                                  'gird', 'gild', 'gold']))
        shortest = 'y'
        self.assertEqual(self.test.mainProgram(startWord, targetWord, fileName, shortest, excludeWords, exWordFile,
                                               remWordList), (3, ['lead', 'load', 'goad', 'gold']))
        # tests that the shortest path inputs accept the expected inputs.


        excludeWords = 'NO'
        self.assertEqual(self.test.mainProgram(startWord, targetWord, fileName, shortest, excludeWords, exWordFile,
                                               remWordList), (3, ['lead', 'load', 'goad', 'gold']))
        # tests that the excludeWords inputs can be entered in uppercase and are converted using the .lower() method.


        excludeWords = 'n'
        self.assertEqual(self.test.mainProgram(startWord, targetWord, fileName, shortest, excludeWords, exWordFile,
                                               remWordList), (3, ['lead', 'load', 'goad', 'gold']))
        excludeWords = 'no'
        self.assertEqual(self.test.mainProgram(startWord, targetWord, fileName, shortest, excludeWords, exWordFile,
                                               remWordList), (3, ['lead', 'load', 'goad', 'gold']))
        excludeWords = 'y'
        self.assertEqual(self.test.mainProgram(startWord, targetWord, fileName, shortest, excludeWords, exWordFile,
                                               remWordList), (4, ['lead', 'read', 'road', 'goad', 'gold']))
        excludeWords = 'yes'
        self.assertEqual(self.test.mainProgram(startWord, targetWord, fileName, shortest, excludeWords, exWordFile,
                                               remWordList), (4, ['lead', 'read', 'road', 'goad', 'gold']))
        # tests that the excludeWords inputs accept the expected inputs.


        excludeWords = '@'
        self.assertEqual(self.test.mainProgram(startWord, targetWord, fileName, shortest, excludeWords, exWordFile,
                                               remWordList), "Answer unclear. Please try again")
        excludeWords = 'fadfafawe'
        self.assertEqual(self.test.mainProgram(startWord, targetWord, fileName, shortest, excludeWords, exWordFile,
                                               remWordList), "Answer unclear. Please try again")
        excludeWords = 'yesyes'
        self.assertEqual(self.test.mainProgram(startWord, targetWord, fileName, shortest, excludeWords, exWordFile,
                                               remWordList), "Answer unclear. Please try again")
        excludeWords = 'yy'
        self.assertEqual(self.test.mainProgram(startWord, targetWord, fileName, shortest, excludeWords, exWordFile,
                                               remWordList), "Answer unclear. Please try again")
        # tests that various incorrect user inputs for the mainProgram function return an error.


        excludeWords = 'n'
        startWord = 'LEAD'
        targetWord = 'gold'
        self.assertEqual(self.test.mainProgram(startWord, targetWord, fileName, shortest, excludeWords, exWordFile,
                                               remWordList), (3, ['lead', 'load', 'goad', 'gold']))
        # tests that the starting word inputs can be entered in uppercase and are converted using the .lower() method.


        startWord = '  lead  '
        targetWord = 'gold'
        self.assertEqual(self.test.mainProgram(startWord, targetWord, fileName, shortest, excludeWords, exWordFile,
                                               remWordList), (3, ['lead', 'load', 'goad', 'gold']))
        # tests that the starting word inputs can be entered with additional spaced before or after and are converted
        # using the .strip() method


        startWord = 'lead'
        targetWord = 'GOLD'
        self.assertEqual(self.test.mainProgram(startWord, targetWord, fileName, shortest, excludeWords, exWordFile,
                                               remWordList), (3, ['lead', 'load', 'goad', 'gold']))
        # tests that the target word inputs can be entered in uppercase and are converted using the .lower() method.


        startWord = 'lead'
        targetWord = '   gold   '
        self.assertEqual(self.test.mainProgram(startWord, targetWord, fileName, shortest, excludeWords, exWordFile,
                                               remWordList), (3, ['lead', 'load', 'goad', 'gold']))
        # tests that the target word inputs can be entered with additional spaced before or after and are converted
        # using the .strip() method


        fileName = False
        self.assertEqual(self.test.mainProgram(startWord, targetWord, fileName, shortest, excludeWords, exWordFile,
                                               remWordList), "That file does not exist or is not a .txt file. Please "
                                                             "try again.")
        # checks that the dictionary file exists otherwise the function produces an error message.


        fileName = 'dictionary'
        self.assertEqual(self.test.mainProgram(startWord, targetWord, fileName, shortest, excludeWords, exWordFile,
                                               remWordList), "That file does not exist or is not a .txt file. Please "
                                                             "try again.")
        # checks that if the dictionary file is not a text file (.txt) it returns an error message.


        fileName = 'dictionary.txt'
        startWord = ''
        self.assertEqual(self.test.mainProgram(startWord, targetWord, fileName, shortest, excludeWords, exWordFile,
                                               remWordList), "No path found")
        # checks that if there is no path the message 'no path found' is returned.


if __name__ == '__main__':
    unittest.main()