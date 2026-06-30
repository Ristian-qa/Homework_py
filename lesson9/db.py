from sqlalchemy import create_engine, text


class Student:
    # подключение к бд
    def __init__(self, db_path):
        self.engine = create_engine(f"sqlite:///{db_path}")

    # добавление нового студента
    def create_student(self, user_id, level, education_form, subject_id):
        with self.engine.connect() as conn:
            result = conn.execute(
                text(
                    "INSERT INTO student (user_id, level, education_form, "
                    "subject_id) VALUES (:user_id, :level, :education_form, "
                    ":subject_id)"
                ),
                {
                    "user_id": user_id,
                    "level": level,
                    "education_form": education_form,
                    "subject_id": subject_id
                }
            )
            conn.commit()
            return result.lastrowid

    # получение студента по user_id
    def get_student_by_user_id(self, user_id):
        with self.engine.connect() as conn:
            result = conn.execute(
                text("SELECT * FROM student WHERE user_id = :user_id"),
                {"user_id": user_id}
            )
            return result.mappings().first()

    # получение всех студентов
    def get_all_students(self):
        with self.engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM student"))
            return result.mappings().all()

    # обновление данных студента
    def update_student(self, user_id, level=None, education_form=None,
                       subject_id=None):
        with self.engine.connect() as conn:
            updates = []
            params = {"user_id": user_id}

            if level is not None:
                updates.append("level = :level")
                params["level"] = level
            if education_form is not None:
                updates.append("education_form = :education_form")
                params["education_form"] = education_form
            if subject_id is not None:
                updates.append("subject_id = :subject_id")
                params["subject_id"] = subject_id

            if not updates:
                return

            query = (
                f"UPDATE student SET {', '.join(updates)} "
                "WHERE user_id = :user_id"
            )
            conn.execute(text(query), params)
            conn.commit()

    # удаление студента
    def delete_student(self, user_id):
        with self.engine.connect() as conn:
            conn.execute(
                text("DELETE FROM student WHERE user_id = :user_id"),
                {"user_id": user_id}
            )
            conn.commit()

    # очистка после теста
    def cleanup_student(self, user_id):
        try:
            self.delete_student(user_id)
        except Exception:
            pass
