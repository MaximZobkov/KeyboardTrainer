message_input.onkeypress = handle;
var string_s = message_input.getAttribute('placeholder');
var number = 0;
var error = 0;
var error_start = 0;

function handle(e) {
    /*if (e.key == Backspace){
        let string_ss = message_input.getAttribute('text');
        message_input.setAttribute('text', string_ss);
    }*/
    if (e.key === string_s[0]) {
        string_s = string_s.slice(1);
        message_input.setAttribute('placeholder', string_s);
    }
    else {
        if (e.key == "Backspace"){
            string_s = "" + string_s
        }
    }
}



//second chance
/*document.addEventListener('keypress', function(event) {
      alert(string[number]);
      number += 1;
    });*/