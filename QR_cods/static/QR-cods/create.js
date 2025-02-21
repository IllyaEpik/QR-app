let name1 = document.querySelectorAll('input')[1]
let color1 = document.querySelectorAll('.color')
let two = document.querySelector('#two')
for (let c of color1){
    c.style.width = name1.clientWidth
    c.style.height = name1.clientHeight
}

document.querySelector("select").addEventListener('change', function (event) {
    if (event.target.value == 'color'){
        two.classList.add('hidden')
    }else{
        two.classList.remove('hidden')
    }
})
console.log(two,'okoko')