// TEST FILE: intentional problems for ESLint to detect.
var unusedVariable = 10;                 // no-var, no-unused-vars

function check(value) {
  if (value == null) {                   // eqeqeq
    return eval("1 + 1");                // no-eval
  }
  console.log("debugging");              // no-console (if enabled)
  undefinedFunction(value);              // no-undef
}

function render(userInput) {
  // XSS pattern: untrusted input written straight into the page
  document.getElementById("out").innerHTML = userInput;
}

module.exports = { check, render };
