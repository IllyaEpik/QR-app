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
    console.log(hide)
    for (let button of buttons){
        console.log(button.name)
        if (button.name === "subscription"){
            button.addEventListener('click',(event) => {
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