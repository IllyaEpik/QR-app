
let baseElement = document.querySelector('#Rating')
for (let count of [1,2,3,4,5,6,7,8,9,10]){
    let element = document.createElement('span')
    element.textContent = '★'
    element.id = `star-${count}`
    element.className = 'star'
    element.style.fontSize = 30
    element.addEventListener("click", () => {
        
        for (let count of [1,2,3,4,5,6,7,8,9,10]){
            console.log(element.id.split('-')[1], count-1)
            if (element.id.split('-')[1] > count-1){
                console.log('ahahha')
                let element1 = document.querySelector(`#star-${count}`)
                element1.style.color = '#D0FF00'
            }else{
                let element1 = document.querySelector(`#star-${count}`)
                element1.style.color = 'black'
            }
            
        }
    })
    baseElement.append(element)
}
