# SPDX-FileCopyrightText: Copyright 2025 Arm Limited and/or its affiliates <open-source-office@arm.com>
# SPDX-License-Identifier: Apache-2.0

from abc import ABC, abstractmethod


class LLMProvider(ABC):
    def __init__(self):
        self.token_usage = {
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "total_tokens": 0,
            "embedding_tokens": 0,
        }

    def estimate_tokens(self, text):
        return len(str(text)) // 4 if text else 0

    def add_token_usage(self, prompt_tokens=0, completion_tokens=0, embedding_tokens=0):
        self.token_usage["prompt_tokens"] += prompt_tokens
        self.token_usage["completion_tokens"] += completion_tokens
        self.token_usage["embedding_tokens"] += embedding_tokens
        self.token_usage["total_tokens"] = (
            self.token_usage["prompt_tokens"]
            + self.token_usage["completion_tokens"]
            + self.token_usage["embedding_tokens"]
        )

    def get_token_usage(self):
        return self.token_usage.copy()

    def reset_token_usage(self):
        self.token_usage = {
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "total_tokens": 0,
            "embedding_tokens": 0,
        }

    @abstractmethod
    def get_embed_model_code(self):
        """Return a code embedding model for vector store."""
        pass

    @abstractmethod
    def get_embed_model_docs(self):
        """Return a docs embedding model for vector store."""
        pass

    @abstractmethod
    def get_chat_model(self, **kwargs):
        """Return a LangChain chat model instance."""
        pass

    @abstractmethod
    def get_query_engine_class(self):
        """Return the LlamaIndex LLM class used for query engines."""
        pass

    @abstractmethod
    def get_query_model_kwargs(self):
        """Return kwargs for constructing the query engine LLM."""
        pass
