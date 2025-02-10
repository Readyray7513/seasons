# 🎉 Minutes Lived Calculator

This Python script calculates the total number of minutes you've been alive and converts the result into words.

## 🚀 How It Works
1. **Input your birth date** in `YYYY-MM-DD` format.
2. The script calculates the total minutes since your birth.
3. It converts the number into words (e.g., **"Five hundred twenty-five thousand, six hundred minutes"**).
4. It prints the result.

## 🛠 Installation
You'll need **Python 3** and the `inflect` library installed.
pip install inflect

▶️ Usage
Run the script in a terminal:
python seasons.py
Enter your birth date when prompted.

🧪 Running Tests
The project includes pytest tests. To run them, use:
pytest test_seasons.py

📂 File Structure
seasons.py – Main script.
test_seasons.py – Unit tests for functions.

🔍 Example Output
(YYYY-MM-DD): 1999-01-01
Five hundred twenty-five thousand, six hundred minutes

📝 Notes
The script exits if you enter an invalid date.
It automatically capitalizes the first letter of the output.
Enjoy tracking your minutes lived! ⏳✨
