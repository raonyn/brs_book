####################################
python+django+postgresql Study
####################################

python 및 VSCode가 설치 되어있고 연동 되어 있다는 가정입니다.
Postgresql 설치를 완료하고 계정과 데이터베이스를 생성하고 로그인 권한까지 부여한 상태입니다.

1. mkdir venv 디렉토리 생성

2. python -m venv "가상환경"

3. VSCode를 실행하고 "파일>폴더열기"에서 새로 만든 가상환경 폴더를 연다

4. F1을 누르고 python select interpreter 입력 => Enter interpreter path 선택 > find.. 선택 > venv/가상환경/Script/python.exe 선택

5. 터미털에서 새터미널을 열고 +버튼 눌러 powershell 창 열기

6. (가상환경이름) 가상환경이름...> 형태로 Powershell 창이 열림. 가상환경으로 진행 가능 상태

---------- django  설치 -------

7. (가상환경이름) 가상환경이름...> py.exe -m pip install --upgrade pip

8. (가상환경이름) 가상환경이름...> pip install Django

--------- 프로젝트 환경 설정 ---------

9. 프로젝트 생성
  (가상환경이름) 가상환경이름...> django-admin startproject "프로젝트명" .
  주의) 끝에 "."을 빼먹으면 곤란하다.

10. 서버 실행
  (가상환경이름) 가상환경이름...> cd "프로젝트명"
  (가상환경이름) 프로젝트경로...> py.exe manager.py runserver
  웹브라우저에서 http://127.0.0.1:8000 접속하여 기본 페이지 뜨는지 확인

11. 설정을 맞춰 준다.
./settings.py

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

12. PostGresql 연동 모듈 설치
 pip install psycopg2

13. settings.py DATABASES 변경

   #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgresql_db',
        'USER': 'admin',
        'PASSWORD': 'Admin!0',
        'HOST': 'localhost',
        'PORT': '5432',

14. migrate 
항상 무언가를 진행하고 모델의 변경점이 생길 때 마다 마이그레이션 실행해주는 것이 좋다.

DB migrate 상태확인
DB migrate 대상 만들기
DB migrate 수행

py.exe .\manage.py showmigrations
py.exe .\manage.py makemigrations
py.exe .\manage.py migrate 

------------ 추가 앱 설정 -----------------

15. 어플리케이션 생성 => 프로젝트명 하위로 여러개 어플리케이션 생성
 (가상환경이름) 프로젝트경로...> python manage.py startapp "앱1"
 (가상환경이름) 프로젝트경로...> python manage.py startapp "앱2"

py manager.py startapp account
py manager.py startapp brs_app


15. settings.py INSTALLED_APPS에 추가

16. 앱 모델 추가
