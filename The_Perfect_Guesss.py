import random
import time
import os

# ---------------- Leaderboard Functions ---------------- #
def load_leaderboard():
    if not os.path.exists("leaderboard.txt"):
        return {}
    scores = {}
    with open("leaderboard.txt", "r") as f:
        for line in f.readlines():
            name, score = line.strip().split(":")
            score = int(score)
            if name not in scores or score > scores[name]:
                scores[name] = score
    return scores

def save_score(name, score):
    scores = load_leaderboard()
    if name not in scores or score > scores[name]:
        scores[name] = score
    with open("leaderboard.txt", "w") as f:
        for n, s in scores.items():
            f.write(f"{n}:{s}\n")

def display_leaderboard():
    print("\n🏆 Leaderboard 🏆")
    scores = load_leaderboard()
    if not scores:
        print("No scores yet. Be the first to play!")
        return
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for i, (name, score) in enumerate(sorted_scores[:5], start=1):  
        print(f"{i}. {name} - {score} points")

# ---------------- Game Functions ---------------- #
def give_hint(secret, guess):
    parity = "even" if secret % 2 == 0 else "odd"
    if guess < secret:
        return f"Hint: The number is greater than {guess} and it’s {parity}."
    else:
        return f"Hint: The number is smaller than {guess} and it’s {parity}."

def play_level(level, player_name, score):
    """Plays one level and returns updated score and success status"""
    if level == 1:
        secret = random.randint(1, 50)
        attempts_allowed = 10
        print("\n🔹 Level 1: Easy (Guess between 1–50)")
    elif level == 2:
        secret = random.randint(1, 100)
        attempts_allowed = 7
        print("\n🔸 Level 2: Medium (Guess between 1–100)")
    else:
        secret = random.randint(1, 500)
        attempts_allowed = 5
        print("\n🔥 Level 3: Hard (Guess between 1–500)")

    guesses = 0
    found = False

    while guesses < attempts_allowed:
        guess = int(input(f"\nAttempt {guesses+1}/{attempts_allowed} - Enter your guess: "))
        guesses += 1
        time.sleep(0.5)
        print("⏳ Checking your guess...")
        time.sleep(0.7)

        if guess == secret:
            print(f"🎉 Correct! You guessed the number {secret} in {guesses} attempts.")
            gained = max(10, (attempts_allowed - guesses + 1) * 10)  # bonus for fewer attempts
            score += gained
            print(f"🏆 You earned {gained} points. Total Score: {score}")
            found = True
            break
        elif guess > secret:
            print("❌ Too high!")
        else:
            print("❌ Too low!")

        print(give_hint(secret, guess))

    if not found:
        print(f"\n😢 Game Over! The number was {secret}. Final Score: {score}")
        save_score(player_name, score)
        return score, False  

    return score, True  

# ---------------- Main Game ---------------- #
print("🎮 Welcome to The Perfect Guess Game 🎮")
display_leaderboard()

player_name = input("\nEnter your name: ")
score = 0
level = 1

# Progressive Levels
while level <= 3:
    score, success = play_level(level, player_name, score)
    if not success:
        break  
    if level < 3:
        print(f"\n✅ Congrats {player_name}! You unlocked Level {level+1}!")
    level += 1

if level > 3:
    print(f"\n🏆 Congratulations {player_name}! You completed all levels with a score of {score}")
    save_score(player_name, score)

print("\n📜 Updated Leaderboard:")
display_leaderboard()
