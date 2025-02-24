설치 단계
1.GitHub에서 리포지토리 클론하기:
git clone https://github.com/changhy2001/django.git
cd django

2.가상환경 생성 및 활성화:
python -m venv venv
source venv/bin/activate   # macOS/Linux
# Windows의 경우: venv\Scripts\activate

3.필요한 패키지 설치:
pip install -r requirements.txt

실행 방법 (Daphne와 Nginx 사용)
1.Daphne (ASGI 서버) 실행:
daphne myproject.asgi:application --port 8000

2.Nginx 설정 및 실행:
brew services start nginx