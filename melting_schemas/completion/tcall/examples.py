def raw_tcall_request_examples():
    class Config:
        smart_unions = True
        examples = {
            "Raw Tool Selection": {
                "value": {
                    "tools": [
                        {
                            "type": "function",
                            "function": {
                                "name": "my_function",
                                "description": "This is my function",
                                "parameters": {
                                    "type": "object",
                                    "properties": {
                                        "my_param": {
                                            "type": "string",
                                            "description": "This is my parameter",
                                        }
                                    },
                                    "required": ["my_param"],
                                },
                            },
                        }
                    ],
                    "messages": [
                        {
                            "content": "Hello",
                            "role": "user",
                        }
                    ],
                    "settings": {
                        "model": "gpt-4o",
                        "tool_choice": "auto",
                    },
                }
            },
            "Raw Tool Calling": {
                "value": {
                    "tools": [
                        {
                            "type": "http",
                            "name": "my_function",
                            "callee": {
                                "method": "GET",
                                "forward_headers": ["x-user-email"],
                                "headers": {"authorization": "my-special-api-token"},
                                "url": "https://datasources.allai.digital/{name}/search",
                                "static": {
                                    "query": {"limit": 2},
                                    "body": {"top_k": 10},
                                },
                                "dynamic": {
                                    "path": ["name"],
                                    "body": ["top_k", "search_query"],
                                },
                            },
                            "json_schema": {
                                "type": "function",
                                "function": {
                                    "name": "my_function",
                                    "description": "This is my function",
                                    "parameters": {
                                        "type": "object",
                                        "properties": {
                                            "my_param": {
                                                "type": "string",
                                                "description": "This is my parameter",
                                            }
                                        },
                                        "required": ["my_param"],
                                    },
                                },
                            },
                        }
                    ],
                    "messages": [
                        {
                            "content": "Hello",
                            "role": "user",
                        }
                    ],
                    "settings": {
                        "model": "gpt-4o",
                        "tool_choice": "auto",
                    },
                }
            },
            "Native Tool Calling": {
                "value": {
                    "tools": ["example-tool-name"],
                    "messages": [
                        {
                            "content": "Hello",
                            "role": "user",
                        }
                    ],
                    "settings": {
                        "model": "gpt-4o",
                        "tool_choice": "auto",
                    },
                }
            },
        }