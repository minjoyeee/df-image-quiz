from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import datetime
import random

app = Flask(__name__)

# 데이터 경로
DATA_DIR = 'data'
QUESTIONS_FILE = os.path.join(DATA_DIR, 'questions.json')
SCORES_FILE = os.path.join(DATA_DIR, 'scores.json')


# JSON 파일 읽기
def load_json(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []


# JSON 파일 저장
def save_json(filepath, data):
    os.makedirs(os.path.dirname(filepath) or '.', exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# 메인 페이지
@app.route('/')
def index():
    return render_template('index.html')


# 게임 페이지
@app.route('/game')
def game():
    return render_template('game.html')


# API: 20개 문제 랜덤 선택
@app.route('/api/questions', methods=['GET'])
def get_questions():
    questions = load_json(QUESTIONS_FILE)
    
    if len(questions) < 20:
        return jsonify({'error': '문제가 20개 미만입니다'}), 400
    
    # 전체 100개 중 랜덤 20개 선택
    selected_questions = random.sample(questions, 20)
    
    return jsonify(selected_questions)


# API: 정답 확인
@app.route('/api/check-answer', methods=['POST'])
def check_answer():
    data = request.get_json()
    question_id = data.get('question_id')
    user_answer = data.get('answer', '').strip()
    
    questions = load_json(QUESTIONS_FILE)
    
    # 질문 찾기
    question = next((q for q in questions if q['id'] == question_id), None)
    
    if not question:
        return jsonify({'error': '질문을 찾을 수 없습니다'}), 404
    
    # 띄어쓰기 무시하고 비교
    correct_answer = question['answer'].replace(' ', '')
    user_answer_normalized = user_answer.replace(' ', '')
    
    is_correct = correct_answer == user_answer_normalized
    
    return jsonify({
        'correct': is_correct,
        'answer': question['answer']
    })


# API: 점수 저장
@app.route('/api/save-score', methods=['POST'])
def save_score():
    data = request.get_json()
    nickname = data.get('nickname', 'Anonymous').strip()
    score = data.get('score', 0)
    
    if not nickname:
        return jsonify({'error': '닉네임을 입력해주세요'}), 400
    
    scores = load_json(SCORES_FILE)
    
    new_score = {
        'id': len(scores) + 1,
        'nickname': nickname,
        'score': score,
        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    scores.append(new_score)
    scores.sort(key=lambda x: x['score'], reverse=True)  # 점수순 정렬
    
    save_json(SCORES_FILE, scores)
    
    return jsonify({'success': True, 'rank': len(scores)})


# API: 리더보드 조회
@app.route('/api/leaderboard', methods=['GET'])
def get_leaderboard():
    scores = load_json(SCORES_FILE)
    return jsonify(scores[:100])  # 상위 100개만


# 결과 페이지
@app.route('/result')
def result():
    return render_template('result.html')


# 리더보드 페이지
@app.route('/leaderboard')
def leaderboard():
    return render_template('leaderboard.html')


if __name__ == '__main__':
    app.run(debug=True)