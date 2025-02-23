let name1 = document.querySelectorAll('input')[1]
let inputs = document.querySelectorAll('input')
let color1 = document.querySelectorAll('.color')
let two = document.querySelector('#two')
let back = document.querySelector('.back')
let select = document.querySelector('select')
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

document.querySelector("form").addEventListener("submit", (event) => {
    localStorage.setItem('url',inputs[1].value)
    localStorage.setItem('name',inputs[2].value)
    localStorage.setItem('color',inputs[3].value)
    localStorage.setItem('color-gradient',inputs[4].value)
    localStorage.setItem('background-color',inputs[5].value)
    localStorage.setItem('select',select.value)
})
console.log(localStorage.getItem('url'))
inputs[1].value = localStorage.getItem('url')
inputs[2].value = localStorage.getItem('name')
inputs[3].value = localStorage.getItem('color')
inputs[4].value = localStorage.getItem('color-gradient')
inputs[5].value = localStorage.getItem('background-color')
if (localStorage.getItem('select')!= undefined){
    select.value = localStorage.getItem('select')
    if (localStorage.getItem('select') == 'gradient'){
        two.classList.remove('hidden')
    }
}