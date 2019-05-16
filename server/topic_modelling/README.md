# Topic Modelling Documentation

_/infore/api/topic_modelling_ (POST, GET)

__Request:__ 
```js
Header = {
    "content-type": "application/json"
}

Body = {
    'context': ''   // context here
}
```
__Response:__

```js
{
    'topics':
        [
            {
                'result':'',    // result with highest capacity
                'score':''      // score of the result
            }, 
            {
                'result':'',    // second
                'score':''
            }, 
            {
                'result':'',    // third
                 'score':''
             }
        ]
}
```
