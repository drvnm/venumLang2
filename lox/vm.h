#ifndef clox_vm_h
#define clox_vm_h

#include "chunk.h"
#include "value.h"

#define STACK_MAX 256

typedef struct
{
    Chunk *chunk;           // chunk to be executed
    uint8_t *ip;            // instruction pointer
    Value stack[STACK_MAX]; // stack
    Value *stackTop;        // stack top
} VM;

// codes that the VM can return
typedef enum
{
    INTERPRET_OK,
    INTERPRET_COMPILE_ERROR,
    INTERPRET_RUNTIME_ERROR
} InterpretResult;

void initVM();
void freeVM();
InterpretResult interpret(Chunk *chunk);
void push(Value value);
Value pop();

#endif