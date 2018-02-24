const express = require('express');
const fs = require('fs');
const app = express();
const util = require('util');
const exec = util.promisify(require('child_process').exec);

const PYTHON_PATH = "/Users/nhnent/Documents/github/haloper.github.io/python/"

async function request(req, res) {
    let data = req.query.data
    let today = new Date()
    let year = today.getFullYear()
    let month = (today.getMonth() + 1) < 10 ? '0' + (today.getMonth() + 1) : (today.getMonth() + 1)
    let day = today.getDate() < 10 ? '0' + today.getDate() : today.getDate()
    let fileName = "" + year + month + day

    // const {err} = await fs.appendFile('/Users/nhnent/Documents/github/haloper.github.io/server/data/' + fileName, data + '\n')
    // if(err) {
    //     console.log(err)
    //     return
    // }
    console.log(data)
    const { stdout, stderr } = await exec(PYTHON_PATH + '/predictor.sh');

    res.send("jcallback('" + stdout + "')")
}


app.get('/', (req, res) => {
  request(req, res);
});

app.listen(9080, () => {
  console.log('http://localhost:9080');
});
