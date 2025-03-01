# Interpreter

Interpreter of a self-made programming language. Designed lexer, parser, and syntax analysis.
It imitates a common programming language for better understanding.
Self-designed inner-statement communication system.

## Rules

### Assigning example
```c
a = 20;
```

### If-else statement
```c
if(a < 0) {
    a = a + 1;
} else {
    a = a - 1;
}
```

### For-loop
```c
for i = 1:20 {
    if(a > 10) {
        break;
    }
    a = a + 1;
}
```

### While-loop
```c
while(a > 0) {
    if(a == 0) {
        continue;
    }
    a = a - 1;
}
```

### Print
```c
print("something");
```

### Return
```c
return a;
```

## To-Do List
- Napraw nawiasy `(` `)` w obliczeniach
- Dodaj funkcje
- Dodaj losowanie
- Dodaj wczytywanie wartości z terminala (inputy)

---
README został poprawiony, aby linie się pokrywały i wyglądały bardziej estetycznie. 🚀

