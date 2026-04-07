from db import get_connection
# load products list

class ProductList_Repository:
    """
    products 테이블에 대한 DB 작업을 담당하는 클래스
    1) 이메일 중복 확인
    2) 사용자 저장
    """

    # 1) 이메일 중복 확인
    @staticmethod
    def get_user_by_email(email: str):
        conn = get_connection()  # DB 연결 열기

        try:
            with conn.cursor() as cur:
                # %s 자리에 email 값이 안전하게 바인딩됩니다.
                cur.execute(
                    """
                    SELECT customer_id, email, nickname, create_date
                        FROM "Companion".customer_detail
                        WHERE email = %s
                    """,
                    (email, )
                )

                # 한 건만 조회
                user = cur.fetchone()
                return user

        finally:
            # DB 연결 닫기
            conn.close()

    # 2) 사용자 저장 - 저장된 사용자 정보 반환
    @staticmethod
    def create_customer():
        conn = get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO "Companion".customer
                    DEFAULT VALUES
                    RETURNING customer_id
                    """
                )
                row = cur.fetchone()
                conn.commit()
                return row["customer_id"]
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()

    @staticmethod
    def create_customer_detail(customer_id, email, nickname, password_hash):
        conn = get_connection()  # DB 연결 열기

        try:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO "Companion".customer_detail (customer_id, email, nickname, password)
                        VALUES (%s, %s, %s, %s)
                        RETURNING customer_id, email, nickname, create_date
                    """,
                    (customer_id, email, nickname, password_hash)
                )

                # INSERT 후 RETURNING으로 방금 저장된 행 받기
                user = cur.fetchone()

                # INSERT/UPDATE/DELETE는 commit 해야 진짜 반영됨
                conn.commit()

                return user

        except Exception:
            # 오류가 나면 DB 반영 취소
            conn.rollback()
            raise

        finally:
            # 연결 닫기
            conn.close()