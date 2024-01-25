'''
Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
  MinStack() initializes the stack object.
  void push(int val) pushes the element val onto the stack.
  void pop() removes the element on the top of the stack.
  int top() gets the top element of the stack.
  int getMin() retrieves the minimum element in the stack.
  You must implement a solution with O(1) time complexity for each function.

Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
'''

# Time Complexity: O(1)
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_val = []

    def push(self, val: int) -> None:
        # If there are no minimum values or the current value is <= to
        #   the last minimum value -> insert the new minimum to the top of the stack
        if self.min_val == [] or val <= self.min_val[0]:
            self.min_val.insert(0, val)
        
        # Insert the new value to the top of the stack
        self.stack.insert(0, val)

    def pop(self) -> None:
        # If the current value to be popped is the last minimum value (current minimum)
        #   -> pop the value from the stack and the minimum values stack
        if self.stack[0] == self.min_val[0]:
            self.min_val = self.min_val[1:]
        self.stack = self.stack[1:]

    def top(self) -> int:
        return self.stack[0]

    def getMin(self) -> int:
        return self.min_val[0]

