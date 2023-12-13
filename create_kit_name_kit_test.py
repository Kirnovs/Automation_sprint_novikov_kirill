import pytest
import sender_stand_request


def get_new_user_token():
    sender_stand_request.post_new_user()
    if sender_stand_request.post_new_user().ok:
        return sender_stand_request.post_new_user().json()
    else:
        return "no auth"


@pytest.mark.parametrize("kit_body", [
    pytest.param("a", id="minimum length (1)"),
    pytest.param("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
    dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC", id="maximum length (511)"),
    pytest.param("QWErty", id="english"),
    pytest.param("Мария", id="russian"),
    pytest.param("№%@"",", id="special"),
    pytest.param(" Человек и КО ", id="spaces"),
    pytest.param("123", id="numbers")
])
def test_positive_assert(kit_body):
    auth_token = get_new_user_token()
    res = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert res.status_code == 201
    assert res.json()["name"] == kit_body


@pytest.mark.parametrize("kit_body", [
    pytest.param("", id="no symbol"),
    pytest.param("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
    dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD", id="more than 511 letters"),
    pytest.param(0, id="parameter was not passed"),
    pytest.param(123, id="parameter number")
])
def test_negative_assert_code_400(kit_body):
    auth_token = get_new_user_token()
    res = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert res.status_code == 400
