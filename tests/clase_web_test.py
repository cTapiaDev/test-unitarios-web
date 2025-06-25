import pytest, requests, responses

API_URL_BASE = "http://localhost:5000"

def test_endpoint_usuarios():

    try:
        r = requests.get(f"{API_URL_BASE}/usuarios")
        assert r.status_code == 200
        assert r.headers['Content-Type'] == 'application/json'
        assert isinstance(r.json(), list)
        assert len(r.json()) > 0
        assert "nombre" in r.json()[0]
        assert isinstance(r.json()[0]["nombre"], str)

    except requests.exceptions.ConnectionError as e:   
        pytest.fail(f"ERROR: {API_URL_BASE}: {e}")


@responses.activate
def test_404():
    responses.add(responses.GET, "https://api.com/usuario/0", status=404)
    r = requests.get("https://api.com/usuario/0")
    assert r.status_code == 404


@responses.activate
def test_mock_user():
    responses.add(
        responses.GET,
        f"{API_URL_BASE}/usuarios/1",
        json = {"id": 1, "nombre": "Ana"},
        status = 200
    )
    r = requests.get(f"{API_URL_BASE}/usuarios/1")
    assert r.json() == {"id": 1, "nombre": "Ana"}