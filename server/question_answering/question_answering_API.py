from flask import Flask, request, Response, send_file
import DrQA.drqa.reader.predictor as predictor
import json
import requests
import jsonpickle
import ast
app = Flask(__name__)

baseURL = "http://localhost:80"

question_answering_API = "/infore/api/question_answering"
test = '/infore/test'

token = "spacy"
predictions = predictor.Predictor(model=None, tokenizer=token, normalize=True, embedding_file=None, num_workers=None)

@app.route(question_answering_API, methods=['GET','POST'])
def answer_question():
    #get question and hash_url
    loaded_body = parse_json_from_request(request)
    context = loaded_body['context']
    question = loaded_body['question']
    print(context)
    print(question)
    
    #predict and return
    #predict
    answer = predictions.predict(document=context, question=question, candidates=None, top_n=3)
    #return
    response = {
        'answers':
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
    response['answers'][0]['result'] = answer[0][0]
    response['answers'][0]['score'] = answer[0][1]
    response['answers'][1]['result'] = answer[1][0]
    response['answers'][1]['score'] = answer[1][1]
    response['answers'][2]['result'] = answer[2][0]
    response['answers'][2]['score'] = answer[2][1]
    
    response_pickled = jsonpickle.encode(response)
    print(response_pickled)
    print(Response(response=response_pickled, status=200, mimetype="application/json"))
    print("________")
    return Response(response=response_pickled, status=200, mimetype="application/json")

@app.route(test, methods = ['GET'])
def test():
    response = {'test': 'say Hi!', 'hello': 'Hello guy'}
    response_pickled = jsonpickle.encode(response)
    return Response(response=response_pickled, status=200, mimetype="application/json")

def parse_json_from_request(request):
    body_dict = request.json
    body_str = json.dumps(body_dict)
    loaded_body = ast.literal_eval(body_str)
    return loaded_body

if __name__ == "__main__":
    # start flask app
    app.run(host='0.0.0.0', port = 5001)
