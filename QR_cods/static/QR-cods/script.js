let name1 = document.querySelectorAll('input')[1]
let color1 = document.querySelector('.color')
color1.style.width = name1.clientWidth
color1.style.height = name1.clientHeight
console.log(name1,color1,name1.style.height,name1.clientHeight)