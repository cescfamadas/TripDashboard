import unittest
from server import create_app


class TestRoutes(unittest.TestCase):
    def setUp(self):
        """
        Configura l'aplicació i el client de proves abans de cada test.
        """
        self.server = create_app()
        self.server.config.update({
            "TESTING": True,

            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"
        })
        self.client = self.server.test_client()

# producte routes
    def test_producte_route_with_parameter(self):
        """Test /producte route with producte parameter."""
        response = self.client.get(
            '/trip/producte/producte1')
        expected = [
            {
                "pes": 13599,
                "producte": "producte1"
            }
        ]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected)

    def test_producte_route_without_parameter(self):
        """Test /producte route without producte parameter."""
        response = self.client.get('/trip/producte')
        self.assertEqual(response.status_code, 200)

    def test_producte_route_with_wrong_parameter(self):
        """Test /producte route with wrong producte parameter."""
        response = self.client.get('/trip/producte/unknown')
        self.assertEqual(response.status_code, 200)


# client routes


    def test_client_route_with_parameter(self):
        """Test /client route with client parameter."""
        response = self.client.get('/trip/client/transport')
        self.assertEqual(response.status_code, 200)

    def test_client_route_without_parameter(self):
        """Test /client route without client parameter."""
        response = self.client.get('/trip/client')
        self.assertEqual(response.status_code, 200)

    def test_client_route_with_wrong_parameter(self):
        """Test /client route with wrong client parameter."""
        response = self.client.get('/trip/client/unknown')
        self.assertEqual(response.status_code, 200)


# data routes


    def test_data_route_with_parameter(self):
        """Test /data route with data parameter."""
        response = self.client.get('/trip/data/transport')
        self.assertEqual(response.status_code, 200)

    def test_data_route_without_parameter(self):
        """Test /data route without data parameter."""
        response = self.client.get('/trip/data')
        self.assertEqual(response.status_code, 200)

    def test_data_route_with_wrong_parameter(self):
        """Test /data route with wrong data parameter."""
        response = self.client.get('/trip/data/unknown')
        self.assertEqual(response.status_code, 200)

    # transportista routes
    def test_transportista_route_with_parameter(self):
        """Test /transportista route with transportista parameter."""
        response = self.client.get('/trip/transportista/jocar')
        self.assertEqual(response.status_code, 200)

    def test_transportista_route_without_parameter(self):
        """Test /transportista route without transportista parameter."""
        response = self.client.get('/trip/transportista')
        self.assertEqual(response.status_code, 200)

    def test_transportista_route_with_wrong_parameter(self):
        """Test /transportista route with wrong transportista parameter."""
        response = self.client.get('/trip/transportista/unknown')
        self.assertEqual(response.status_code, 200)

    # desti routes

    def test_desti_route_with_parameter(self):
        """Test /desti route with desti parameter."""
        response = self.client.get('/trip/desti/noé')
        self.assertEqual(response.status_code, 200)

    def test_desti_route_without_parameter(self):
        """Test /desti route without desti parameter."""
        response = self.client.get('/trip/desti')
        self.assertEqual(response.status_code, 200)

    def test_desti_route_with_wrong_parameter(self):
        """Test /desti route with wrong desti parameter."""
        response = self.client.get('/trip/desti/unknown')
        self.assertEqual(response.status_code, 200)

    def test_404(self):
        """Test 404 page."""
        response = self.client.get('/trip/unknown')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
