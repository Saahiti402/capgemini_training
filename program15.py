M = input("Enter move by A :").strip()
win = {
    "rock": "Paper",
    "paper": "Scissors",
    "scissors": "Rock"
}
print("Winning move by B : ", win[M])