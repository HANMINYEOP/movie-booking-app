from flask import Flask
from auth import login
from booking import reserve_seat

app = Flask(__name__)

@app.route('/')
def home():
    return "🎬 영화 예매 앱에 오신 것을 환영합니다!"

@app.route('/login')
def login_route():
    return login("user1", "pass123")

@app.route('/reserve')
def reserve_route():
    return reserve_seat("user1", "영화 A", "A5")

if __name__ == '__main__':
    app.run(debug=True)
