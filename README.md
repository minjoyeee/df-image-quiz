# 던파 이미지 퀴즈 (DF Image Quiz)

던전앤파이터(DFO)의 아이템, 몬스터, NPC 이미지를 보고 정답을 맞추는 웹 기반 퀴즈 게임입니다.

## 🎮 게임 규칙

- **총 20개 문제**: 전체 100개 문제 중 랜덤으로 20개 선택
- **점수 시스템**:
  - 정답: 100점
  - 힌트 사용 후 정답: 50점
  - 패스: 0점
- **입력 규칙**: 띄어쓰기는 무시되며, 오타는 인정되지 않음
- **피드백**: 정답/오답 즉시 표시

## ✨ 주요 기능

- ✅ 닉네임 기반 게임 플레이
- ✅ 실시간 점수 계산
- ✅ 힌트 기능 (첫 글자만 표시)
- ✅ 패스 기능 (모르는 문제 넘어가기)
- ✅ 자동 점수 저장
- ✅ 전체 리더보드 조회
- ✅ Enter 키로 정답 제출 및 다음 문제 이동

## 🛠️ 기술 스택

- **백엔드**: Flask (Python)
- **프론트엔드**: HTML, CSS (Tailwind CSS), JavaScript
- **데이터 저장**: JSON (questions.json, scores.json)
- **배포**: AWS EC2

## 📋 설치 및 실행

### 1. 저장소 클론
```bash
git clone https://github.com/minjoyeee/df-image-quiz.git
cd df-image-quiz
```

### 2. 가상환경 생성 및 활성화
```bash
# 가상환경 생성
python -m venv df_venv

# 활성화 (Windows)
df_venv\Scripts\activate

# 활성화 (Mac/Linux)
source df_venv/bin/activate
```

### 3. 필요한 패키지 설치
```bash
pip install -r requirements.txt
```

### 4. 애플리케이션 실행
```bash
python app.py
```

브라우저에서 `http://localhost:5000` 접속

## 📁 프로젝트 구조

```
df-image-quiz/
├── app.py                 # Flask 메인 애플리케이션
├── requirements.txt       # Python 패키지 의존성
├── README.md             # 이 파일
├── data/
│   ├── questions.json    # 퀴즈 문제 데이터 (id, image_path, answer)
│   └── scores.json       # 사용자 점수 기록
├── templates/
│   ├── index.html        # 메인 페이지 (닉네임 입력)
│   ├── game.html         # 게임 페이지
│   ├── result.html       # 결과 페이지
│   └── leaderboard.html  # 리더보드 페이지
└── static/
    ├── images/           # 퀴즈 이미지 파일들
    ├── css/
    └── js/
```

## 🔄 API 엔드포인트

| 메서드 | 엔드포인트 | 설명 |
|--------|-----------|------|
| GET | `/` | 메인 페이지 |
| GET | `/game` | 게임 페이지 |
| GET | `/result` | 결과 페이지 |
| GET | `/leaderboard` | 리더보드 페이지 |
| GET | `/api/questions` | 랜덤 20개 문제 조회 |
| POST | `/api/check-answer` | 정답 검증 |
| POST | `/api/save-score` | 점수 저장 |
| GET | `/api/leaderboard` | 리더보드 데이터 조회 |

## 📊 문제 데이터 포맷

`questions.json` 예시:
```json
[
  {
    "id": 1,
    "image_path": "/static/images/item_001.jpg",
    "answer": "황금거미"
  },
  {
    "id": 2,
    "image_path": "/static/images/monster_001.jpg",
    "answer": "검은빛귀"
  }
]
```

## 🎯 향후 계획

- [ ] 카테고리별 필터링 (아이템/몬스터/NPC)
- [ ] 난이도 선택 기능
- [ ] 일일 도전 미션
- [ ] 사용자별 통계 분석
- [ ] 친구 경쟁 모드
- [ ] 모바일 반응형 개선

## 👨‍💻 개발자

- **MINJONGKIM** - 개발 및 유지보수

## 📝 라이센스

이 프로젝트는 개인 프로젝트이며, 던전앤파이터는 Nexon의 등록 상표입니다.

## 📧 피드백

버그 리포트나 기능 제안은 GitHub Issues에 등록해주세요.