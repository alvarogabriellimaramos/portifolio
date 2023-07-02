const lua = document.getElementById('lua')
const shadow_sol = img => {
    img.addEventListener('mouseenter',function(){
        img.style.filter = 'drop-shadow(0 0 0.2px white)'
    })
    img.addEventListener('mouseout',function(){
        img.style.filter = 'drop-shadow(0 0 0 black)'
    })
}
const background_sol = (img) => {
    document.body.style.backgroundColor = 'white'
    document.body.style.color = 'black'
    img.style.display = 'none'
    lua.style.display = 'flex'
}
const inputs_black = (input_1,input_2) => {
    input_1.style.backgroundColor = 'black'
    input_2.style.backgroundColor = 'black'
    input_1.style.color = 'white'
    input_2.style.color = 'white'
}
const inputs_white = (input_1,input_2) => {
    input_1.style.backgroundColor = '#F6F8FA'
    input_2.style.backgroundColor = '#F6F8FA'
    input_1.style.color = 'black'
    input_2.style.color = 'black'
}
const background_lua = (img) => {
    const input_1 = document.getElementById('email')
    const input_2 = document.getElementById('password')
    inputs_black(input_1,input_2)
    const li_1 = document.getElementById('li-1')
    document.body.style.backgroundColor = '#0D1117'
    document.body.style.color = 'white'
    img.style.display = 'none'
    const sol_img = document.createElement('img')
    sol_img.src = 'https://icones.pro/wp-content/uploads/2021/04/symbole-du-soleil-jaune.png'
    sol_img.alt = 'Icone sol '
    sol_img.style.width = '18px'
    sol_img.style.cursor = 'pointer'
    shadow_sol(sol_img)
    li_1.appendChild(sol_img)
    sol_img.addEventListener('click',function(){
        background_sol(sol_img)
        inputs_white(input_1,input_2)
    })

}
module.exports = {
    background_lua,
    background_sol
}