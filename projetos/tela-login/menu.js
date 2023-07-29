const menu_btn = document.querySelector('.btn')
let contador = 0
menu_btn.addEventListener('click',function(){
    const nav_bar = document.querySelector('.nav-2')
    if (contador < 2 ){
        nav_bar.style.display = 'flex'
    }
    contador ++
    if (contador == 2){
        nav_bar.style.display = 'none'
        contador = 0
    }
})