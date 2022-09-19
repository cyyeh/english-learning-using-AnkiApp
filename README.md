# English Learning using AnkiApp

This repo contains scripts to parse English learning contents from the web and export them to `.csv` files. The content
format of `.csv` files is based on the specification from AnkiApp, a flashcard app to learn languages and more.

**The content format of `.csv` files**

The `.csv` file should have a row for each card in the deck, and up to (but not exceeding) 7 columns of data representing
the following:

1. text for front of card
2. text for back of card
3. (optional) list of tags, comma separated
4. (optional) filename for image on front of card
5. (optional) filename for image of back of card
6. (optional) filename of audio file for front of card
7. (optional) filename of audio file for back of card

## TODOs

- [x] hello-world test to export a naive `.csv` file
- [ ] parse English learning contents from the [web](https://basicenglishspeaking.com/)
  - [ ] [3000 most common words](https://basicenglishspeaking.com/3000-most-common-words/)
  - [ ] [100 common English phrases and sentence patterns(with dialogue)](https://basicenglishspeaking.com/100-common-phrases-and-sentence-patterns/)
  - [ ] [50 common English expressions and daily use English sentences](https://basicenglishspeaking.com/common-expressions-english/)
  - [ ] [181 common phrasal verbs](https://basicenglishspeaking.com/phrasal-verbs/)
  - [ ] [102 common English idioms](https://basicenglishspeaking.com/102-common-english-idioms/)
  - [ ] [75 daily english conversation practice](https://basicenglishspeaking.com/daily-english-conversation-topics/)
- [ ] export English learning contents to `.csv` files according to the specification of AnkiApp
