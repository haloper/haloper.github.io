const util = require('util');
const exec = util.promisify(require('child_process').exec);

const PYTHON_PATH = "/Users/hoon/Documents/github/haloper.github.io/python"

async function lsExample() {
    const { stdout, stderr } = await exec(PYTHON_PATH + '/predictor.sh');
    console.log('stdout:', stdout);
}
lsExample();

// exec("cd " + PYTHON_PATH, function (error, stdout, stderr) {
//     exec(PREDICTER, function (error, stdout, stderr) {
//         if(error) {
//             console.log(stderr)
//             return
//         }
//         let msg = stdout
//     })
// })