class TestMain(object):

    def test_index(self, client):
        # Ensure Flask is setup.
        response = client.get('/', follow_redirects=True)
        assert response.status_code == 200
        assert b'{\n  "status": "OK"\n}' == response.data
