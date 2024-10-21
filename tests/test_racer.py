import unittest
from unittest.mock import patch, MagicMock
from wikiracer.racer import WikiRacer

class TestWikiRacer(unittest.TestCase):
    def setUp(self):
        self.racer = WikiRacer()

    @patch('wikiracer.racer.WikiRacer.get_page_content')
    def test_find_path(self, mock_get_page_content):
        # Mocked page content and links
        # This is a simplified test to demonstrate the concept
        def side_effect(url):
            soup = MagicMock()
            soup.find.return_value = MagicMock()
            if 'Start_Page' in url:
                links = {'https://en.wikipedia.org/wiki/Intermediate_Page'}
            elif 'Intermediate_Page' in url:
                links = {'https://en.wikipedia.org/wiki/End_Page'}
            else:
                links = set()
            soup.find.return_value.find_all.return_value = [
                MagicMock(attrs={'href': '/wiki/' + link.split('/')[-1]}) for link in links
            ]
            return soup

        mock_get_page_content.side_effect = side_effect

        start_url = 'https://en.wikipedia.org/wiki/Start_Page'
        end_url = 'https://en.wikipedia.org/wiki/End_Page'

        path = self.racer.find_path(start_url, end_url)
        expected_path = [
            'https://en.wikipedia.org/wiki/Start_Page',
            'https://en.wikipedia.org/wiki/Intermediate_Page',
            'https://en.wikipedia.org/wiki/End_Page'
        ]
        self.assertEqual(path, expected_path)

if __name__ == '__main__':
    unittest.main()
