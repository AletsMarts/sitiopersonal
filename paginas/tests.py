from django.test import SimpleTestCase

# Create your tests here.
class PruebasPaginaInicio(SimpleTestCase):
    def test_url_existe(self):
        respuesta = self.client.get('/')
        self.assertEqual(respuesta.status_code, 200)

class PruebasPaginasAbout(SimpleTestCase):
    def test_template(self):
        respuesta = self.client.get('/nosotros/')
        self.assertEqual(respuesta.status_code, 200)
        #self.assertTemplateUsed(respuesta, 'paginas/index.html')
