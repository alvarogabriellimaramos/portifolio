const button_clique = document.getElementById('btn-clique')
let contador = 1
button_clique.addEventListener('click',function(){
    const cont = document.getElementById('cont')
    cont.innerText = `${contador++} cliques`
    if (contador == 21){
        contador = 0
    }
})
const like = document.getElementById('like')
const deslike = document.getElementById('deslike')
const resposta_like = document.querySelector('.resposta-like')
const span_like = document.querySelector('.span-like')
like.addEventListener('click',() => {
    like.classList.add('like')
    deslike.classList.remove('deslike')
    localStorage.verificar = 'true'
    deslike.addEventListener("click",function(){
        like.classList.remove('like')
        deslike.classList.add('deslike')
        localStorage.verificar = 'false'
        resposta_like.style.display = 'none'
        span_like.style.display = 'block'
    })
    resposta_like.style.display = 'block'
    span_like.style.display = 'none'
})
deslike.addEventListener('click',function(){
    deslike.classList.add("deslike")
    like.classList.remove('like')
    localStorage.verificar = 'false'
    span_like.style.display = 'block'
    like.addEventListener('click',function(){
        like.classList.add('like')
        localStorage.verificar = 'true'
        deslike.classList.remove('deslike')
        resposta_like.style.display = 'block'
        span_like.style.display = 'none'
    })
    resposta_like.style.display = 'none'
})
window.onload = () => {
    if (localStorage.getItem('verificar') == 'true'){
        like.classList.add('like')
        deslike.classList.remove('deslike')
        resposta_like.style.display = 'block'
        span_like.style.display = 'none'
    }
    if (localStorage.getItem('verificar') == 'false'){
        like.classList.remove('like')
        deslike.classList.add('deslike')
        resposta_like.style.display = 'none'
        span_like.style.display = 'block'
    }
}