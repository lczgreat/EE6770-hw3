import uvicorn
from fastapi import FastAPI
from typing import Union
from fastapi.middleware.cors import CORSMiddleware

# 创建 FastAPI 应用实例
app = FastAPI()

# 跨域配置
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,         # 允许所有来源
    allow_credentials=True,       # 允许携带凭据
    allow_methods=["*"],          # 允许所有 HTTP 方法
    allow_headers=["*"],          # 允许所有请求头
)

# 根路由
@app.get("/", tags=["Root"])
def read_root():
    return {"Hello": "Chenzhi Lu"}

# 带路径参数的路由
@app.get("/uni/{uni_id}")
def read_item(uni_id: str, q: Union[str, None] = None):
    return {"uni_id": uni_id, "q": q}

# 启动服务
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
