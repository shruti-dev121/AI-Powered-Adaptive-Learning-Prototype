+-------------------+
|  User Input       |  <-- Name, Starting Level (Easy/Medium/Hard)
+-------------------+
          |
          v
+-------------------+
| Puzzle Generator  |  <-- Generates addition, subtraction,
|                   |      multiplication, or division problems
+-------------------+
          |
          v
+-------------------+
| Performance       |  <-- Tracks correctness and response time
| Tracker           |
+-------------------+
          |
          v
+-------------------+
| Adaptive Engine   |  <-- ML-based logic predicts next difficulty
|                   |
+-------------------+
          |
          v
+-------------------+
| Session Summary   |  <-- Displays accuracy, average time,
|                   |      recommended next level
+-------------------+



2. Adaptive Logic Used

Model: Logistic Regression (lightweight, fast, interpretable).

Features:

1.Last N puzzle correctness (e.g., last 3 answers)
2.Average response time
3.Current difficulty level (encoded numerically)
Prediction:
#Model predicts the next difficulty level (Easy, Medium, Hard).

##Rule-Based Fallback (Optional)
If ML is unavailable, a simple rule can be applied:

Accuracy > 80% → increase difficulty

Accuracy 50–80% → maintain current level

Accuracy < 50% → decrease difficulty

Why This Approach

Personalization: ML predicts difficulty based on individual performance trends, unlike fixed rules.
Lightweight: Logistic Regression ensures fast computation suitable for kids’ learning sessions.

Demo Video: [Watch on Google Drive]:https://drive.google.com/file/d/1Br1yMeYEzc9U4TQIlAVKtjfJN1V3343_/view?usp=sharing

