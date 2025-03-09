(module
  ;; Import the 'console.log' function from JavaScript
  (import "env" "log" (func $log (param i32)))

  ;; Define the WebAssembly function 'hi_world'
  (func $hi_world
    (call $log (i32.const 0))  ;; Call 'log' function with a pointer to "Hi, World!" string
  )

  ;; Define the memory for the module (needed to store the string)
  (memory 1)

  ;; Export the 'hi_world' function to be called from JavaScript
  (export "hi_world" (func $hi_world))

  ;; Define the string "Hi, World!" in memory
  (data (i32.const 0) "Hi, World!\00
    ")
)
