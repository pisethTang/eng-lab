"""
A fake llm provider for the lab. It copies the shape of OpenAI's chat API, so the gateway (and later LiteLLM)
can talk to it like a real provider and cost nothing. 


Run 2 copies to act as 2 different providers: 
    uv run fake_llm.py --name provider-a --port 9001
    uv run fake_llm.py --name provider-b --port 9002
"""


from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
import random 
import time 

import uuid 

import argparse
import uvicorn


class Message(BaseModel):
    role: str # "system", "user", "assistant"
    content: str 

class ChatRequest(BaseModel):
    model: str
    messages: list[Message]


def count_tokens(text: str) -> int:
    # Real providers split text into tokens (word pieces) and bill per token. 
    # Rule of thumb for English: 1 token is about 4 characters.
    return max(1, len(text)//4)



def build_app(name: str, api_key: str, fail_rate: float) -> FastAPI:
    app = FastAPI(title=name)

    @app.post("/v1/chat/completions")
    def chat(req: ChatRequest, authorization: str = Header(default="")):
        # 1. Check the caller sent this provider's real API key.
        if authorization != f"Bearer {api_key}":
            raise HTTPException(status_code=401, detail=f"{name}: invalid api key")
        # 2. Someitmes pretend to be overloaed, like real providers do.
        if random.random() < fail_rate:
            raise HTTPException(status_code=429, detail=f"{name}: rate limited, try later")

        # 3. Pretend the model is thinking.
        time.sleep(random.uniform(0.2, 0.6))

        # 4. build a fake answer and report how many tokens were used. 
        prompt = " ".join(m.content for m in req.messages)
        answer = f"[{name} / {req.model}] You said: {prompt[:80]}"
        prompt_tokens = count_tokens(prompt)
        completion_tokens = count_tokens(answer)

        return {
            "id": f"chatcmpl-{uuid.uuid4().hex[:8]}",
            "object": "chat.completion",
            "created": int(time.time()),
            "model": req.model,
            "choices": [
                {
                    "index": 0,
                    "message": {"role": "assistant", "content": answer},
                    "finish_reason": "stop",
                }
            ], 
            "usage": {
                "prompt_tokens": prompt_tokens,
                "completion_tokens": completion_tokens,
                "total_tokens": prompt_tokens + completion_tokens,
            }

        }
    return app 



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a fake LLM provider")
    parser.add_argument("--name", default="provider-a")
    parser.add_argument("--port", type=int, default=9001)
    parser.add_argument(
        "--fail-rate", type=float, default=0.0,
        help="share of requests to reject with 429, e.g. 0.3 = 30%",
    )

    args = parser.parse_args()

    api_key = f"sk-real-{args.name}"
    print(f"{args.name} listening on port {args.port}, real key = {api_key}")
    uvicorn.run(build_app(args.name, api_key, args.fail_rate), host="127.0.0.1", port=args.port)