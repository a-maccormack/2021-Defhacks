/**
 * (c) Facebook, Inc. and its affiliates. Confidential and proprietary.
 */

//==============================================================================
// Welcome to scripting in Spark AR Studio! Helpful links:
//
// Scripting Basics - https://fb.me/spark-scripting-basics
// Reactive Programming - https://fb.me/spark-reactive-programming
// Scripting Object Reference - https://fb.me/spark-scripting-reference
// Changelogs - https://fb.me/spark-changelog
//
// For projects created with v87 onwards, JavaScript is always executed in strict mode.
//==============================================================================

// How to load in modules
const Materials = require("Materials");
const Textures = require('Textures');
const TouchGestures = require('TouchGestures');
const Diagnostics = require('Diagnostics');

// Enable async/await in JS [part 1]
(async function() {
    // Locate the material and texture in the Assets
    const [MaskMaterial, Design1, Design2, Design3] = await Promise.all([
      Materials.findFirst('MaskDesign'),
      Textures.findFirst('D1'),
      Textures.findFirst('D2'),
      Textures.findFirst('D3')
    ]);

    Diagnostics.log("Screen ready")


    TouchGestures.onTap().subscribe(toogleMat);

    var CurrentD = 1
    
  function toogleMat() {
 
        Diagnostics.log("Screen Touched")
    
    
        if(CurrentD == 1) {
        MaskMaterial.diffuse = Design2;
        CurrentD = 2
        }
    
    
        else if (CurrentD == 2) {
        MaskMaterial.diffuse = Design3;
        CurrentD = 3
        }
    
    
        else {
        MaskMaterial.diffuse = Design1;
        CurrentD = 1
    }
    
}
    

})();
