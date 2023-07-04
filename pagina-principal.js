const lua = document.getElementById('moon')
const li_1 = document.getElementById('li-1')
lua.addEventListener('click',function(){
    document.body.style.backgroundColor = 'black'
    document.body.style.color = 'white'
    lua.style.display = 'none'
    const sol = document.createElement('img')
    sol.src = 'https://cdn-icons-png.flaticon.com/512/2698/2698194.png'
    sol.alt = 'Icone sol'
    sol.style.width = '30px'
    sol.style.position = 'relative'
    sol.style.left = '-8px'
    sol.style.top = '1px'
    sol.addEventListener('mouseenter',function(){
        sol.style.filter = 'drop-shadow(0 0 0.80px yellow)'
    })
    sol.addEventListener('mouseout',function(){
        sol.style.filter = 'drop-shadow ( 0 0 0 black)'
    })
    sol.addEventListener('click',function(){
        document.body.style.backgroundColor = 'white'
        document.body.style.color = 'black'
        sol.style.display = 'none'
        lua.style.display = 'inline-block'
    })
    li_1.appendChild(sol)
})