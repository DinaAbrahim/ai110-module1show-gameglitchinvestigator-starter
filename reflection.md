# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The setup of the game looked correct. It had a place to enter the guess, buttons to submit the guess, start a new game, and turn off the hints. 
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
The hints seemed to be backwards. It said go higher when it should have said go lower and vice-versa. The score given at the end of the game did not make sense. I couldn't tell what the score was based off of. 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The AI suggested that the bug with go higher/lower hints was that the hints were switched. I looked through the code and agreed with what the AI suggested. 
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
When I tried adding a pytest, the AI wanted me to add a new test file. It didn't realize that I already had one. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I made a pytest with the help of AI and ran it. I also played the game and verified that the test worked. 
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
A manual test I ran to test the go higher/lower bug was inputting my guess and seeing what hint was given. I checked what the secret was and whether the hint made sense, knowing which hint it was supposed to give me. 
- Did AI help you design or understand any tests? How?
Yes. I used AI to design the pytests. 

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
One strategy I liked was testing the game as a user and seeing how many bugs I could find, without looking at the code. 
- What is one thing you would do differently next time you work with AI on a coding task?
I would spend more time thinking about how I would fix the bugs before asking AI to help me.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project showed me how useful AI can be to code, especially to make test cases. However, the AI did make some mistakes, so it's important to double-check. 