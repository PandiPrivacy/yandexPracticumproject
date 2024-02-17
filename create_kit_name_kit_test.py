import data
import sender_stand_request

auth = "d07afdd2-c8e6-4473-b92d-8a51bdfae65f"


def negative_assert_code(response):
    assert response.status_code == 400
    assert response.json()["code"] == 400


def positive_assert_name(response, kit_body):
    assert response.json()["name"] == kit_body["name"]


def test_one_symbol_1():
    kit_body = data.kit_body1
    response = sender_stand_request.post_new_client_kit(kit_body, auth)
    assert response.status_code == 201
    positive_assert_name(response, kit_body)


def test_allow_number_symbol_2():
    kit_body = data.kit_body2
    response = sender_stand_request.post_new_client_kit(kit_body, auth)
    assert response.status_code == 201
    positive_assert_name(response, kit_body)


def test_zero_symbols_3():
    kit_body = data.kit_body3
    response = sender_stand_request.post_new_client_kit(kit_body, auth)
    negative_assert_code(response)


def test_many_symbols_4():
    kit_body = data.kit_body4
    response = sender_stand_request.post_new_client_kit(kit_body, auth)
    negative_assert_code(response)


def test_engish_symbols_5():
    kit_body = data.kit_body5
    response = sender_stand_request.post_new_client_kit(kit_body, auth)
    assert response.status_code == 201
    positive_assert_name(response, kit_body)


def test_russian_symbols_6():
    kit_body = data.kit_body6
    response = sender_stand_request.post_new_client_kit(kit_body, auth)
    assert response.status_code == 201
    positive_assert_name(response, kit_body)


def test_special_symbols_7():
    kit_body = data.kit_body7
    response = sender_stand_request.post_new_client_kit(kit_body, auth)
    assert response.status_code == 201
    positive_assert_name(response, kit_body)


def test_space_and_symbols_8():
    kit_body = data.kit_body8
    response = sender_stand_request.post_new_client_kit(kit_body, auth)
    assert response.status_code == 201
    positive_assert_name(response, kit_body)


def test_numbers_in_string_9():
    kit_body = data.kit_body9
    response = sender_stand_request.post_new_client_kit(kit_body, auth)
    assert response.status_code == 201
    positive_assert_name(response, kit_body)


def test_no_parameter_10():
    kit_body = data.kit_body10
    response = sender_stand_request.post_new_client_kit(kit_body, auth)
    negative_assert_code(response)


def test_other_type_numbers_11():
    kit_body = data.kit_body11
    response = sender_stand_request.post_new_client_kit(kit_body, auth)
    negative_assert_code(response)


