from sqlalchemy import text
from db import Student

# Подключение к базе данных
db = Student("/Users/admin/Desktop/firstbd")


# добавление нового студента
def test_add_student():
    # подготовка данных
    user_id = 99999
    level = "Intermediate"
    education_form = "group"
    subject_id = 1

    # добавляем студента
    db.create_student(user_id, level, education_form, subject_id)

    # проверяем, что студент появился в БД
    created = db.get_student_by_user_id(user_id)

    # проверяем, что все поля соответствуют ожиданиям
    assert created is not None, "Студент не создался!"
    assert created["user_id"] == user_id
    assert created["level"] == level
    assert created["education_form"] == education_form
    assert created["subject_id"] == subject_id

    # удаляем созданного студента
    db.cleanup_student(user_id)


# изменение данных студента
def test_edit_student():
    # подготовка
    user_id = 99998
    db.create_student(user_id, "Beginner", "personal", 2)

    # изменение данных
    db.update_student(
        user_id,
        level="Upper-Intermediate",
        education_form="group",
        subject_id=3
    )

    # проверяем, что данные обновились в БД
    updated = db.get_student_by_user_id(user_id)

    # проверяем, что все поля обновились корректно
    assert updated is not None, "Студент не найден после обновления!"
    assert updated["level"] == "Upper-Intermediate"
    assert updated["education_form"] == "group"
    assert updated["subject_id"] == 3

    # удаляение
    db.cleanup_student(user_id)


# удаление студента
def test_delete_student():
    # подготовка
    user_id = 99997
    db.create_student(user_id, "Advanced", "personal", 4)

    # проверяем, что студент создался
    created = db.get_student_by_user_id(user_id)
    assert created is not None, "Студент не создался!"

    # удаление студента
    db.delete_student(user_id)

    # проверяем, что студент удалился
    deleted = db.get_student_by_user_id(user_id)
    assert deleted is None, "Студент не удалился!"


# получение всех студентов из таблицы
def test_get_all_students():
    # получаем все строки из таблицы student
    all_students = db.get_all_students()

    # проверяем, что таблица не пустая
    assert len(all_students) > 0, "Таблица student пуста!"

    # проверяем структуру первой записи
    first_student = all_students[0]
    assert "user_id" in first_student
    assert "level" in first_student
    assert "education_form" in first_student
    assert "subject_id" in first_student

    # выводим информацию для наглядности
    print(f"Найдено {len(all_students)} студентов")


# проверка допустимых уровней студентов
def test_student_levels():
    # проверяем, что все уровни студентов валидны
    valid_levels = [
        "Beginner",
        "Elementary",
        "Pre-Intermediate",
        "Intermediate",
        "Upper-Intermediate",
        "Advanced"
    ]

    with db.engine.connect() as conn:
        placeholders = ", ".join(f"'{level}'" for level in valid_levels)
        result = conn.execute(
            text(
                f"SELECT COUNT(*) as count FROM student "
                f"WHERE level NOT IN ({placeholders})"
            )
        )
        count = result.mappings().first()["count"]

    assert count == 0, f"Найдено {count} записей с неверным уровнем"


# проверка, что subject_id существует в таблице subject
def test_subject_id_exists():
    with db.engine.connect() as conn:
        result = conn.execute(
            text(
                "SELECT COUNT(*) as count FROM student s "
                "LEFT JOIN subject sub ON s.subject_id = sub.subject_id "
                "WHERE sub.subject_id IS NULL"
            )
        )
        count = result.mappings().first()["count"]

    assert count == 0, f"Найдено {count} записей с несуществующим subject_id"
