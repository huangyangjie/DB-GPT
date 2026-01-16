#!/usr/bin/env python3
"""
Test script to verify the fix for single_prompt() method in APIChatCompletionRequest.
"""

from dbgpt.core.schema.api import APIChatCompletionRequest

# Test case 1: Multiple messages, should return last user message
test_messages_1 = [
    {"role": "user", "content": "你好，我叫黄杨杰，你叫什么名字？"},
    {"role": "assistant", "content": "你好，黄杨杰！我叫通义千问，是阿里巴巴集团旗下的通义实验室研发的超大规模语言模型。"},
    {"role": "user", "content": "我头疼，挂哪个科？"}
]

request_1 = APIChatCompletionRequest(
    model="test-model",
    messages=test_messages_1
)

result_1 = request_1.single_prompt()
print(f"Test 1 result: '{result_1}'")
print(f"Test 1 expected: '我头疼，挂哪个科？'")
print(f"Test 1 passed: {result_1 == '我头疼，挂哪个科？'}")
print()

# Test case 2: Single user message, should return it
test_messages_2 = [
    {"role": "user", "content": "你好，我叫黄杨杰，你叫什么名字？"}
]

request_2 = APIChatCompletionRequest(
    model="test-model",
    messages=test_messages_2
)

result_2 = request_2.single_prompt()
print(f"Test 2 result: '{result_2}'")
print(f"Test 2 expected: '你好，我叫黄杨杰，你叫什么名字？'")
print(f"Test 2 passed: {result_2 == '你好，我叫黄杨杰，你叫什么名字？'}")
print()

# Test case 3: String messages, should return the string
test_messages_3 = "你好，我叫黄杨杰，你叫什么名字？"

request_3 = APIChatCompletionRequest(
    model="test-model",
    messages=test_messages_3
)

result_3 = request_3.single_prompt()
print(f"Test 3 result: '{result_3}'")
print(f"Test 3 expected: '你好，我叫黄杨杰，你叫什么名字？'")
print(f"Test 3 passed: {result_3 == '你好，我叫黄杨杰，你叫什么名字？'}")
print()

# Test case 4: Multiple messages with system message, should return last user message
test_messages_4 = [
    {"role": "system", "content": "你是一个医疗助手，帮助用户解答医疗相关问题。"},
    {"role": "user", "content": "你好，我叫黄杨杰，你叫什么名字？"},
    {"role": "assistant", "content": "你好，黄杨杰！我是医疗助手，很高兴为你服务。"},
    {"role": "user", "content": "我头疼，挂哪个科？"}
]

request_4 = APIChatCompletionRequest(
    model="test-model",
    messages=test_messages_4
)

result_4 = request_4.single_prompt()
print(f"Test 4 result: '{result_4}'")
print(f"Test 4 expected: '我头疼，挂哪个科？'")
print(f"Test 4 passed: {result_4 == '我头疼，挂哪个科？'}")
print()

# Summary
all_passed = all([
    result_1 == '我头疼，挂哪个科？',
    result_2 == '你好，我叫黄杨杰，你叫什么名字？',
    result_3 == '你好，我叫黄杨杰，你叫什么名字？',
    result_4 == '我头疼，挂哪个科？'
])

print(f"All tests passed: {all_passed}")
