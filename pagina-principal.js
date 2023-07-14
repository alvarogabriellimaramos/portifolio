const button_clique = document.getElementById('btn-clique')
let contador = 1
button_clique.addEventListener('click',function(){
    const cont = document.getElementById('cont')
    cont.innerText = `${contador++} cliques`
    if (contador == 21){
        contador = 0
    }
})
