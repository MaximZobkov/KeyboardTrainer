message_input.onkeypress = handle;
var string_s = message_input.getAttribute('placeholder');
var loops = message_input.getAttribute('about');
var name = 'element'
var ind = 1;
var number = 0;
var error = 0;
var error_start = 0;

function handle(e) {
    if (string_s.length == 0){
        if (ind + 1 == loops){
            document.getElementById('itog').textContent = "Вы молодец, на сегодня хватит";
        }
        else {
            var mas = document.getElementById(name + String(ind)).textContent;
            string_s = mas;
            ind += 1;
        }
    }
    else{
        if (e.key === string_s[0]) {
            string_s = string_s.slice(1);
            message_input.setAttribute('class', "completed");
        }
        else {
            message_input.setAttribute('class', "not_completed");
        }
    }
    message_input.setAttribute('placeholder', string_s);
}