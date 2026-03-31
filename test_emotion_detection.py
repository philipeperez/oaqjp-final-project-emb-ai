from EmotionDetection import emotion_detector
import unittest


class TestEmotions(unittest.TestCase):
    def test_joy_emotion(self):
        res = emotion_detector('I am glad this happened')
        self.assertEqual(res['dominant_emotion'], 'joy')
    
    def test_anger_emotion(self):
        res = emotion_detector('I am really mad about this')
        self.assertEqual(res['dominant_emotion'], 'anger')

    def test_disgust_emotion(self):
        res = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(res['dominant_emotion'], 'disgust')
    
    def test_sadness_emotion(self):
        res = emotion_detector('I am so sad about this')
        self.assertEqual(res['dominant_emotion'], 'sadness')
    
    def test_fear_emotion(self):
        res = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(res['dominant_emotion'], 'fear')


if __name__ == '__main__':
    unittest.main()