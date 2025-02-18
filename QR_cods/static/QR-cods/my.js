let qrCards = document.querySelectorAll('.qr-card')
let inp = document.querySelector('input')
let fil = document.querySelector('.filter')


fil.addEventListener("click", (e) =>{
   for (let qrCard of qrCards ){
    console.log(qrCard.id.split(inp.value))
   if (qrCard.id.split(inp.value).length>1){
    qrCard.classList.remove("hidden")
    }else{
        qrCard.classList.add("hidden")
    }
} 
})





