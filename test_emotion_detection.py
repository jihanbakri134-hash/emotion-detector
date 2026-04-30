import unittest
from emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_emotion(self):
        result = emotion_detector("I am happy")
        
        self.assertIn("joy", result)
        self.assertIn("anger", result)
        self.assertIn("sadness", result)

if __name__ == "__main__":
    unittest.main()
