# 0x11. ES6 data manipulation




### Learning Objectives

* How to use map, filter and reduce on arrays
* Typed arrays
* The Set, Map, and Weak link data structures



### Demo

```
export default function getListStudents() {
  return [
    { id: 1, firstName: 'Guillaume', location: 'San Francisco' },
    { id: 2, firstName: 'James', location: 'Columbia' },
    { id: 5, firstName: 'Serena', location: 'San Francisco' },
  ];
}

```


```
Jaafar@Fares:~$ cat 0-main.js
import getListStudents from "./0-get_list_students.js";

console.log(getListStudents());

Jaafar@Fares:~$ 
Jaafar@Fares:~$ npm run dev 0-main.js 
[
  { id: 1, firstName: 'Guillaume', location: 'San Francisco' },
  { id: 2, firstName: 'James', location: 'Columbia' },
  { id: 5, firstName: 'Serena', location: 'San Francisco' }
]
Jaafar@Fares:~$ 

```






### Made by [Jaafar Fares](https://github.com/jaafarfares) for [Holberton School](https://www.holbertonschool.com/)
