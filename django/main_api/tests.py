from django.test import TestCase
from .views import BoardPost
from django.test.utils import override_settings
import requests

class NotifyViewTests(TestCase):
    def gen_test_one(self):
        """
        General Django Test v1
        """
        my_blance = [1,2,3,4,5]
        self.assertIs(len(my_blance) == 6, True)

    @override_settings(DEBUG=True)
    def gen_test_two(self):
        """
        General Django Test v2
        """
        myobj = {"type": "resistor", "description": "abc"}
        httpresponse = BoardPost().post(myobj)
        self.assertIs(httpresponse == 1, True)

    def test_incomplete_resistor(self):
        """
        Test Incomplete Type = Resistor (Bad Request)
        """
        url = 'http://localhost:8000/api/boardpost'
        myobj = {"type": "resistor", "description": "abc"}
        x = requests.post(url, data = myobj)
        self.assertIs(x.status_code == 400, True)

    def test_bad_value_transistor(self):
        """
        Test Bad Value Transistor (Bad Request)
        """
        url = 'http://localhost:8000/api/boardpost'
        myobj = {"type": "transistor", "current_gain": 'hey', "collector_emitter_voltage": 200.0, "emitter_base_voltage": 0.05, "collector_current": 0.0}
        x = requests.post(url, data = myobj)
        self.assertIs(x.status_code == 400, True)

    def test_pass_value_transistor(self):
        """
        Test Bad Value Transistor (Bad Request)
        """
        url = 'http://localhost:8000/api/boardpost'
        myobj = {"type": "transistor", "current_gain": 0.02, "collector_emitter_voltage": 200.0, "emitter_base_voltage": 0.05, "collector_current": 0.0}
        x = requests.post(url, data = myobj)
        self.assertIs(x.status_code == 200, True)
