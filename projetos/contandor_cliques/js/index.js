const btn_button = document.getElementById('btn')
let contador = 0
btn_button.addEventListener('click',function(){
    const p_clicks = document.getElementById('p')
    const clicks = document.getElementById('clicks')
    clicks.innerText = contador++
    btn_button.style.transition = '0'
    const animation = btn_button.animate([
        {boxShadow: 'inset 2px 2px 2px 1px black'},
        {boxShadow: 'inset 0 0 0 0 black'}
    ],
    {
        duration: 500
    }
)  
})
const btn_reset_button = document.getElementById('btn-reset')
btn_reset_button.addEventListener('click',() => {
    const clicks = document.getElementById('clicks')
    clicks.innerText = contador = 0
    btn_reset_button.animate(
        [
            {boxShadow: 'inset 2px 2px 2px black'},
            {boxShadow: 'inset 0 0 0'}
        ],
        {
            duration:500
        }
    )
})