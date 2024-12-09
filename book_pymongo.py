from pymongo import MongoClient
from datetime import datetime

def insert_data():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.local  # 'local' 데이터베이스 사용

    # 책 데이터 삽입
    books = [
        {"title": "Kafka on the Shore", "author": "Haruki Murakami", "year": 2002},
        {"title": "Norwegian Wood", "author": "Haruki Murakami", "year": 1987},
        {"title": "1Q84", "author": "Haruki Murakami", "year": 2009}
    ]
    db.books.insert_many(books)

    # 영화 데이터 삽입
    movies = [
        {"title": "Inception", "director": "Christopher Nolan", "year": 2010, "rating": 8.8},
        {"title": "Interstellar", "director": "Christopher Nolan", "year": 2014, "rating": 8.6},
        {"title": "The Dark Knight", "director": "Christopher Nolan", "year": 2008, "rating": 9.0}
    ]
    db.movies.insert_many(movies)

    # 사용자 행동 데이터 삽입
    user_actions = [
        {"user_id": 1, "action": "click", "timestamp": datetime(2023, 4, 12, 8, 0)},
        {"user_id": 1, "action": "view", "timestamp": datetime(2023, 4, 12, 9, 0)},
        {"user_id": 2, "action": "purchase", "timestamp": datetime(2023, 4, 12, 10, 0)},
    ]
    db.user_actions.insert_many(user_actions)

    print("Data inserted successfully")
    client.close()

if __name__ == "__main__":
    insert_data()


# 문제1. 특정 장르의 책 찾기

def find_books_by_genre(db, genre):
    books_collection = db.books
    query = {"genre": genre}
    projection = {"_id": 0, "title": 1, "author": 1}

    books = books_collection.find(query, projection)
    for book in books:
        print(book)

    find_books_by_genre(db, "fantasy")


# 문제2. 감독별 평균 영화 평점 계산

def calulate_average_ratings(db):
    movies_collection = db.movies
    pipeline = [
        {"$group": {"_id": "$director", "average_rating": {"$avg": "$rating"}}},
        {"$sort": {"average_rating": -1}}
    ]

    results = movies_collection.aggregate(pipeline)
    for result in results:
        print(result)

    calulate_average_ratings(db)


# 문제3. 특정 사용자의 최근 행동 조회

def find_recent_actions_by_user(db, user_id, limit = 5):
    user_actions_collection = db.user_actions
    query = {"user_id": user_id}
    sort_criteria = [("timestamp", -1)]

    actions = user_actions_collection.find(query).sort(sort_criteria).limit(limit)
    for action in actions:
        print(action)

    find_recent_actions_by_user(db, 1)


# 문제4. 출판 연도별 책의 수 계산

def count_books_by_year(db):
    books_collection = db.books
    pipeline = [
        {"$group": {"_id": "$year", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ]

    results = book_collection.aggregate(pipeline)
    for result in results:
        print(result)

    count_books_by_year(db)


# 문제5. 특정 사용자의 행동 유형 업데이트

from datetime import datetime

def update_user_actions_before_date(db, user_id, date, old_action, new_action):
    user_actions_collection = db.user_action
    query = {"user_id": user_id, "action": old_action, "timestamp": {"$lt": datr}}
    update = {"$set": {"action": new_action}}

    result = user_actions_collection.update_many(query, update)
    print(f"updated {result.modified_count} documents.")

    update_user_actions_before_date(db, 1, datetime(2023, 4, 13), "view", "seen")