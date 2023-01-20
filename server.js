const express = require('express');

const app = express();
app.set('view engine', 'ejs');

const PORT = 8080;

app.get('/', function(req, res){
    res.render('index');
});

app.listen(port=PORT, function(){
    console.log(`Server is running on port ${PORT}`);
});