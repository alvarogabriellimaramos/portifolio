const moon = document.getElementById('moon')
const li_1 = document.getElementById('li-1')
const h2 = document.getElementById('h2')
moon.addEventListener('click',function(){
    document.body.style.backgroundColor = 'black'
    document.body.style.color = 'white'
    moon.style.display = 'none'
    h2.style.backgroundImage = 'linear-gradient(to right,rgba(255, 255, 255, 0.027),white)'
    const sol = document.createElement('img')
    sol.src = 'https://cdn-icons-png.flaticon.com/512/2698/2698194.png'
    sol.alt = 'Icone sol '
    sol.style.width = '30px'
    sol.style.cursor = 'pointer'
    sol.addEventListener('mouseenter',function(){
        sol.style.filter = 'drop-shadow(0 0 0.80px yellow)'
    })
    sol.addEventListener('mouseout',function(){
       sol.style.filter = 'drop-shadow(0 0 0 black)'
    })
    sol.addEventListener('click',function(){
        document.body.style.backgroundColor = 'white'
        document.body.style.color = 'black'
        sol.style.display = 'none'
        moon.style.display = 'inline-block'
        h2.style.backgroundImage = 'linear-gradient(to right ,rgba(0, 0, 0, 0.151),black)'
        
    })
    li_1.appendChild(sol)
})
