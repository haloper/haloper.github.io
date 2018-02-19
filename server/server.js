const express = require('express');
const fs = require('fs');
const app = express();
const exec = require('child_process').exec

const PYTHON_PATH = "/Users/nhnent/Documents/github/haloper.github.io/python/"
const PREDICTER = "python3 ./predicter.py"

app.get('/', (req, res) => {
  let data = req.query.data
  let today = new Date()
  let year = today.getFullYear()
  let month = (today.getMonth() +1) < 10 ? '0' + (today.getMonth() +1) : (today.getMonth() +1)
  let day = today.getDate() < 10 ? '0' + today.getDate() : today.getDate()
  let fileName = "" + year + month + day

  fs.appendFile('/Users/nhnent/Documents/github/haloper.github.io/server/data/' + fileName, data + '\n', function (err) {
    if(err) {
        console.log(err)
        return
    }
    console.log(data)

    exec("cd " + PYTHON_PATH, function (error, stdout, stderr) {
        exec(PREDICTER, function (error, stdout, stderr) {
            if(error) {
                console.log(stderr)
                return
            }
            let msg = stdout
            res.send("jcallback('" + msg + "')")
        })
    })
  });

 });

app.listen(9080, () => {
  console.log('http://localhost:9080');
});
