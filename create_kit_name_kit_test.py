# Здесь хранятся тесты по чек-листу

# Импорт пакетов
import data
import sender_stand_request


# Код для нового пользователя
def create_new_user():
    auth_token = sender_stand_request.get_new_user_token()
    if auth_token.status_code == 201 and auth_token.json()["authToken"] != "":
        return auth_token.json()["authToken"]


# Создаем нового пользователя
auth = create_new_user()


# Код для получения тела запроса
def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body


# Позитивные проверки
def positive_assert_name(kit_name):
    kit_body = get_kit_body(kit_name)
    response = sender_stand_request.post_new_client_kit(kit_body, auth)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]


# Негативные проверки
def negative_assert_code(kit_name):
    kit_body = get_kit_body(kit_name)
    response = sender_stand_request.post_new_client_kit(kit_body, auth)
    assert response.status_code == 400
    assert response.json()["code"] == 400


def negative_assert_no_kit_name(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, auth)
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "Не все необходимые параметры были переданы"


# Тесты по чеклисту
# 1 Допустимое количество символов (1)
def test_one_symbol_1():
    positive_assert_name("a")


# 2 Допустимое количество символов (511)
def test_allow_number_symbol_2():
    positive_assert_name(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


# 3 Количество символов меньше допустимого (0)
def test_zero_symbols_3():
    negative_assert_code("")


# 4 Количество символов больше допустимого (512)
def test_many_symbols_4():
    negative_assert_code(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


# 5 Разрешены английские буквы
def test_engish_symbols_5():
    positive_assert_name("QWErty")


# 6 Разрешены русские буквы
def test_russian_symbols_6():
    positive_assert_name("Мария")


# 7 Разрешены спецсимволы
def test_special_symbols_7():
    positive_assert_name("\"№%@\",")


# 8 Разрешены пробелы
def test_space_and_symbols_8():
    positive_assert_name(" Человек и КО ")


# 9 Разрешены цифры
def test_numbers_in_string_9():
    positive_assert_name("123")


# 10 Параметр не передан в запросе
def test_no_parameter_10():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_no_kit_name(kit_body)


# 11 Передан другой тип параметра (число)
def test_other_type_numbers_11():
    negative_assert_code(123)
