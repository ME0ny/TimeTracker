from starlette.config import Config

config = Config(".env")

DATABASE_URL = config("IS_DATABASE_URL", cast=str, default="")
ACCESS_TOKEN_EXPIRE_MINUTES = 60
ALGORITHM = "HS256"
SECRET_KEY = config("IS_SECRET_KEY", cast=str, default="")
EMOTICON_SERVER = config("ES_URL", cast=str, default="")
# человек:
# id          1
# логин       meony
#hashId       1q2w323d3f
# пароль      123
# имя         Артём
# фамилия     Ипатов
# статус      ученик

# время:
# id
# ученик_id   1
# дата        17.11.2021
# время       86400

# фотографии:
# id
# ученик_id   1
# дата        17.11.2021
# название    86400