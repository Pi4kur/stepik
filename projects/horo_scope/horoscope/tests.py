from django.test import TestCase
from horoscope.views import ZODIACS_DICT as z_dict
# Create your tests here.

class TestHoroscope(TestCase):
    def test_index(self):
        response = self.client.get('/horoscope/')
        self.assertEqual(response.status_code, 200)


    def test_libra(self):
        response = self.client.get('/horoscope/libra')
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября)', response.content.decode()
        )


    def test_libra_redirect(self):
        response = self.client.get('/horoscope/7')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/horoscope/libra')


    def test_all_zodiacs(self):
        for zod, info in z_dict.items():
            # print(f'Testing for zodiac {zod}...')
            response = self.client.get(f'/horoscope/{zod}')
            self.assertEqual(response.status_code, 200)
            self.assertIn(info, response.content.decode())


    def test_all_zodiacs_by_number(self):
        for i in range(1, 13):
            # print(f'Testing number {i}')
            response = self.client.get(f'/horoscope/{i}')
            self.assertEqual(response.status_code, 302)
            lst = list(z_dict)
            self.assertEqual(response.url, f'/horoscope/{lst[i-1]}')