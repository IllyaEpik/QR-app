let name1 = document.querySelectorAll('input')[1]
let inputs = document.querySelectorAll('input')
let color1 = document.querySelectorAll('.color')
let two = document.querySelector('#two')
let back = document.querySelector('.back')
let select = document.querySelector('.custom-select')
let type = document.querySelector('.type-of-qr')
let block = document.querySelector('.block')

// let main = document.querySelector('main')
// main.classList.add('opasity')
block.style.width = select.clientWidth*1.1
for (let c of color1){
    c.style.width = name1.clientWidth/3
    c.style.height = name1.clientHeight
}
back.style.width =name1.clientWidth
select.addEventListener('change', function (event) {
    if (event.target.value == 'color'){
        two.classList.add('hidden')
    }else{
        two.classList.remove('hidden')
    }
})
if (type.value == localStorage.getItem('type') == 'desktop'){
    block.classList.add('hidden')
}
console.log(block.id)
if (block.id == 'free'){
type.addEventListener('change', function (event) {
    
        if (event.target.value == 'desktop'){
            block.classList.add('hidden')
        }else{
            block.classList.remove('hidden')
        }
    })
}else{
    block.classList.add('hidden')
}
// type-of-qr
document.querySelector("form").addEventListener("submit", (event) => {
    localStorage.setItem('url',inputs[1].value)
    localStorage.setItem('name',inputs[2].value)
    localStorage.setItem('color',inputs[3].value)
    localStorage.setItem('color-gradient',inputs[4].value)
    localStorage.setItem('background-color',inputs[5].value)
    localStorage.setItem('select',select.value)
    localStorage.setItem('type',type.value)
})
console.log(localStorage.getItem('url'))
if (localStorage.getItem('background-color')){
    inputs[5].value = localStorage.getItem('background-color')
}else{
    inputs[5].value = '#FFFFFF'
}
inputs[1].value = localStorage.getItem('url')
console.log(localStorage.getItem('type'))
if (localStorage.getItem('type') != null){
    console.log(localStorage.getItem('type'))
    type.value = localStorage.getItem('type')
}
inputs[3].value = localStorage.getItem('color')
inputs[2].value = localStorage.getItem('name')
inputs[4].value = localStorage.getItem('color-gradient')
if (localStorage.getItem('select')){
    select.value = localStorage.getItem('select')
    if (localStorage.getItem('select') == 'gradient'){
        two.classList.remove('hidden')
    }
}