# My Adventures With Wordle
## Intro
For those few of you who haven't heard of the hit game Wordle by Josh Wardle you should play it yourself [here](https://www.powerlanguage.co.uk/wordle/).  
  
This repo and code is my attempt at making a Wordle bot as a fun side project for myself. After seeing several videos on Tik Tok about the best first word to guess with I decided to make a bot for solving Wordle. I'm sure others have already done this but this is my attempt.  


## Step 1
My end goal was to have a bot that can solve the real web version of Wordle using something like Selenium to execute the commands. For testing purposes though I created a local instance of Wordle to use in this [file](wordleBoard.py).  
  
This was a playable non-bot version that only has terminal input and output.  
  
This helped me get the Wordle game working locally before I made a second version of it for use by my bot [here](wordleBoardForBot.py).  
  
## Step 2
Now I needed to create the bot. I thought about what I did badly at the game. The main thing that I struggle with is completely eliminating invalid words. For instance if I use my old faithful first guess "soare" and "e" is eleiminated, I find it hard to never use a word containing "e" later. A bot would be great at this though. So I decided I would keep a list of invalid letters and eliminate any word that contains those. I was seeing great progress with that idea. With a starting list size of around 6,000 words. After one guess of "soare" I would usually have less than a 1,000 words just from that elimination. But Wordle gives more feedback. Green if your letter is in the word and in the right spot. And yellow if your letter is in the word but in the wrong place. So how to represent these to a bot? I decided on an array of characters to represent each letter such as below:
```python
['X','X','X','O','O']
```
An ```X``` represents that the letter cannot be in that location. For example if I guessed "soare" and got back gray, gray, gray, yellow, gray I know that "r" cannot be the 2nd to last letter in the word. So it will be displayed as ```['O','O','O','X','O']```. An ```O``` means that it is as possible place for the letter.  
  
From there my code can simple eliminate any word that has an "r" in the second to last location. This further eleminates the possible words. And from testing with the starting word "soare" typically gets the list of available words down to less than 100 which is about 1.7% of the initial wordbank.

## Step 3
The way I implemented this into my bot was to create a letter class that had a match method that returned a boolean depending on if the word it was tested against could coincide with it's placement. From there you can simply test each available letter against the wordbank and eliminate any word that draws a ```False``` return. The main issue in my approach lies in my choice of the next word to guess which I do randomly from the wordbank.

## Step 4
My method of choosing the word stated above is problematic. It leaves part of the bot's success up to chance. This creates inconsistent results. Running my bot against 1,000 games of Wordle I got a success rate of **65.5%** seen on line #93006 [here](firstAlgoResults.txt). This was less than satisfactory so I devised a better way to choose the bot's next guess.

## Step 5
To choose the bot's next guess I wanted to use letter frequency to determine the ideal word. Scanning my 6,000 line wordbank I assembled each letter's frequency of words this does not include repeat letters such as n in "funny". The results are in this [list](frequency.txt) which is in alphabetical order. A new class ```FrequencyMaker``` assembles the results in a dictionary. A method in ```FrequencyMaker``` then returns the highest scoring word out of a list of words. I thought this method was sure to have amazing results. Surely enough it didn't. My results which are [here](secondAlgoResults.txt), showed a **52.1%** success rate out of 1,000 games. This puzzles me, because sure the random choosing of a word is bound to have a lucky game, but for every really good game there should be an equally bad game. But the random choosing is consistently better than my letter frequency system. I will be going over my code further to determine the cause of failure. Hopefully my implementation is flawed and the idea itself is sound, we shall see.