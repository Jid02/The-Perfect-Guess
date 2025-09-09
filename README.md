# 🎮 The Perfect Guess Game  

An upgraded Python-based number guessing game with **levels, hints, scoring system, and leaderboard**.  
Test your luck and logic while progressing through increasing levels of difficulty.  

---------------------------------------------------------------------------------------------------------------------

## 🚀 Features  
- ✅ **Three Levels**:  
  - Level 1: Easy (1–50, 10 attempts)  
  - Level 2: Medium (1–100, 7 attempts)  
  - Level 3: Hard (1–500, 5 attempts)  

- ✅ **Smart Hints**: Get hints whether the number is higher/lower and whether it’s odd/even.  
- ✅ **Scoring System**: Earn points based on how quickly you guess correctly.  
- ✅ **Progressive Unlocks**: Beat a level to unlock the next one.  
- ✅ **Leaderboard**: Saves top scores in a `leaderboard.txt` file.  
- ✅ **Replayability**: Compete with friends and improve your ranking.  

------------------------------------------------------------------------------------------------------------------------

## 🖥️ How It Works  
1. Enter your name and view the **current leaderboard**.  
2. Start from **Level 1** with a random number in a fixed range.  
3. Each wrong guess reduces your attempts, but gives you a **hint**.  
4. Guess correctly to earn points and unlock the next level.  
5. If you fail, your **score is saved** to the leaderboard.  
6. The leaderboard displays the top 5 players.  

---------------------------------------------------------------------------------------------------------------------------

## 🏗️ Code Overview  

### 🎯 Game Flow
- The `play_level()` function handles each level’s logic.  
- The player gets limited attempts based on difficulty.  
- Correct guesses award **bonus points** (fewer attempts = higher score).  

### 🏆 Leaderboard
- Scores are stored in `leaderboard.txt`.  
- The `save_score()` and `display_leaderboard()` functions manage storing and showing top players.  

### 💡 Hint System
- The `give_hint()` function gives extra help:  
  - Whether the secret number is **higher/lower** than the guess  
  - Whether the secret number is **odd/even**  

------------------------------------------------------------------------------------------------------------------------------

## 📂 Project Structure  

The-Perfect-Guess/

│

├── The_Perfect_Guess.py # Main game file

├── leaderboard.txt # Stores top scores (auto-created)

├── README.md # Project documentation

----------------------------------------------------------------------------------------------------------------------------------

## ⚡ How to Run  

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/The-Perfect-Guess.git
   
2. Navigate to the folder:
   
     cd The-Perfect-Guess

4. Run the game:
   
     python The_Perfect_Guess.py

---------------------------------------------------------------------------------------------------------------------------------------

## 🎮 Example Gameplay

🎮 Welcome to The Perfect Guess Game 🎮

🏆 Leaderboard 🏆
1. Alex - 150 points
2. Sarah - 120 points

Enter your name: John

🔹 Level 1: Easy (Guess between 1–50)

Attempt 1/10 - Enter your guess: 25
❌ Too low!
Hint: The number is greater than 25 and it’s even.

Attempt 2/10 - Enter your guess: 42
🎉 Correct! You guessed the number 42 in 2 attempts.
🏆 You earned 90 points. Total Score: 90

✅ Congrats John! You unlocked Level 2!

-----------------------------------------------------------------------------------------------------------------------------------------------

## 📌 Future Enhancements

1. Add multiplayer mode
2. Create a GUI version with Tkinter or PyGame
3. Add a timer mode for speed challenges

------------------------------------------------------------------------------------------------------------------------------------------------

## 🏆 About
Made with ❤️ in Python as a fun beginner-friendly project to practice:

1. Loops
2. Conditionals
3. File handling
4. Leaderboards
5. Game logic

