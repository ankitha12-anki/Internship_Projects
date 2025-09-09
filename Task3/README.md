## Task3: Sentiment Aanlysis using Flask + Textblob

---

### Requirements:
- Python 3.x
- Flask
- TextBlob
- ```Install using:
    pip install flask textblob
    python -m textblob.download_corpora   # run once if needed


### Steps to Run:
1. Open Anaconda Prompt.
2. ```Navigate to Task3 folder and Run the Flask app:
       cd Internship_Projects/Task3
       python app.py
3. ```Open in browser:
       http://127.0.0.1:5000/

### Example Inputs & Outputs:

Input: "I love this app!" <br>
Output: Sentiment = Positive | Polarity = 0.60 | Subjectivity = 0.75 <br><br>

Input: "I hate waiting in long queues." <br>
Output: Sentiment = Negative | Polarity = -0.80 | Subjectivity = 0.90 <br><br>

Input: "The book is on the table." <br>
Output: Sentiment = Neutral | Polarity = 0.00 | Subjectivity = 0.10


### Observations:
- Polarity > 0.1 → Positive
- Polarity < -0.1 → Negative
- Between -0.1 and 0.1 → Neutral
- Subjectivity: 0 = fact, 1 = opinion

### Screenshots
1. [Screenshot](ex1.png.png)
2. [Screenshot1](ex2.png.png)
3. [Screenshot2](ex3.png.png)
4. [Screenshot1](ex4.png.png)

 [Click here to watch screen recording](output.mp4)
 
### Conclusion:
This project shows how Flask + TextBlob can be used to build a simple 
Sentiment Analysis web app with an interactive interface.
