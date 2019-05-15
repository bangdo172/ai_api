$(document).ready(function() {
    $("#btn").click(function() {
        var document_input = $('#DocInput').val()
        var question_input = $('#QuesInput').val()
        check = confirm("Are you sure?")
        
        if (check) {
            // Define JSON variable
            var sentObj = {
                context: document_input,
                question: question_input
            };

            // Send to sever a Json object
            url_server = 'http://3c459b8e.ngrok.io/infore/api/question_answering'
            
            $.ajax({
                type: 'POST',
                url: url_server,
                data: JSON.stringify(sentObj),
                success: function (data) {
                  var names = data
                  console.log(data.answers[0].result)
                  $("#response pre").html(data.answers[0].result)
                },
                contentType: "application/json",
                dataType: 'json'
            });     
        }
    })
})