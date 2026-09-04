import os
from uuid import uuid4

from dotenv import load_dotenv
from sqlalchemy import create_engine, text


load_dotenv()

DB_CONNECTION_STRING = os.getenv("DB_CONNECTION_STRING")

db = create_engine(DB_CONNECTION_STRING)


def test_add_subject():
    subject_id = int(uuid4().int % 1000000000)
    subject_title = f"Test subject {uuid4()}"

    with db.begin() as connection:
        connection.execute(
            text(
                """
                INSERT INTO subject (subject_id, subject_title)
                VALUES (:subject_id, :subject_title)
                """
            ),
            {
                "subject_id": subject_id,
                "subject_title": subject_title,
            },
        )

        check = connection.execute(
            text(
                """
                SELECT subject_title
                FROM subject
                WHERE subject_id = :subject_id
                """
            ),
            {"subject_id": subject_id},
        ).scalar()

        assert check == subject_title

        connection.execute(
            text(
                """
                DELETE FROM subject
                WHERE subject_id = :subject_id
                """
            ),
            {"subject_id": subject_id},
        )


def test_update_subject():
    subject_id = int(uuid4().int % 1000000000)
    subject_title = f"Test subject {uuid4()}"
    new_title = f"Updated subject {uuid4()}"

    with db.begin() as connection:
        connection.execute(
            text(
                """
                INSERT INTO subject (subject_id, subject_title)
                VALUES (:subject_id, :subject_title)
                """
            ),
            {
                "subject_id": subject_id,
                "subject_title": subject_title,
            },
        )

        connection.execute(
            text(
                """
                UPDATE subject
                SET subject_title = :new_title
                WHERE subject_id = :subject_id
                """
            ),
            {
                "new_title": new_title,
                "subject_id": subject_id,
            },
        )

        check = connection.execute(
            text(
                """
                SELECT subject_title
                FROM subject
                WHERE subject_id = :subject_id
                """
            ),
            {"subject_id": subject_id},
        ).scalar()

        assert check == new_title

        connection.execute(
            text(
                """
                DELETE FROM subject
                WHERE subject_id = :subject_id
                """
            ),
            {"subject_id": subject_id},
        )


def test_delete_subject():
    subject_id = int(uuid4().int % 1000000000)
    subject_title = f"Test subject {uuid4()}"

    with db.begin() as connection:
        connection.execute(
            text(
                """
                INSERT INTO subject (subject_id, subject_title)
                VALUES (:subject_id, :subject_title)
                """
            ),
            {
                "subject_id": subject_id,
                "subject_title": subject_title,
            },
        )

        connection.execute(
            text(
                """
                DELETE FROM subject
                WHERE subject_id = :subject_id
                """
            ),
            {"subject_id": subject_id},
        )

        check = connection.execute(
            text(
                """
                SELECT subject_id
                FROM subject
                WHERE subject_id = :subject_id
                """
            ),
            {"subject_id": subject_id},
        ).scalar()

        assert check is None
