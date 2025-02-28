let qrCards = document.querySelectorAll('.qr-card')
let inp = document.querySelector('input')
let fil = document.querySelector('.filter')
let details = document.querySelector('.details')
let modal = document.getElementById('modal')
let close1 = document.getElementById('close')
let bg = document.getElementById('modalBg')


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

close1.addEventListener("click", togglePopup)
details.addEventListener("click", togglePopup)
bg.addEventListener("click", togglePopup)


function togglePopup(){
    bg.classList.toggle("show")
    modal.classList.toggle("show")
}