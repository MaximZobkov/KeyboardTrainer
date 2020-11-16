message_input.onkeypress = handle;
var string_s = message_input.getAttribute('placeholder');
var loops = message_input.getAttribute('about');
var mas = new Array(message_input.getAttribute('my_attribute'));
var ind = 1;
var number = 0;
var error = 0;
var error_start = 0;

function handle(e) {
    /*if (e.key == Backspace){
        let string_ss = message_input.getAttribute('text');
        message_input.setAttribute('text', string_ss);
    }*/
    if (string_s.length == 0){
        alert('1');
        alert(mas);
        let x = mas[1];
        alert(x);
        let el = mas[ind];
        string_s = el;
        index += 1;
    }
    if (e.key === string_s[0]) {
        string_s = string_s.slice(1);
    }
    /*else {
        alert('1');
        if (e.key != string_s[0] && e.key != Backspace){
            string_s = "<" + string_s;
        }
        if (e.key == Backspace){
            string_s = string_s.slice(1);
        }
    }*/
    message_input.setAttribute('placeholder', string_s);
}



//second chance
/*document.addEventListener('keypress', function(event) {
      alert(string[number]);
      number += 1;
    });*/