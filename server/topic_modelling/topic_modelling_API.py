import fastText
from flask import Flask, request, Response, send_file
import json
import requests
import ast
import jsonpickle
from flask_cors import CORS
app = Flask(__name__)
#CORS(app)
baseURL = "http://localhost:80"

topic_modelling_API = "/infore/api/topic_modelling"


topic = ["", "Bán hàng", "Bất động sản", "Nghệ thuật", "Chăm sóc sắc đẹp", "Chính trị", "Triết lý sống", "Địa điểm", "Đồ dùng gia đình", "Du lịch", "Gia đình", "Truyền hình", "Giáo dục", "Hoạt động xã hội", "Đám cưới", "Kinh doanh", "Lễ hội", "Pháp luật", "Giao thông vận tải", "Quảng cáo trực tuyến", "Thiết bị điện tử", "Thời tiết khí hậu", "Thời trang", "Thực phẩm + nấu ăn", "Tôn giáo tín ngưỡng", "Tuyển dụng", "Y tế Sức khỏe", "Công nghệ", "Dịch vụ giao hàng", "Trang sức", "Nấu ăn", "Ngoại ngữ", "Mỹ phẩm", "Nhiếp ảnh", "Nghệ sĩ", "Cộng đồng", "Tổ chức xã hội", "Đồ uống", "Đồ ăn tráng miệng", "Địa điểm giải trí", "Động vật", "Phim", "Tâm sự", "Tổ chức sự kiện"]


@app.route(topic_modelling_API, methods=['GET','POST'])
def classify_topic():
    loaded_body = parse_json_from_request(request)
    context = loaded_body['context']
    print("________")
    print(context)
    
    label, prob = fastText.load_model("models/model_fb_190308.bin").predict(context, 3)
    ind = [int(label[0][9:]), int(label[1][9:]), int(label[2][9:])]
    response = {
        'topics':
        [
            {
                'result':'',
                'score':''
            }, 
            {
                'result':'',
                'score':''
            }, 
            {
                'result':'',
                 'score':''
             }
        ], 
        'status': '200'
    }
    
    response['topics'][0]['result'] = topic[ind[0]]
    response['topics'][0]['score'] = str(prob[0])
    response['topics'][1]['result'] = topic[ind[1]]
    response['topics'][1]['score'] = str(prob[1])
    response['topics'][2]['result'] = topic[ind[2]]
    response['topics'][2]['score'] = str(prob[2])
    
    response_pickled = jsonpickle.encode(response)
    
    print(response_pickled)
    print(Response(response=response_pickled, status=200, mimetype="application/json"))
    print("________")
    return Response(response=response_pickled, status=200, mimetype="application/json")
        
def parse_json_from_request(request):
    body_dict = request.json
    body_str = json.dumps(body_dict)
    loaded_body = ast.literal_eval(body_str)
    return loaded_body

if __name__ == "__main__":
    # start flask app
    app.run(host='0.0.0.0', port = 5002, debug = True)