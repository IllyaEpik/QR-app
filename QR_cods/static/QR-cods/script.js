let name1 = document.querySelectorAll('input')[1]
let color1 = document.querySelectorAll('.color')
for (let c of color1){

    c.style.width = name1.clientWidth
    c.style.height = name1.clientHeight
}
console.log(name1,color1,name1.style.height,name1.clientHeight)