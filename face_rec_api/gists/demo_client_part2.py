import requests
import json
    
def test_face_rec():
    url = 'http://127.0.0.1:5001/face_rec'
    # open file in binary mode
    files = {'file': open('sample_images/peter2.jpg', 'rb')} 
    params = {'facial_features': 'true', 'face_locations':'true'}
    resp = requests.post(url, files = files, params = params)
    print( 'face_rec response:\n', json.dumps(resp.json()) )
    
if __name__ == '__main__':
    test_face_rec()