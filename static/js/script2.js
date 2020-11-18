message_input.onkeypress = handle;
alert("1");
var string_s = not_completed.getAttribute('my_attribute');
var string_s2 = completed.getAttribute('my_attribute');
alert(string_s);
alert(string_s2);
var ind = 1;
var number = 0;
var error = 0;
var error_start = 0;

function handle(e) {
    if (e.key === string_s[0]) {
        string_s = string_s.slice(1);
        string_s2 = string_s2 + e.key;
    }
    not_completed.setAttribute('my_attribute', string_s);
    completed.setAttribute('my_attribute', string_s2)
    document.getElementById("not_completed").textContent  = string_s;
    document.getElementById("completed").textContent = string_s2;
}