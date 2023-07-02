const modules = require('../../background.js')
const lua = document.getElementById('lua')
lua.addEventListener('click',function(){
    modules.background_lua(lua)
})