let hex = document.getElementById('hex');
let button = document.getElementById('button');
let wynik = document.getElementById('wynik');
let error = document.getElementById('error');

function isIn(whatIn, inWhat) {
  for(let i = 0; i < inWhat.length; i++) {
    if(whatIn == inWhat[i]) return true;
  }
  return false;
}

function containsIllegalChars(testChars, legalChars) {
  for(let i = 0; i < testChars.length; i++) {
    if(!isIn(testChars[i], legalChars)) return true;
  }
  return false;
}

hex.onkeyup = () => {
  textArea = hex.value.toUpperCase();
  console.log(textArea);
  let tabLegal = ['A','B','C','D','E','F','1','2','3','4','5','6','7','8','9','0'];


  if(containsIllegalChars(textArea, tabLegal)) {
    error.innerHTML = "Invalid Character"
  }
  else error.innerHTML = ""
  if(textArea.length == 6 && !containsIllegalChars(textArea, tabLegal)) button.disabled = false
  else button.disabled = true

   // let zle = false;
   // for(let j=0; j<znak.length; j++) {
   //   for(let i=0; i<tab.length; i++) {
   //       // console.log("znak"+znak[j]);
   //       // console.log("tab"+tab[i]);
   //       console.log(znak)
   //       if(znak[j]==tab[i]) {
   //          zle = true;
   //       }
   //    }
   // }
   // if(!zle) error.innerHTML = "test";
   // else error.innerHTML = "";
}

// #FC 23 CD
function toDec(x) {
   let a = x.charAt(0).toUpperCase();
   let b = x.charAt(1).toUpperCase();
   let tab = ['A','B','C','D','E','F']
   //          0   1   2   3   4   5
   // console.log(a);
   // console.log(b);

   for(let i=0; i<6; i++) {
      if(tab[i]==a) a = i+10;
      if(tab[i]==b) b = i+10;
   }
   let wynik = parseInt(a*16) + parseInt(b);
   return wynik;
}

button.onclick = () => {
   let value = hex.value;
   let r =  toDec(value.substr(0,2));
   let g =  toDec(value.substr(2,2));
   let b =  toDec(value.substr(4,2));
   let RGB = "rgb("+r+','+g+','+b+')';
   wynik.innerHTML = RGB;

   document.body.style.background = RGB;
}
