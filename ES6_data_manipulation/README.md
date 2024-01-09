# ES6 Data Manipulation
- In ES6, JavaScript introduced these array methods to simplify and enhance the manipulation of arrays.

- map: The map method creates a new array by applying a function to each element of the original array. It transforms each element based on the provided function and returns a new array of the same length.
    const numbers = [1, 2, 3, 4];
    const doubled = numbers.map(num => num * 2);
    // doubled is now [2, 4, 6, 8]

- Alos, Map is a collection of key-value pairs, similar to an object, but with more flexibility in the types of keys.
    const userRoles = new Map();
    userRoles.set('John', 'Admin');
    userRoles.set('Jane', 'User');
    // userRoles is now { 'John' => 'Admin', 'Jane' => 'User' }

- filter: The filter method creates a new array containing only the elements that pass a provided condition.
    const numbers = [1, 2, 3, 4];
    const evens = numbers.filter(num => num % 2 === 0);
    // evens is now [2, 4]

- reduce: The reduce method executes a reducer function on each element of the array, resulting in a single accumulated value.
    const numbers = [1, 2, 3, 4];
    const sum = numbers.reduce((acc, num) => acc + num, 0);
    // sum is now 10

- Typed Arrays are a set of array-like objects introduced in ES6 that provide a way to work with binary data in a more controlled manner. They include Int8Array, Uint8Array, Int16Array, Uint16Array, and so on.
    const buffer = new ArrayBuffer(4); // 4 bytes
    const int8Array = new Int8Array(buffer);
    int8Array[0] = 42;
    console.log(int8Array[0]); // 42

- Typed Arrays allow for efficient manipulation of binary data and are especially useful in scenarios where precise control over memory is required, such as working with images or networking.

- Set: A Set is a collection of values where each value must be unique. It's useful for storing a list of unique items.
    const uniqueNumbers = new Set([1, 2, 3, 1]);
    // uniqueNumbers is now {1, 2, 3}

- WeakLink: WeakMap and WeakSet are variations of Map and Set that allow the garbage collector to reclaim their associated memory if there are no other references to the keys.
