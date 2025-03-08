try{
    let button = document.querySelector('.copy-button')
    let h1 = document.querySelector('.copy-h1')
    // copyInput
    button.addEventListener('click', () => {
        // inp.select()
        navigator.clipboard.writeText(h1.textContent)
        // document.execCommand()
        console.log(h1.textContent)
    })
    console.log()
}catch{

    let buttons = document.querySelectorAll("button")
    let form = document.querySelector('form')
    let bg = document.querySelector('.bg')
    let hide = document.querySelector("#hide")
    let count = document.querySelector('.count')
    let inputs = document.querySelectorAll('input')
    let subscription = document.querySelector('span')
    console.log(hide)
    for (let button of buttons){
        console.log(button.name)
        if (button.name === "subscription"){
            button.addEventListener('click',(event) => {
                console.log(count.value < 101,'qewqeweqwwqewqeqew')
                if (count.value < 101 || event.target.value != 'desktop'){

                    form.classList.remove('hidden')
                    bg.classList.remove('hidden')
                    hide.value = event.target.value
                    if (hide.value == 'desktop'){
                        
                        if (!count.value){
                            bg.classList.add('hidden')
                            form.classList.add('hidden')
                            hide.value
                        }else{
                            hide.value += `;${count.value}`
                        }
                        subscription.textContent = `Do you want to buy ${count.value} desktop QR-codes? It costs ${count.value*10}$`
                    }else{
                        subscription.textContent = `from ${subscription.id} to ${event.target.value}`
                    }
                    if (hide.value == 'free'){
                        document.createElement('input').required = false
                        inputs[2].required = false
                        inputs[2].hidden = true
                        inputs[3].required = false
                        inputs[3].hidden = true
                    }
                    
                }
                    console.log(event.target,event.target.value)
            })
        }
    }
    bg.addEventListener('click', () =>{

        bg.classList.add('hidden')
        form.classList.add('hidden')
    })
}