let fs = require("fs");
let jimp = require("jimp");
let files = fs.readdirSync("./input");
let images = [];
for (file of files) {
    images.push(file);

}
let batch = images.map(e => `input/${e}`);

let jimps = [];
for (e of batch) {
    jimps.push(jimp.read(e))
}

Promise.all(jimps).then(() => {
    return Promise.all(jimps)
}).then(data => {
    for (info = 0; info < data.length; info++) {

        let newimg = data[info];
        newimg.resize(400, 400);
        newimg.write(`output/${info}.jpeg`);

    }
    newFunction();
})

function newFunction() {
    console.log("i have finished master");
}