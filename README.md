# Interpreter

Interpreter of "self-made programming language". Designed lexer, parser and syntax analysis.
Its imitating common programming language for better understanding. Self-designed inner-statement communication system.

# Rules

### Assigning example

a = 20;

### If-else statement

if(a < 0) {
    a = a + 1;
} else {
    a = a - 1;
}

### For-loop

for i = 1:20 {
    if(a > 10) {
        break;
    }
    a = a + 1;
}

### While-loop

while(a > 0) {
    if(a == 0) {
        continue;
    }    
    a = a - 1;
}

### Print

print("something");

### Return

return a;

# ToDo List

Napraw nawiasy "(" ")" w obliczeniach

Dodaj funkcje

Dodaj losowanie

Dodaj wczytywanie z terminala wartości: inputy