
// Back Button
function ShowAll() {
var x = document.getElementById("FulBox");
var y = document.getElementById("RedBox");
var z = document.getElementById("IfyBox");   
x.style.display = "block";
y.style.display = "block";
z.style.display = "block";
clearCanvases();
}

 var imgBG = null;
 var imgFG = null;

 function uploadFG()
{
  var fileInput = document.getElementById("MaskFile");
  var canvas = document.getElementById("canvas1");
  imgFG = new SimpleImage(fileInput);
  imgFG.drawTo(canvas);
}

//Printify Mask
function LayerIfy() {
clearCanvases();
  var red = document.getElementById("RedBox");
  var ful = document.getElementById("FulBox");
  red.style.display = "none";
  ful.style.display = "none";

  var fileInput = document.getElementById("IfybgFile");
  var canvas = document.getElementById("canvas1");
  imgBG = new SimpleImage(fileInput);
    imgBG.drawTo(canvas);

}

// Printful Mask
function LayerFul() {
clearCanvases();
  var ify = document.getElementById("IfyBox");
  var red = document.getElementById("RedBox");
  ify.style.display = "none";
  red.style.display = "none";

  var fileInput = document.getElementById("FulbgFile");
  var canvas = document.getElementById("canvas1");
  imgBG = new SimpleImage(fileInput);
    imgBG.drawTo(canvas);
}

// Redbubble mask
function LayerRed() {
clearCanvases();
  var ify = document.getElementById("IfyBox");
  var ful = document.getElementById("FulBox");
  ify.style.display = "none";
  ful.style.display = "none";

  var fileInput = document.getElementById("RedbgFile");
  var canvas = document.getElementById("canvas1");
  imgBG = new SimpleImage(fileInput);
  imgBG.drawTo(canvas);
}

function Combine()
{
    var canvas = document.getElementById("canvas1");
    var output  = new SimpleImage(imgFG.getWidth(), imgFG.getHeight());
    for (var pixel of imgFG.values()) {
    //Look at currentPixel and if it is green, 
    if (pixel.getGreen() > pixel.getRed() + pixel.getBlue()) {
        //Look at same position in bgImage
        var x = pixel.getX();
        var y = pixel.getY();
        var bgPixel = imgBG.getPixel(x, y);
        //and set output's corresponding pixel to bgImage's pixel
        output.setPixel(x, y, bgPixel);
    }
    //Otherwise: set output's corresponding pixel to currentPixel
    else {
        output.setPixel(pixel.getX(), pixel.getY(), pixel);
    }    
}
  clearCanvases();
  var canvas = document.getElementById("canvas1");
  output.drawTo(canvas);
}

function clearCanvases()
{
  imgBG = null;
  var canvas1 = document.getElementById("canvas1");
  var context = canvas1.getContext("2d");
  context.clearRect(0, 0, canvas1.width, canvas1.height);

 }


