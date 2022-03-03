# DB revision이 꼬였을 경우
alembic stamp base( 리비전 초기화)
alembic stamp head  
alembic revision --autogenerate (새로 생성)
alembic upgrade head (DB에 적용)