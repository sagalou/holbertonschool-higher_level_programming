# 🟡 JavaScript - Warm up

> Introduction to JavaScript scripting fundamentals — variables, functions, control flow, and more, built at Holberton School.

---

## 📖 Description & Objectives

This project covers the core concepts of JavaScript as a scripting language. It serves as a foundation before using JavaScript for web front-end development.

**Learning objectives:**
- Understand why JavaScript is amazing
- Create variables and constants (`let`, `const`) — never `var`
- Know all available data types in JavaScript
- Use `if`, `if...else`, `while`, `for`, `break`, `continue`
- Write and call functions, understand scope and return values
- Manipulate objects and arrays
- Import files with `require`

---

## 🛠 Technologies Used

| Tool | Version |
|------|---------|
| Node.js | 14.x |
| Semistandard | 16.x |
| Style | Semistandard (Standard + semicolons) |

---

## ✅ Prerequisites

- OS: Ubuntu 20.04 LTS
- Node.js 14.x
- semistandard 16.x

**Install Node.js 14:**
```bash
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs
```

**Install semistandard:**
```bash
sudo npm install semistandard --global
```

---

## ⚙️ Installation

```bash
git clone https://github.com/sagalou/holbertonschool-higher_level_programming.git
cd holbertonschool-higher_level_programming/javascript-warm_up
```

---

## 🚀 How to Use

All scripts are executable. Run any file directly:

```bash
chmod +x <filename>.js
./<filename>.js
```

**Example — Task 0:**
```bash
./0-javascript_is_amazing.js
# → JavaScript is amazing
```

**Check code style:**
```bash
semistandard ./<filename>.js
```

---

## 📋 Tasks

| # | File | Description |
|---|------|-------------|
| 0 | `0-javascript_is_amazing.js` | Print "JavaScript is amazing" using a `const` variable |
| 1 | `1-multi_languages.js` | Print 3 lines using `console.log` |
| 2 | `2-arguments.js` | Print a message based on the number of arguments passed |
| 3 | `3-value_argument.js` | Print the first argument passed to the script |
| 4 | `4-concat.js` | Print two arguments in the format `<arg1> is <arg2>` |
| 5 | `5-to_integer.js` | Print an integer if the first argument can be converted |
| 6 | `6-multi_languages_loop.js` | Print 3 lines using a loop and an array |
| 7 | `7-multi_c.js` | Print "C is fun" x times |
| 8 | `8-square.js` | Print a square of size n using the character `X` |
| 9 | `9-add.js` | Print the addition of two integers |
| 10 | `10-factorial.js` | Compute and print a factorial recursively |
| 11 | `11-second_biggest.js` | Find the second biggest integer in a list of arguments |
| 12 | `12-object.js` | Update the value of an object |
| 13 | `13-add.js` | Export a function `add` using `module.exports` |

---

## 📁 Project Structure

```
javascript-warm_up/
├── 0-javascript_is_amazing.js
├── 1-multi_languages.js
├── 2-arguments.js
├── 3-value_argument.js
├── 4-concat.js
├── 5-to_integer.js
├── 6-multi_languages_loop.js
├── 7-multi_c.js
├── 8-square.js
├── 9-add.js
├── 10-factorial.js
├── 11-second_biggest.js
├── 12-object.js
├── 13-add.js
└── README.md
```

---

## 👤 Author

**Sagal Haider** — [@sagalou](https://github.com/sagalou)  
Holberton School — Cybersecurity track