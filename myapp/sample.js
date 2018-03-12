var jsonString = "{\"workspace\":[\"workspace1\",\"workspace2\"]}"

var response = JSON.parse(jsonString);
console.log(typeof(response))
console.log(response)
var response2 = JSON.stringify(response)
console.log(typeof(response2))
console.log(response2)
