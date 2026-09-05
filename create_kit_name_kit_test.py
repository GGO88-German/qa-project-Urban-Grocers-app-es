import data
import sender_stand_request


# Crea un nuevo usuario y obtiene el authToken
def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    return response.json()["authToken"]


# Crea una copia del body del kit y modifica el campo "name"
def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body


# Validación para casos positivos
# Resultado esperado: Status Code 201
def positive_assert(kit_body):
    auth_token = get_new_user_token()

    kit_response = sender_stand_request.post_new_client_kit(
        kit_body,
        auth_token
    )

    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]


# Validación para casos negativos
# Resultado esperado: Status Code 400
def negative_assert(kit_body):
    auth_token = get_new_user_token()

    kit_response = sender_stand_request.post_new_client_kit(
        kit_body,
        auth_token
    )

    assert kit_response.status_code == 400


# TEST CASE 1
# El número permitido de caracteres (1)
# kit_body = {"name": "a"}
# Resultado esperado: 201
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert(get_kit_body("a"))


# TEST CASE 2
# El número permitido de caracteres (511)
# Resultado esperado: 201
def test_create_kit_511_letters_in_name_get_success_response():
    name = (
        "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
    )

    positive_assert(get_kit_body(name))


# TEST CASE 3
# El número de caracteres es menor que la cantidad permitida (0)
# kit_body = {"name": ""}
# Resultado esperado: 400
def test_create_kit_0_letters_in_name_get_error_response():
    negative_assert(get_kit_body(""))


# TEST CASE 4
# El número de caracteres es mayor que la cantidad permitida (512)
# Resultado esperado: 400
def test_create_kit_512_letters_in_name_get_error_response():
    name = "a" * 512

    negative_assert(get_kit_body(name))


# TEST CASE 5
# Se permiten caracteres especiales
# kit_body = {"name": "№%@,"}
# Resultado esperado: 201
def test_create_kit_special_characters_in_name_get_success_response():
    positive_assert(get_kit_body("№%@,"))


# TEST CASE 6
# Se permiten espacios
# kit_body = {"name": " A Aaa "}
# Resultado esperado: 201
def test_create_kit_spaces_in_name_get_success_response():
    positive_assert(get_kit_body(" A Aaa "))


# TEST CASE 7
# Se permiten números
# kit_body = {"name": "123"}
# Resultado esperado: 201
def test_create_kit_numbers_in_name_get_success_response():
    positive_assert(get_kit_body("123"))


# TEST CASE 8
# El parámetro "name" no se pasa en la solicitud
# kit_body = {}
# Resultado esperado: 400
def test_create_kit_no_name_get_error_response():
    negative_assert({})


# TEST CASE 9
# Se ha pasado un tipo de parámetro diferente (número)
# kit_body = {"name": 123}
# Resultado esperado: 400
def test_create_kit_number_type_in_name_get_error_response():
    negative_assert(get_kit_body(123))