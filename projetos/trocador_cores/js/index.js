// colocar um loop que anda um elemento toda  vez que o usuario clicar
const btn_1 = document.getElementById('button-1')
const btn_2 = document.getElementById('button-2')
const container = document.getElementById('container')
const list = ['blue','yellow','green','red','black','pink','orange']
let contador = 0

btn_1.addEventListener('click',function(){
    contador ++ 
    document.body.style.backgroundColor = list[contador]
    if (contador >= list.length ){
        contador = 0
        document.body.style.backgroundColor = list[contador]
    }
})
btn_2.addEventListener('click',function(){
    contador ++ 
    container.style.backgroundColor = list[contador]
    if (contador >= list.length){
        contador = 0 
        container.style.backgroundColor = list[contador]
    }
    if (contador == 4){
        container.style.color = 'white'
    }
    if (contador > 4 || contador < 4){
        container.style.color = 'black'
    }
})