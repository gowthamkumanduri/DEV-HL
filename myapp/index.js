var express= require('express');
var app= express();
var path = require('path');
var bodyParser = require('body-parser')
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
var watson = require('watson-developer-cloud');
var conversation = new watson.ConversationV1({
    username:'644992e6-c535-45b3-aa78-c1b0b87845a5',
    password:'8tKI4IZjclLh',
    version_date: '2018-02-16'
    
});

/*conversation.listWorkspaces(function(err, response) {
    if (err) {
      console.error(err);
    } else {
      console.log(JSON.stringify(response, null, 2));
    }
});

var params = {
    workspace_id: '0737c07f-7830-4ff4-a9a9-979d6be3c0a2'
  };
  
conversation.getWorkspace(params, function(err, response) {
    if (err) {
      console.error(err);
    } else {
      console.log(JSON.stringify(response, null, 2));
    }
});*/

app.get('/message',function(req,res){
  res.sendFile(path.join('/home/gowtham/Desktop/myapp/view'+'/message.html'));
});

app.post('/message',function(req,res){
  console.log('hi')
  message = JSON.stringify(req.body)
  console.log(message);
  conversation.message({
    workspace_id: '0737c07f-7830-4ff4-a9a9-979d6be3c0a2',
    input: {'text': message}
  },  function(err, response) {
    if (err)
      console.log('error:', err);
    else
      recieveddata = response.output.text;
      console.log(typeof(recieveddata));
      res.json(recieveddata);
  });


});





app.listen(3000);
console.log("Running at Port 3000");