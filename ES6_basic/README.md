# ES6 Basics

- ES6(ECMAScript 2015) is a significant update to the JavaScript language that introduces new syntax and features, enhancing the language's readability and capability.

- New feautures such as 'let' and 'const' for variable declaration, arrow functions and concise function syntax, template literals for improved string formatting and more. Enhancing the overall functionality of JS code.
// Example using let and arrow function
let square = (x) => x * x;
console.log(square(5)); //Output: 25

- Constant vs. Variable, a variable declared with 'let' can be reassigned while a variable declared with 'const' is a *constant* and cannot be reassigned after initalization, hence creating an immutable value.

- Block-Scoped Variables, while using 'let' and 'const', limiting the variables scope to the block, statement, or expression in which it is defines, improving code maintainability and reducing unintended side effects.

- Arrow functions, provide a concise syntax for writing functions with implicit return for one-line expressions and automatically inferting the 'this' value from the surrounding scope, making them particularly useful for callback fucntions and improving code readability.

- Rest and Spread Parameters, the *rest* parameter('...') allows functions to accept an indefinite number of arguments as an array, while the *spread* operator is used to spread elements of an iterable (like an array) into another array or function call, enhancing flexibility in funciton definition and calls.

- String Templating, ES^ introduces template literals, allowing the embedding of expressions within string literals using backticks ('`') providing a more readable and concise way to create strings with variables and expressions.

- Object Creation in ES6, simplifies abject creation with concise sytaanx for defining properties and methods, making it more intuitive and reducing boilerplate code, particularly with the introduction of classes for object-oriented programming.

- Iterators and for/of loops, allowing objects to define their iteration behavior and the 'for/of' loop for easily iterating over iterable objects liek arrays, improving the handling of collections and sequences in JS.
