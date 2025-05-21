# 🎬 영화 예매 앱 시뮬레이션 (Flask 기반)

## ✅ 개요
영화 예매 앱의 일상적인 사용 시나리오를 시퀀스 다이어그램으로 모델링하고, 이를 기반으로 실제 동작하는 샘플 코드를 Flask로 구현했습니다.

---

## 📌 구성 파일

| 파일명             | 설명 |
|------------------|------|
| `app.py`           | 메인 Flask 앱 실행 파일 |
| `auth.py`          | 사용자 로그인 처리 |
| `booking.py`       | 좌석 예약 처리 |
| `requirements.txt` | 필요한 라이브러리 (Flask) |
| `README.md`        | 프로젝트 설명 문서 |

---

## 🛠 실행 방법

```bash
# 1. 가상환경 생성 (선택)
python -m venv venv
source venv/bin/activate  # Windows는 venv\Scripts\activate

# 2. 라이브러리 설치
pip install -r requirements.txt

# 3. 앱 실행
python app.py
