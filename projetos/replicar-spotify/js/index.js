const button = document.getElementById('btn')
const nav_2 = document.getElementById('nav-2')
const div_img_nav_2 = document.getElementById('div-img-nav-2')
const li_playlist = document.getElementById('li-playlist')
const div_playlist = document.getElementById('div-playlist')
const div = document.getElementById('div')
const seta_para_cima = document.createElement('span')
const li_economia = document.getElementById('li-economia')
const div_economia = document.getElementById('div-economia')
const div_2 = document.getElementById('div-2')
const li_aleatoria = document.getElementById('li-aleatoria')
const li_podcasts = document.getElementById('li-podcasts')
button.addEventListener('click',function(){
    nav_2.style.display = 'block'
    document.body.style.overflowY = 'hidden'
    const btn_2 = document.createElement('button')
    btn_2.innerText = 'X'
    btn_2.style.color = 'white'
    btn_2.style.fontSize = '30px'
    nav_2.appendChild(btn_2)
    div_img_nav_2.style.display = 'block'
    btn_2.addEventListener('click',function(){
        document.body.style.overflowY = 'auto' 
        nav_2.style.display = 'none'
        div_img_nav_2.style.display = 'none'
    })
})

let contador = 0
li_playlist.addEventListener("click",function(){
    let seta_list = document.getElementById('seta-list')
    if (contador < 2){
    div_playlist.style.display = 'block'
    seta_list.style.display = 'none'
    seta_para_cima.innerText = '⇑'
    seta_para_cima.style.display = 'inline'
    div.appendChild(seta_para_cima)
    }
    contador += 1
    if (contador == 2){
        div_playlist.style.display = 'none'
        seta_para_cima.style.display = 'none'
        seta_list.style.display = 'block'
        seta_list.style.position = 'absolute'
        seta_list.style.top = '40px'
        div.removeChild(seta_para_cima)
        contador = 0
    }
})
li_economia.addEventListener('click',function(){
    const seta_list = document.getElementById('seta-list')
    if (contador < 2 ){
        div_economia.style.display = 'block'
    }
    contador += 1 
    if (contador == 2){
       
        div_economia.style.display = 'none'
        contador = 0
    }
})
li_aleatoria.addEventListener("click",function(){
    const div_aleatoria = document.getElementById('div-aleatoria')
    
    if (contador < 2){
        div_aleatoria.style.display = 'block'
    }
    contador ++
    if (contador == 2){
        div_aleatoria.style.display = 'none'
        contador = 0
    }
})
li_podcasts.addEventListener('click',function(){
    const div_podcasts = document.getElementById('div-podcasts')
    if (contador < 2){
        div_podcasts.style.display = 'block'
    }
    contador ++
    if (contador == 2 ){
        div_podcasts.style.display = 'none'
        contador = 0 
    }
})