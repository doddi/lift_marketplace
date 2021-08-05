#!/usr/bin/env python3
import sys
from sonatypeliftlib.apiv1 import ApiV1, ToolNote

class HelloWorld(ApiV1):
    def tool_applicable(self):
        return ApiV1.is_applicable()

    def tool_run(self):
        tool_notes = []

        tn1 = ToolNote("Hello", "Hello world Message", "hello.cpp", None, None)
        tool_notes.append(tn1)
        return tool_notes

def main():
    tool = HelloWorld("HelloWorld", sys.argv)
    tool.service()

if __name__ == "__main__":
    main()

