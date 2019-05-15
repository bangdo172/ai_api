import requests
import json
addr = 'http://localhost:5000'
test_get = addr + '/v1/api/test_get'
test_post = addr + '/v1/api/summarize'
question_answering = "http://04d75191.ngrok.io/infore/api/question_answering"
test = "http://04d75191.ngrok.io/infore/test"

#request test API
get_response = requests.get(test)
res = get_response.json()
test_ = res['test']
hello_ = res['hello']
print(test_)
print(hello_)

#request question answering API
payload2 = {
"context":"Computer science is interesting. i love this",
"question": "What do i love?"
}
payload2 = json.dumps(payload2)
loaded_payload2 = json.loads(payload2)
post_response = requests.post(question_answering, '', json=loaded_payload2)
print(post_response)
res = post_response.json()
print('Response of POST method: ' + str(res) )
