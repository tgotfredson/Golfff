# Golf Tournament App Prototype

## Overview

This is a simple web-based application for inputting golf scores, calculating weighted scores based on course difficulty, and displaying a leaderboard. The goal is to allow golfers to compete on different courses, while normalizing scores based on the difficulty of each course, so they can compare results fairly.

### Features:
- Input the golf course name, score, and handicap.
- Real-time course search with suggestions as you type.
- Automatic retrieval of the course difficulty index.
- Calculation of a weighted score using the formula: `(Score - Handicap) * (113 / Difficulty Index)`.
- A leaderboard that displays the courses played and weighted scores.
  
### Leaderboard
The leaderboard tracks each player’s weighted score for the current month, allowing them to compare their performance with others who may have played on different courses.

---

## Setup Instructions

1. **Download or Clone the Repository**
   - Download the `index.html` and `README.md` files or clone the repository to your local machine.

2. **Open the App**
   - Simply open the `index.html` file in any web browser to use the app.

3. **How to Use**
   - In the "Golf Course" field, start typing the name of a course. The app will suggest course names based on the pre-defined list.
   - Select a course from the list to auto-populate its difficulty index.
   - Input your score and handicap, then press "Submit Score" to add your result to the leaderboard.
   - The app will calculate your weighted score and display it on the leaderboard.

### Course List
- The following courses and their difficulty indices are available by default:
  - Pebble Beach (75.1)
  - Augusta National (78.3)
  - St. Andrews (73.2)
  - Pinehurst No. 2 (76.0)

You can modify the `courses` variable inside `index.html` to add more golf courses and their difficulty indices.

---

## Future Enhancements

- Add user authentication to save each golfer's scores.
- Expand the golf course database by connecting to a live course database API.
- Enhance the leaderboard to support multiple months or seasons of tournaments.
- Include additional metrics or graphs to analyze golfer performance over time.

---

## License
This project is for prototyping purposes and is not intended for commercial use. Feel free to modify it as needed for personal use.

