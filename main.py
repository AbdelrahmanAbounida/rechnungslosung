# Here u can check the sol results for both aufgaben 

from losung.aufgabe1 import task1
from losung.aufgabe2 import task2
from dotenv import load_dotenv

load_dotenv()


if __name__ == '__main__':
    task2()
    # task2() # Before running task2 make sure to add GOOGLE_GEMINI_APIKEY to your .env