let fs = require("fs");
let jimp = require("jimp");
let files = fs.readdirSync("./input");
let images = [];
for (file of files) {
  images.push(file);
}
let frame = jimp.read("./compose/frame.jpg")
let batch = images.map((e) => `input/${e}`);


let jimps = [];
for (e of batch) {
    jimps.push(jimp.read(e));
}
function enframe(img, name) {
    let testImg = [frame, img];


Promise.all(testImg).then(e => {
    return Promise.all(testImg);
    
}).then(e => {
    e[0].resize(1510, 1510);
    e[1].resize(1470,1470)

    e[0].composite(e[1], 20, 20);
    e[0].write(`output/${name}.jpg`, console.log("done master"))
    
})
    
}
for (let index = 0; index < jimps.length; index++) {
    const e= jimps[index];
    enframe(e,index)
    
}


// Promise.all(jimps)
//   .then(() => {
//     return Promise.all(jimps);
//   })
//   .then((data) => {
//     for (info = 0; info < data.length; info++) {
//       let newimg = data[info];
//       newimg.resize(400, 400);
//       newimg.write(`output/${info}.jpeg`);
//     }
//     newFunction();
//   })
//   .catch((e) => console.log(e));

// function newFunction() {
//     console.log("i have finished master")
// }